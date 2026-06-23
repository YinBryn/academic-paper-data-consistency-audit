"""Command-line interface for Academic Paper Data Consistency Audit."""

from __future__ import annotations

import argparse
import math
import sys

from .checks import (
    DEFAULT_MOLAR_VOLUME_ML_PER_MOL,
    arrhenius_fit,
    calculate_conductivity_from_geometry,
    calculate_faradaic_efficiency,
    calculate_statistics,
    check_component_sum,
    check_current_density_power_density_relation,
    check_diffusion_unit,
    check_potential_unit,
    improvement_ratio,
    reduction_ratio,
    relative_difference_pct,
)
from .demo import run_demo
from .output import OUTPUT_FORMATS, emit_record, emit_table
from .tolerance_report import build_tolerance_report_from_csv


def _add_output_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--output",
        choices=OUTPUT_FORMATS,
        default="text",
        help="Output format: text, json, markdown, or csv.",
    )


def _add_arrhenius_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("arrhenius", help="Fit Arrhenius resistance/ASR data and report Ea.")
    parser.add_argument("--temperature-c", nargs="+", type=float, required=True, help="Temperatures in Celsius.")
    parser.add_argument("--resistance", nargs="+", type=float, required=True, help="Resistance, Rp, or ASR values.")
    parser.add_argument("--use-rt-correction", action="store_true", help="Fit ln(R*T) instead of ln(R).")
    _add_output_argument(parser)
    parser.set_defaults(func=_run_arrhenius)


def _add_statistics_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("statistics", help="Recalculate mean/std from replicate values.")
    parser.add_argument("--values", nargs="+", type=float, required=True, help="Replicate values.")
    parser.add_argument("--reported-mean", type=float, help="Optional reported mean value.")
    parser.add_argument("--reported-std", type=float, help="Optional reported standard deviation.")
    parser.add_argument("--population-std", action="store_true", help="Compare against population std instead of sample std.")
    parser.add_argument("--tolerance-pct", type=float, default=1.0, help="Tolerance in percent.")
    _add_output_argument(parser)
    parser.set_defaults(func=_run_statistics)


def _add_ratio_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("ratio", help="Calculate improvement or reduction ratios.")
    parser.add_argument("--new", type=float, required=True, help="New or modified value.")
    parser.add_argument("--baseline", type=float, required=True, help="Baseline value.")
    parser.add_argument("--mode", choices=["improvement", "reduction"], default="improvement", help="Ratio convention to report.")
    _add_output_argument(parser)
    parser.set_defaults(func=_run_ratio)


def _add_dimensional_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("dimensional", help="Run dimensional and I-V-P checks.")
    parser.add_argument("--diffusion-unit", type=str, help="Check diffusion unit, e.g. 'cm^2/s'.")
    parser.add_argument("--potential-unit", type=str, help="Check potential unit, e.g. 'V' or 'eV'.")
    parser.add_argument("--power-density", type=float, help="Reported power density in W/cm^2.")
    parser.add_argument("--current-density", type=float, help="Current density in A/cm^2.")
    parser.add_argument("--voltage", type=float, help="Cell voltage in V.")
    parser.add_argument("--tolerance-pct", type=float, default=1.0, help="Tolerance in percent.")
    _add_output_argument(parser)
    parser.set_defaults(func=_run_dimensional)


def _add_resistance_sum_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser(
        "resistance-sum",
        help="Check whether reported total Rp/ASR equals the sum of listed components.",
    )
    parser.add_argument("--reported-total", type=float, required=True, help="Reported total resistance, Rp, or ASR value.")
    parser.add_argument("--components", nargs="+", type=float, required=True, help="Listed component resistances to sum.")
    parser.add_argument("--tolerance-pct", type=float, default=1.0, help="Tolerance in percent relative to the component sum.")
    _add_output_argument(parser)
    parser.set_defaults(func=_run_resistance_sum)


