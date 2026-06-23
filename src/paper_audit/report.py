"""Synthetic audit report generation from JSON configuration files."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .checks import (
    arrhenius_fit,
    calculate_conductivity_from_geometry,
    calculate_faradaic_efficiency,
    calculate_statistics,
    check_component_sum,
    check_current_density_power_density_relation,
    improvement_ratio,
    reduction_ratio,
    relative_difference_pct,
)
from .output import normalize_value
from .tolerance_report import build_tolerance_report_from_csv


@dataclass(frozen=True)
class ReportCheckResult:
    """One check result in a generated audit report."""

    check_id: str
    check_type: str
    title: str
    status: str
    result: dict[str, Any]
    note: str


def _as_path(config_path: Path, value: str) -> str:
    path = Path(value)
    if path.is_absolute():
        return str(path)
    return str((config_path.parent / path).resolve())


def _status_from_bool(value: bool | None) -> str:
    if value is True:
        return "PASS"
    if value is False:
        return "FLAG"
    return "INFO"


def _normalize_mapping(record: dict[str, Any]) -> dict[str, Any]:
    return {key: normalize_value(value) for key, value in record.items()}


def _run_arrhenius(params: dict[str, Any]) -> tuple[str, dict[str, Any], str]:
    result = arrhenius_fit(
        temperature_c=params["temperature_c"],
        resistance=params["resistance"],
        use_rt_correction=bool(params.get("use_rt_correction", False)),
    )
    record = {
        "fitted_quantity": "ln(R*T)" if params.get("use_rt_correction") else "ln(R)",
        "slope": result.slope,
        "intercept": result.intercept,
        "r_squared": result.r_squared,
        "ea_ev": result.ea_ev,
    }
    return "INFO", record, "Arrhenius fit completed. Review Ea and R^2 against the intended comparison."


def _run_statistics(params: dict[str, Any]) -> tuple[str, dict[str, Any], str]:
    stats = calculate_statistics(params["values"])
    target_std = stats.population_std if params.get("population_std") else stats.sample_std
    tolerance = float(params.get("tolerance_pct", 1.0))
    record: dict[str, Any] = {
        "n": stats.n,
        "mean": stats.mean,
        "sample_std": stats.sample_std,
        "population_std": stats.population_std,
    }
    checks: list[bool] = []
    if "reported_mean" in params:
        mean_diff = relative_difference_pct(float(params["reported_mean"]), stats.mean)
        mean_ok = mean_diff <= tolerance
        record["reported_mean_difference_pct"] = mean_diff
        record["reported_mean_within_tolerance"] = mean_ok
        checks.append(mean_ok)
    if "reported_std" in params:
        std_diff = relative_difference_pct(float(params["reported_std"]), target_std)
        std_ok = None if std_diff is None else std_diff <= tolerance
        record["reported_std_difference_pct"] = std_diff
        record["reported_std_within_tolerance"] = std_ok
        if std_ok is not None:
            checks.append(std_ok)
    status = "INFO" if not checks else _status_from_bool(all(checks))
    return status, record, "Statistics recalculation completed."


def _run_ratio(params: dict[str, Any]) -> tuple[str, dict[str, Any], str]:
    mode = params.get("mode", "improvement")
    if mode == "reduction":
        value = reduction_ratio(float(params["new"]), float(params["baseline"]))
    else:
        mode = "improvement"
        value = improvement_ratio(float(params["new"]), float(params["baseline"]))
    return "INFO", {"mode": mode, "ratio_pct": value}, "Ratio calculation completed."


def _run_dimensional(params: dict[str, Any]) -> tuple[str, dict[str, Any], str]:
    ok, calculated, diff = check_current_density_power_density_relation(
        power_density=float(params["power_density"]),
        current_density=float(params["current_density"]),
        voltage=float(params["voltage"]),
        tolerance_pct=float(params.get("tolerance_pct", 1.0)),
    )
    record = {
        "calculated_power_density": calculated,
        "difference_pct": diff,
        "relation_consistent": ok,
    }
    return _status_from_bool(ok), record, "Checked the P = j x V relation."


def _run_resistance_sum(params: dict[str, Any]) -> tuple[str, dict[str, Any], str]:
    result = check_component_sum(
        reported_total=float(params["reported_total"]),
        components=params["components"],
        tolerance_pct=float(params.get("tolerance_pct", 1.0)),
    )
    record = {
        "reported_total": result.reported_total,
        "component_sum": result.component_sum,
        "absolute_difference": result.absolute_difference,
        "relative_difference_pct": result.relative_difference_pct,
        "within_tolerance": result.within_tolerance,
    }
    return _status_from_bool(result.within_tolerance), record, "Checked reported total against listed components."


def _run_faradaic_efficiency(params: dict[str, Any]) -> tuple[str, dict[str, Any], str]:
    if "current_a" in params:
        current_a = float(params["current_a"])
    else:
        current_a = float(params["current_density_a_cm2"]) * float(params["area_cm2"])
    result = calculate_faradaic_efficiency(
        current_a=current_a,
        measured_flow_ml_min=float(params["measured_flow_ml_min"]),
        electrons_per_molecule=float(params["electrons_per_molecule"]),
        molar_volume_ml_per_mol=float(params.get("molar_volume_ml_mol", 22414.0)),
        reported_fe_pct=params.get("reported_fe_pct"),
        tolerance_pct_points=float(params.get("tolerance_pct_points", 5.0)),
    )
    record = {
        "current_a": result.current_a,
        "electrons_per_molecule": result.electrons_per_molecule,
        "theoretical_flow_100pct_ml_min": result.theoretical_flow_100pct_ml_min,
        "measured_flow_ml_min": result.measured_flow_ml_min,
        "calculated_fe_pct": result.calculated_fe_pct,
        "reported_fe_pct": result.reported_fe_pct,
        "fe_difference_pct_points": result.fe_difference_pct_points,
        "within_tolerance": result.within_tolerance,
    }
    return _status_from_bool(result.within_tolerance), record, "Calculated flow-based Faradaic efficiency."


def _run_conductivity_geometry(params: dict[str, Any]) -> tuple[str, dict[str, Any], str]:
    if "thickness_cm" in params:
        thickness_cm = float(params["thickness_cm"])
    else:
        thickness_cm = float(params["thickness_mm"]) / 10.0
    if "area_cm2" in params:
        area_cm2 = float(params["area_cm2"])
    else:
        diameter_cm = float(params["diameter_mm"]) / 10.0
        area_cm2 = math.pi * (diameter_cm / 2.0) ** 2
    result = calculate_conductivity_from_geometry(
        resistance_ohm=float(params["resistance_ohm"]),
        thickness_cm=thickness_cm,
        area_cm2=area_cm2,
        reported_conductivity_s_cm=params.get("reported_conductivity_s_cm"),
        tolerance_pct=float(params.get("tolerance_pct", 5.0)),
    )
    record = {
        "resistance_ohm": result.resistance_ohm,
        "thickness_cm": result.thickness_cm,
        "area_cm2": result.area_cm2,
        "calculated_conductivity_s_cm": result.calculated_conductivity_s_cm,
        "reported_conductivity_s_cm": result.reported_conductivity_s_cm,
        "relative_difference_pct": result.relative_difference_pct,
        "within_tolerance": result.within_tolerance,
    }
    return _status_from_bool(result.within_tolerance), record, "Calculated geometry-normalized conductivity."


def _run_tolerance_report(config_path: Path, params: dict[str, Any]) -> tuple[str, dict[str, Any], str]:
    report = build_tolerance_report_from_csv(
        csv_path=_as_path(config_path, params["csv"]),
        reported_column=params["reported_column"],
        reference_column=params["reference_column"],
        id_column=params.get("id_column"),
        tolerance_pct=float(params.get("tolerance_pct", 5.0)),
    )
    record = {
        "total_rows": report.total_rows,
        "pass_count": report.pass_count,
        "fail_count": report.fail_count,
        "tolerance_pct": report.tolerance_pct,
    }
    return _status_from_bool(report.fail_count == 0), record, "Built a row-level tolerance summary."


def run_report_check(config_path: Path, check: dict[str, Any]) -> ReportCheckResult:
    """Run one configured check."""
    check_type = check["type"]
    params = dict(check.get("params", {}))
    title = check.get("title", check_type)
    check_id = check.get("id", check_type)

    if check_type == "arrhenius":
        status, record, note = _run_arrhenius(params)
    elif check_type == "statistics":
        status, record, note = _run_statistics(params)
    elif check_type == "ratio":
        status, record, note = _run_ratio(params)
    elif check_type == "dimensional":
        status, record, note = _run_dimensional(params)
    elif check_type == "resistance-sum":
        status, record, note = _run_resistance_sum(params)
    elif check_type == "faradaic-efficiency":
        status, record, note = _run_faradaic_efficiency(params)
    elif check_type == "conductivity-geometry":
        status, record, note = _run_conductivity_geometry(params)
    elif check_type == "tolerance-report":
        status, record, note = _run_tolerance_report(config_path, params)
    else:
        raise ValueError(f"Unsupported report check type: {check_type}")

    return ReportCheckResult(
        check_id=check_id,
        check_type=check_type,
        title=title,
        status=status,
        result=_normalize_mapping(record),
        note=check.get("note", note),
    )


def build_report_from_json(config_path: str | Path) -> dict[str, Any]:
    """Build a report dictionary from a JSON config file."""
    path = Path(config_path)
    with path.open(encoding="utf-8") as handle:
        config = json.load(handle)
    checks = [run_report_check(path, check) for check in config.get("checks", [])]
    summary = {
        "checks_run": len(checks),
        "pass_count": sum(1 for check in checks if check.status == "PASS"),
        "flag_count": sum(1 for check in checks if check.status == "FLAG"),
        "info_count": sum(1 for check in checks if check.status == "INFO"),
    }
    return {
        "title": config.get("title", "Synthetic Audit Report"),
        "description": config.get("description", "Synthetic report generated by paper-audit."),
        "summary": summary,
        "checks": [
            {
                "id": check.check_id,
                "type": check.check_type,
                "title": check.title,
                "status": check.status,
                "result": check.result,
                "note": check.note,
            }
            for check in checks
        ],
    }


def format_report_markdown(report: dict[str, Any]) -> str:
    """Format a generated report as Markdown."""
    lines = [
        f"# {report['title']}",
        "",
        str(report.get("description", "")),
        "",
        "## Summary",
        "",
    ]
    for key, value in report["summary"].items():
        lines.append(f"- **{key}:** {value}")
    for index, check in enumerate(report["checks"], start=1):
        lines.extend(
            [
                "",
                f"## Check {index}: {check['title']}",
                "",
                f"- **id:** {check['id']}",
                f"- **type:** {check['type']}",
                f"- **status:** {check['status']}",
                f"- **note:** {check['note']}",
                "",
                "| field | value |",
                "|---|---:|",
            ]
        )
        for key, value in check["result"].items():
            lines.append(f"| {key} | {value} |")
    lines.append("")
    return "\n".join(lines)


def format_report_json(report: dict[str, Any]) -> str:
    """Format a generated report as JSON."""
    return json.dumps(report, indent=2, sort_keys=True)
