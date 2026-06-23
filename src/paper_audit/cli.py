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
from .tolerance_report import build_tolerance_report_from_csv, format_tolerance_report


def _add_demo_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("demo", help="Run a synthetic smoke-test demo.")
    parser.set_defaults(func=_run_demo)


def _add_arrhenius_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("arrhenius", help="Fit Arrhenius values and report Ea.")
    parser.add_argument("--temperature-c", nargs="+", type=float, required=True)
    parser.add_argument("--resistance", nargs="+", type=float, required=True)
    parser.add_argument("--use-rt-correction", action="store_true")
    parser.set_defaults(func=_run_arrhenius)


def _add_statistics_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("statistics", help="Recalculate mean/std.")
    parser.add_argument("--values", nargs="+", type=float, required=True)
    parser.add_argument("--reported-mean", type=float)
    parser.add_argument("--reported-std", type=float)
    parser.add_argument("--population-std", action="store_true")
    parser.add_argument("--tolerance-pct", type=float, default=1.0)
    parser.set_defaults(func=_run_statistics)


def _add_ratio_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("ratio", help="Calculate improvement or reduction ratios.")
    parser.add_argument("--new", type=float, required=True)
    parser.add_argument("--baseline", type=float, required=True)
    parser.add_argument("--mode", choices=["improvement", "reduction"], default="improvement")
    parser.set_defaults(func=_run_ratio)


def _add_dimensional_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("dimensional", help="Run unit and P=jV checks.")
    parser.add_argument("--diffusion-unit", type=str)
    parser.add_argument("--potential-unit", type=str)
    parser.add_argument("--power-density", type=float)
    parser.add_argument("--current-density", type=float)
    parser.add_argument("--voltage", type=float)
    parser.add_argument("--tolerance-pct", type=float, default=1.0)
    parser.set_defaults(func=_run_dimensional)


def _add_resistance_sum_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("resistance-sum", help="Check a total against listed components.")
    parser.add_argument("--reported-total", type=float, required=True)
    parser.add_argument("--components", nargs="+", type=float, required=True)
    parser.add_argument("--tolerance-pct", type=float, default=1.0)
    parser.set_defaults(func=_run_resistance_sum)


def _add_faradaic_efficiency_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("faradaic-efficiency", help="Calculate efficiency from current and flow.")
    current_group = parser.add_mutually_exclusive_group(required=True)
    current_group.add_argument("--current-a", type=float)
    current_group.add_argument("--current-density-a-cm2", type=float)
    parser.add_argument("--area-cm2", type=float)
    parser.add_argument("--measured-flow-ml-min", type=float, required=True)
    parser.add_argument("--electrons-per-molecule", type=float, required=True)
    parser.add_argument("--reported-fe-pct", type=float)
    parser.add_argument("--tolerance-pct-points", type=float, default=5.0)
    parser.add_argument("--molar-volume-ml-mol", type=float, default=DEFAULT_MOLAR_VOLUME_ML_PER_MOL)
    parser.set_defaults(func=_run_faradaic_efficiency)


def _add_conductivity_geometry_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("conductivity-geometry", help="Calculate conductivity from geometry.")
    parser.add_argument("--resistance-ohm", type=float, required=True)
    thickness_group = parser.add_mutually_exclusive_group(required=True)
    thickness_group.add_argument("--thickness-cm", type=float)
    thickness_group.add_argument("--thickness-mm", type=float)
    area_group = parser.add_mutually_exclusive_group(required=True)
    area_group.add_argument("--area-cm2", type=float)
    area_group.add_argument("--diameter-mm", type=float)
    parser.add_argument("--reported-conductivity-s-cm", type=float)
    parser.add_argument("--tolerance-pct", type=float, default=5.0)
    parser.set_defaults(func=_run_conductivity_geometry)


def _add_tolerance_report_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("tolerance-report", help="Compare two numeric CSV columns.")
    parser.add_argument("--csv", required=True)
    parser.add_argument("--reported-column", required=True)
    parser.add_argument("--reference-column", required=True)
    parser.add_argument("--id-column")
    parser.add_argument("--tolerance-pct", type=float, default=5.0)
    parser.set_defaults(func=_run_tolerance_report)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="paper-audit",
        description="Technical consistency checks for materials electrochemistry.",
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
    label = "ln(R*T)" if args.use_rt_correction else "ln(R)"
    print("Arrhenius fitting result")
    print("------------------------")
    print(f"Fitted quantity: {label}")
    print(f"Slope: {result.slope:.6f}")
    print(f"Intercept: {result.intercept:.6f}")
    print(f"R^2: {result.r_squared:.6f}")
    print(f"Ea: {result.ea_ev:.6f} eV")
    return 0


