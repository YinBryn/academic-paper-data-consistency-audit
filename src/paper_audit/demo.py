"""One-command synthetic demonstration workflow for the paper-audit CLI."""

from __future__ import annotations

import math
from dataclasses import dataclass

from .checks import (
    arrhenius_fit,
    calculate_conductivity_from_geometry,
    calculate_faradaic_efficiency,
    calculate_statistics,
    check_component_sum,
    check_current_density_power_density_relation,
)
from .tolerance_report import build_tolerance_report


@dataclass(frozen=True)
class DemoStep:
    """A completed synthetic demo step."""

    name: str
    detail: str


def build_demo_steps() -> list[DemoStep]:
    """Run representative checks on synthetic data and return compact step summaries."""
    steps: list[DemoStep] = []

    arrhenius = arrhenius_fit(
        temperature_c=[800.0, 750.0, 700.0],
        resistance=[0.022, 0.053, 0.103],
    )
    steps.append(
        DemoStep(
            name="Arrhenius recalculation",
            detail=f"Ea={arrhenius.ea_ev:.4f} eV, R^2={arrhenius.r_squared:.4f}",
        )
    )

    statistics = calculate_statistics([4.65, 4.83, 4.84, 4.76, 4.77])
    steps.append(
        DemoStep(
            name="Statistics recalculation",
            detail=f"n={statistics.n}, mean={statistics.mean:.4f}, sample_std={statistics.sample_std:.4f}",
        )
    )

    ivp_ok, calculated_power, ivp_diff = check_current_density_power_density_relation(
        power_density=2.60,
        current_density=2.00,
        voltage=1.30,
        tolerance_pct=1.0,
    )
    steps.append(
        DemoStep(
            name="I-V-P dimensional check",
            detail=f"calculated_power_density={calculated_power:.4f} W/cm^2, difference={ivp_diff:.4f}%, within_tolerance={ivp_ok}",
        )
    )

    component_sum = check_component_sum(
        reported_total=0.151,
        components=[0.052, 0.061, 0.038],
        tolerance_pct=1.0,
    )
    steps.append(
        DemoStep(
            name="Resistance component-sum check",
            detail=f"component_sum={component_sum.component_sum:.4f}, difference={component_sum.relative_difference_pct:.4f}%, within_tolerance={component_sum.within_tolerance}",
        )
    )

    faradaic = calculate_faradaic_efficiency(
        current_a=0.50,
        measured_flow_ml_min=3.30,
        electrons_per_molecule=2,
        reported_fe_pct=95.0,
        tolerance_pct_points=5.0,
    )
    steps.append(
        DemoStep(
            name="Faradaic efficiency check",
            detail=f"calculated_FE={faradaic.calculated_fe_pct:.2f}%, reported_FE={faradaic.reported_fe_pct:.2f}%, within_tolerance={faradaic.within_tolerance}",
        )
    )

    diameter_cm = 6.0 / 10.0
    area_cm2 = math.pi * (diameter_cm / 2.0) ** 2
    conductivity = calculate_conductivity_from_geometry(
        resistance_ohm=10.0,
        thickness_cm=0.33 / 10.0,
        area_cm2=area_cm2,
        reported_conductivity_s_cm=0.01167,
        tolerance_pct=5.0,
    )
    steps.append(
        DemoStep(
            name="Conductivity geometry check",
            detail=f"calculated_sigma={conductivity.calculated_conductivity_s_cm:.6f} S/cm, within_tolerance={conductivity.within_tolerance}",
        )
    )

    tolerance_report = build_tolerance_report(
        records=[
            {"sample": "synthetic-A", "reported_Rp": "0.101", "source_Rp": "0.100"},
            {"sample": "synthetic-B", "reported_Rp": "0.178", "source_Rp": "0.180"},
        ],
        reported_column="reported_Rp",
        reference_column="source_Rp",
        id_column="sample",
        tolerance_pct=5.0,
    )
    steps.append(
        DemoStep(
            name="Batch tolerance report",
            detail=f"rows={tolerance_report.total_rows}, pass={tolerance_report.pass_count}, fail={tolerance_report.fail_count}",
        )
    )

    return steps


def build_demo_report() -> str:
    """Return a human-readable synthetic demo report."""
    steps = build_demo_steps()
    lines = [
        "Academic Paper Data Consistency Audit Demo",
        "===========================================",
        "Synthetic data only. No real article data is used.",
        "",
    ]
    lines.extend(f"[PASS] {step.name} - {step.detail}" for step in steps)
    lines.extend(
        [
            "",
            f"Demo completed: {len(steps)} synthetic checks passed.",
            "Use this command as a quick smoke test after installation.",
        ]
    )
    return "\n".join(lines)


def run_demo() -> int:
    """Print the synthetic demo report and return a process-style exit code."""
    print(build_demo_report())
    return 0
