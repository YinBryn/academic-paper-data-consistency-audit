#!/usr/bin/env python3
"""Statistics consistency helper for replicate source data."""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class StatisticsResult:
    n: int
    mean: float
    sample_std: float | None
    population_std: float


def _values(values: Iterable[float]) -> list[float]:
    parsed = [float(v) for v in values]
    if not parsed:
        raise ValueError("At least one value is required.")
    return parsed


def calculate_statistics(values: Iterable[float]) -> StatisticsResult:
    """Return mean, sample standard deviation, and population standard deviation."""
    data = _values(values)
    n = len(data)
    mean = sum(data) / n
    population_std = math.sqrt(sum((x - mean) ** 2 for x in data) / n)
    sample_std = math.sqrt(sum((x - mean) ** 2 for x in data) / (n - 1)) if n > 1 else None
    return StatisticsResult(n=n, mean=mean, sample_std=sample_std, population_std=population_std)


def compare_reported_value(
    reported_mean: float,
    reported_std: float | None,
    values: Iterable[float],
    tolerance_pct: float = 1.0,
    use_sample_std: bool = True,
) -> dict[str, float | bool | None]:
    """Compare reported mean/std with recalculated statistics."""
    stats = calculate_statistics(values)
    target_std = stats.sample_std if use_sample_std else stats.population_std

    def rel_diff(reported: float | None, calculated: float | None) -> float | None:
        if reported is None or calculated is None:
            return None
        if calculated == 0:
            return 0.0 if reported == 0 else math.inf
        return abs(reported - calculated) / abs(calculated) * 100.0

    mean_diff = rel_diff(reported_mean, stats.mean)
    std_diff = rel_diff(reported_std, target_std)
    return {
        "n": stats.n,
        "calculated_mean": stats.mean,
        "calculated_std": target_std,
        "mean_relative_difference_pct": mean_diff,
        "std_relative_difference_pct": std_diff,
        "mean_within_tolerance": mean_diff is not None and mean_diff <= tolerance_pct,
        "std_within_tolerance": None if std_diff is None else std_diff <= tolerance_pct,
    }


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Recalculate mean/std from replicate values and compare reported values.")
    parser.add_argument("--values", nargs="+", type=float, required=True, help="Replicate values.")
    parser.add_argument("--reported-mean", type=float, help="Reported mean value.")
    parser.add_argument("--reported-std", type=float, help="Reported standard deviation.")
    parser.add_argument("--population-std", action="store_true", help="Compare against population std instead of sample std.")
    parser.add_argument("--tolerance-pct", type=float, default=1.0, help="Tolerance in percent.")
    return parser


def main() -> None:
    args = _build_parser().parse_args()
    result = calculate_statistics(args.values)
    print("Statistics check")
    print("----------------")
    print(f"n: {result.n}")
    print(f"mean: {result.mean:.6f}")
    print(f"sample_std: {result.sample_std if result.sample_std is not None else 'NA'}")
    print(f"population_std: {result.population_std:.6f}")
    if args.reported_mean is not None:
        comparison = compare_reported_value(args.reported_mean, args.reported_std, args.values, args.tolerance_pct, not args.population_std)
        print("Comparison:")
        for key, value in comparison.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