def _run_statistics(args: argparse.Namespace) -> int:
    stats = calculate_statistics(args.values)
    target_std = stats.population_std if args.population_std else stats.sample_std
    print("Statistics recalculation result")
    print("-------------------------------")
    print(f"n: {stats.n}")
    print(f"mean: {stats.mean:.6f}")
    if stats.sample_std is None:
        print("sample_std: n/a")
    else:
        print(f"sample_std: {stats.sample_std:.6f}")
    print(f"population_std: {stats.population_std:.6f}")

    if args.reported_mean is not None:
        mean_diff = relative_difference_pct(args.reported_mean, stats.mean)
        print(f"reported_mean_difference_pct: {mean_diff:.6f}")
        print(f"reported_mean_within_tolerance: {mean_diff <= args.tolerance_pct}")
    if args.reported_std is not None:
        std_diff = relative_difference_pct(args.reported_std, target_std)
        if std_diff is None:
            print("reported_std_difference_pct: n/a")
            print("reported_std_within_tolerance: n/a")
        else:
            print(f"reported_std_difference_pct: {std_diff:.6f}")
            print(f"reported_std_within_tolerance: {std_diff <= args.tolerance_pct}")
    return 0


def _run_ratio(args: argparse.Namespace) -> int:
    if args.mode == "reduction":
        value = reduction_ratio(args.new, args.baseline)
        print(f"Reduction ratio: {value:.6f}%")
    else:
        value = improvement_ratio(args.new, args.baseline)
        print(f"Improvement ratio: {value:.6f}%")
    return 0


def _run_dimensional(args: argparse.Namespace) -> int:
    if args.diffusion_unit:
        ok, message = check_diffusion_unit(args.diffusion_unit)
        print(f"diffusion_unit_valid: {ok}")
        print(f"message: {message}")
    if args.potential_unit:
        ok, message = check_potential_unit(args.potential_unit)
        print(f"potential_unit_valid: {ok}")
        print(f"message: {message}")
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
        print(f"calculated_power_density: {calculated:.6f}")
        print(f"difference_pct: {diff:.6f}")
        print(f"relation_consistent: {ok}")
    return 0


def _run_resistance_sum(args: argparse.Namespace) -> int:
    result = check_component_sum(args.reported_total, args.components, args.tolerance_pct)
    print("Resistance component-sum result")
    print("-------------------------------")
    print(f"reported_total: {result.reported_total:.6f}")
    print(f"component_sum: {result.component_sum:.6f}")
    print(f"absolute_difference: {result.absolute_difference:.6f}")
    print(f"relative_difference_pct: {result.relative_difference_pct:.6f}")
    print(f"within_tolerance: {result.within_tolerance}")
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
    print("Faradaic efficiency result")
    print("--------------------------")
    print(f"current_a: {result.current_a:.6f}")
    print(f"electrons_per_molecule: {result.electrons_per_molecule:.6f}")
    print(f"theoretical_flow_100pct_ml_min: {result.theoretical_flow_100pct_ml_min:.6f}")
    print(f"measured_flow_ml_min: {result.measured_flow_ml_min:.6f}")
    print(f"calculated_fe_pct: {result.calculated_fe_pct:.6f}")
    if result.reported_fe_pct is not None:
        print(f"reported_fe_pct: {result.reported_fe_pct:.6f}")
        print(f"fe_difference_pct_points: {result.fe_difference_pct_points:.6f}")
        print(f"within_tolerance: {result.within_tolerance}")
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
    print("Conductivity geometry result")
    print("----------------------------")
    print(f"resistance_ohm: {result.resistance_ohm:.6f}")
    print(f"thickness_cm: {result.thickness_cm:.6f}")
    print(f"area_cm2: {result.area_cm2:.6f}")
    print(f"calculated_conductivity_s_cm: {result.calculated_conductivity_s_cm:.8f}")
    if result.reported_conductivity_s_cm is not None:
        print(f"reported_conductivity_s_cm: {result.reported_conductivity_s_cm:.8f}")
        print(f"relative_difference_pct: {result.relative_difference_pct:.6f}")
        print(f"within_tolerance: {result.within_tolerance}")
    return 0


def _run_tolerance_report(args: argparse.Namespace) -> int:
    report = build_tolerance_report_from_csv(
        csv_path=args.csv,
        reported_column=args.reported_column,
        reference_column=args.reference_column,
        id_column=args.id_column,
        tolerance_pct=args.tolerance_pct,
    )
    print(format_tolerance_report(report))
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
