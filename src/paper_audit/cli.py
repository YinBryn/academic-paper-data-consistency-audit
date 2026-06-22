"""Command-line interface for Academic Paper Data Consistency Audit."""

from __future__ import annotations

import argparse
import sys

from .checks import (
    arrhenius_fit,
    calculate_statistics,
    check_component_sum,
    check_current_density_power_density_relation,
    check_diffusion_unit,
    check_potential_unit,
    improvement_ratio,
    reduction_ratio,
    relative_difference_pct,
)


def _add_arrhenius_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("arrhenius", help="Fit Arrhenius resistance/ASR data and report Ea.")
    parser.add_argument("--temperature-c", nargs="+", type=float, required=True, help="Temperatures in Celsius.")
    parser.add_argument("--resistance", nargs="+", type=float, required=True, help="Resistance, Rp, or ASR values.")
    parser.add_argument("--use-rt-correction", action="store_true", help="Fit ln(R*T) instead of ln(R).")
    parser.set_defaults(func=_run_arrhenius)


def _add_statistics_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("statistics", help="Recalculate mean/std from replicate values.")
    parser.add_argument("--values", nargs="+", type=float, required=True, help="Replicate values.")
    parser.add_argument("--reported-mean", type=float, help="Optional reported mean value.")
    parser.add_argument("--reported-std", type=float, help="Optional reported standard deviation.")
    parser.add_argument("--population-std", action="store_true", help="Compare against population std instead of sample std.")
    parser.add_argument("--tolerance-pct", type=float, default=1.0, help="Tolerance in percent.")
    parser.set_defaults(func=_run_statistics)


def _add_ratio_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("ratio", help="Calculate improvement or reduction ratios.")
    parser.add_argument("--new", type=float, required=True, help="New or modified value.")
    parser.add_argument("--baseline", type=float, required=True, help="Baseline value.")
    parser.add_argument("--mode", choices=["improvement", "reduction"], default="improvement", help="Ratio convention to report.")
    parser.set_defaults(func=_run_ratio)


def _add_dimensional_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("dimensional", help="Run dimensional and I-V-P checks.")
    parser.add_argument("--diffusion-unit", type=str, help="Check diffusion unit, e.g. 'cm^2/s'.")
    parser.add_argument("--potential-unit", type=str, help="Check potential unit, e.g. 'V' or 'eV'.")
    parser.add_argument("--power-density", type=float, help="Reported power density in W/cm^2.")
    parser.add_argument("--current-density", type=float, help="Current density in A/cm^2.")
    parser.add_argument("--voltage", type=float, help="Cell voltage in V.")
    parser.add_argument("--tolerance-pct", type=float, default=1.0, help="Tolerance in percent.")
    parser.set_defaults(func=_run_dimensional)


def _add_resistance_sum_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser(
        "resistance-sum",
        help="Check whether reported total Rp/ASR equals the sum of listed components.",
    )
    parser.add_argument("--reported-total", type=float, required=True, help="Reported total resistance, Rp, or ASR value.")
    parser.add_argument("--components", nargs="+", type=float, required=True, help="Listed component resistances to sum.")
    parser.add_argument("--tolerance-pct", type=float, default=1.0, help="Tolerance in percent relative to the component sum.")
    parser.set_defaults(func=_run_resistance_sum)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="paper-audit",
        description="Physics-informed data consistency checks for materials electrochemistry papers.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    _add_arrhenius_parser(subparsers)
    _add_statistics_parser(subparsers)
    _add_ratio_parser(subparsers)
    _add_dimensional_parser(subparsers)
    _add_resistance_sum_parser(subparsers)
    return parser


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