def _add_faradaic_efficiency_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser(
        "faradaic-efficiency",
        help="Calculate gas-flow-based Faradaic efficiency from current and electron stoichiometry.",
    )
    current_group = parser.add_mutually_exclusive_group(required=True)
    current_group.add_argument("--current-a", type=float, help="Total current in A.")
    current_group.add_argument("--current-density-a-cm2", type=float, help="Current density in A/cm^2; requires --area-cm2.")
    parser.add_argument("--area-cm2", type=float, help="Active area in cm^2 when using --current-density-a-cm2.")
    parser.add_argument("--measured-flow-ml-min", type=float, required=True, help="Measured product gas flow in mL/min.")
    parser.add_argument("--electrons-per-molecule", type=float, required=True, help="Electrons per product molecule, e.g. 2 or 4 depending on product stoichiometry.")
    parser.add_argument("--reported-fe-pct", type=float, help="Optional reported Faradaic efficiency in percent.")
    parser.add_argument("--tolerance-pct-points", type=float, default=5.0, help="Tolerance in FE percentage points.")
    parser.add_argument("--molar-volume-ml-mol", type=float, default=DEFAULT_MOLAR_VOLUME_ML_PER_MOL, help="Gas molar volume used for mL/min conversion.")
    _add_output_argument(parser)
    parser.set_defaults(func=_run_faradaic_efficiency)


def _add_conductivity_geometry_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser(
        "conductivity-geometry",
        help="Calculate conductivity from resistance, thickness, and electrode area.",
    )
    parser.add_argument("--resistance-ohm", type=float, required=True, help="Measured resistance in ohm.")
    thickness_group = parser.add_mutually_exclusive_group(required=True)
    thickness_group.add_argument("--thickness-cm", type=float, help="Sample thickness in cm.")
    thickness_group.add_argument("--thickness-mm", type=float, help="Sample thickness in mm.")
    area_group = parser.add_mutually_exclusive_group(required=True)
    area_group.add_argument("--area-cm2", type=float, help="Electrode/sample area in cm^2.")
    area_group.add_argument("--diameter-mm", type=float, help="Circular electrode/sample diameter in mm.")
    parser.add_argument("--reported-conductivity-s-cm", type=float, help="Optional reported conductivity in S/cm.")
    parser.add_argument("--tolerance-pct", type=float, default=5.0, help="Tolerance in percent.")
    _add_output_argument(parser)
    parser.set_defaults(func=_run_conductivity_geometry)


def _add_tolerance_report_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser(
        "tolerance-report",
        help="Batch compare reported values against source/reference values from a CSV file.",
    )
    parser.add_argument("--csv", required=True, help="CSV file containing reported and reference columns.")
    parser.add_argument("--reported-column", required=True, help="Column containing reported values.")
    parser.add_argument("--reference-column", required=True, help="Column containing source-data or reference values.")
    parser.add_argument("--id-column", help="Optional row identifier column, e.g. sample or condition.")
    parser.add_argument("--tolerance-pct", type=float, default=5.0, help="Relative tolerance in percent.")
    _add_output_argument(parser)
    parser.set_defaults(func=_run_tolerance_report)


def _add_demo_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("demo", help="Run a one-command synthetic demo workflow.")
    parser.set_defaults(func=_run_demo)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="paper-audit",
        description="Physics-informed data consistency checks for materials electrochemistry papers.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    _add_demo_parser(subparsers)
    _add_arrhenius_parser(subparsers)
    _add_statistics_parser(subparsers)
    _add_ratio_parser(subparsers)
    _add_dimensional_parser(subparsers)
    _add_resistance_sum_parser(subparsers)
    _add_faradaic_efficiency_parser(subparsers)
    _add_conductivity_geometry_parser(subparsers)
    _add_tolerance_report_parser(subparsers)
    return parser


def _run_demo(args: argparse.Namespace) -> int:
    del args
    return run_demo()


def _run_arrhenius(args: argparse.Namespace) -> int:
    result = arrhenius_fit(args.temperature_c, args.resistance, args.use_rt_correction)
    record = {
        "fitted_quantity": "ln(R*T)" if args.use_rt_correction else "ln(R)",
        "slope": result.slope,
        "intercept": result.intercept,
        "r_squared": result.r_squared,
        "ea_ev": result.ea_ev,
    }
    emit_record("Arrhenius fitting result", record, args.output)
    return 0


def _run_statistics(args: argparse.Namespace) -> int:
    stats = calculate_statistics(args.values)
    target_std = stats.population_std if args.population_std else stats.sample_std
    record: dict[str, object] = {
        "n": stats.n,
        "mean": stats.mean,
        "sample_std": stats.sample_std,
        "population_std": stats.population_std,
    }

    if args.reported_mean is not None:
        mean_diff = relative_difference_pct(args.reported_mean, stats.mean)
        record["reported_mean_difference_pct"] = mean_diff
        record["reported_mean_within_tolerance"] = mean_diff <= args.tolerance_pct
    if args.reported_std is not None:
        std_diff = relative_difference_pct(args.reported_std, target_std)
        record["reported_std_difference_pct"] = std_diff
        record["reported_std_within_tolerance"] = None if std_diff is None else std_diff <= args.tolerance_pct

    emit_record("Statistics recalculation result", record, args.output)
    return 0


def _run_ratio(args: argparse.Namespace) -> int:
    if args.mode == "reduction":
        value = reduction_ratio(args.new, args.baseline)
        record = {"mode": "reduction", "ratio_pct": value}
        title = "Reduction ratio result"
    else:
        value = improvement_ratio(args.new, args.baseline)
        record = {"mode": "improvement", "ratio_pct": value}
        title = "Improvement ratio result"
    emit_record(title, record, args.output)
    return 0


def _run_dimensional(args: argparse.Namespace) -> int:
    record: dict[str, object] = {}
    if args.diffusion_unit:
        ok, message = check_diffusion_unit(args.diffusion_unit)
        record["diffusion_unit_valid"] = ok
        record["diffusion_unit_message"] = message
    if args.potential_unit:
        ok, message = check_potential_unit(args.potential_unit)
        record["potential_unit_valid"] = ok
        record["potential_unit_message"] = message
    p_args = (args.power_density, args.current_density, args.voltage)
    if any(value is not None for value in p_args):
        if not all(value is not None for value in p_args):
            raise SystemExit("--power-density, --current-density, and --voltage must be provided together.")
        ok, calculated, diff = check_current_density_power_density_relation(
            args.power_density,
            args.current_density,
            args.voltage,
            args.tolerance_pct,
        )
        record["calculated_power_density"] = calculated
        record["difference_pct"] = diff
        record["relation_consistent"] = ok
    if not record:
        record["checks_run"] = 0
    emit_record("Dimensional consistency result", record, args.output)
    return 0


def _run_resistance_sum(args: argparse.Namespace) -> int:
    result = check_component_sum(args.reported_total, args.components, args.tolerance_pct)
    record = {
        "reported_total": result.reported_total,
        "component_sum": result.component_sum,
        "absolute_difference": result.absolute_difference,
        "relative_difference_pct": result.relative_difference_pct,
        "within_tolerance": result.within_tolerance,
    }
    emit_record("Resistance component-sum result", record, args.output)
    return 0


def _run_faradaic_efficiency(args: argparse.Namespace) -> int:
    if args.current_a is not None:
        current_a = args.current_a
    else:
        if args.area_cm2 is None:
            raise SystemExit("--area-cm2 is required when using --current-density-a-cm2.")
        current_a = args.current_density_a_cm2 * args.area_cm2

    result = calculate_faradaic_efficiency(
        current_a=current_a,
        measured_flow_ml_min=args.measured_flow_ml_min,
        electrons_per_molecule=args.electrons_per_molecule,
        molar_volume_ml_per_mol=args.molar_volume_ml_mol,
        reported_fe_pct=args.reported_fe_pct,
        tolerance_pct_points=args.tolerance_pct_points,
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
    emit_record("Faradaic efficiency result", record, args.output)
    return 0


def _run_conductivity_geometry(args: argparse.Namespace) -> int:
    thickness_cm = args.thickness_cm if args.thickness_cm is not None else args.thickness_mm / 10.0
    if args.area_cm2 is not None:
        area_cm2 = args.area_cm2
    else:
        diameter_cm = args.diameter_mm / 10.0
        area_cm2 = math.pi * (diameter_cm / 2.0) ** 2

    result = calculate_conductivity_from_geometry(
        resistance_ohm=args.resistance_ohm,
        thickness_cm=thickness_cm,
        area_cm2=area_cm2,
        reported_conductivity_s_cm=args.reported_conductivity_s_cm,
        tolerance_pct=args.tolerance_pct,
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
    emit_record("Conductivity geometry result", record, args.output)
    return 0


def _run_tolerance_report(args: argparse.Namespace) -> int:
    report = build_tolerance_report_from_csv(
        csv_path=args.csv,
        reported_column=args.reported_column,
        reference_column=args.reference_column,
        id_column=args.id_column,
        tolerance_pct=args.tolerance_pct,
    )
    summary = {
        "total_rows": report.total_rows,
        "pass_count": report.pass_count,
        "fail_count": report.fail_count,
        "tolerance_pct": report.tolerance_pct,
    }
    rows = [
        {
            "row_id": row.row_id,
            "reported": row.reported_value,
            "reference": row.reference_value,
            "abs_diff": row.absolute_difference,
            "rel_diff_pct": row.relative_difference_pct,
            "pass": row.within_tolerance,
        }
        for row in report.rows
    ]
    emit_table("Tolerance report", summary, rows, args.output)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except (ValueError, ZeroDivisionError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
