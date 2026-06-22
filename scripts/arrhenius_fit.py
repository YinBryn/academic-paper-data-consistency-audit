#!/usr/bin/env python3
"""Arrhenius fitting helper for resistance or ASR data."""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Iterable, Sequence

KB_EV_PER_K = 8.617333262145e-5


@dataclass(frozen=True)
class ArrheniusResult:
    temperature_k: list[float]
    x_1000_over_t: list[float]
    y: list[float]
    slope: float
    intercept: float
    r_squared: float
    ea_ev: float


def _as_float_list(values: Iterable[float]) -> list[float]:
    parsed = [float(v) for v in values]
    if len(parsed) < 2:
        raise ValueError("At least two data points are required.")
    return parsed


def linear_regression(x: Sequence[float], y: Sequence[float]) -> tuple[float, float, float]:
    """Return slope, intercept, and R2 for y = slope*x + intercept."""
    if len(x) != len(y):
        raise ValueError("x and y must have the same length.")
    if len(x) < 2:
        raise ValueError("At least two points are required.")

    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    ss_xx = sum((xi - mean_x) ** 2 for xi in x)
    if ss_xx == 0:
        raise ValueError("Cannot fit data with identical x values.")
    ss_xy = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    slope = ss_xy / ss_xx
    intercept = mean_y - slope * mean_x
    ss_tot = sum((yi - mean_y) ** 2 for yi in y)
    ss_res = sum((yi - (slope * xi + intercept)) ** 2 for xi, yi in zip(x, y))
    r_squared = 1.0 if ss_tot == 0 else 1.0 - ss_res / ss_tot
    return slope, intercept, r_squared


def arrhenius_fit(
    temperature_c: Iterable[float],
    resistance: Iterable[float],
    use_rt_correction: bool = False,
) -> ArrheniusResult:
    """Fit resistance data and return activation energy in eV."""
    temp_c = _as_float_list(temperature_c)
    r_values = _as_float_list(resistance)
    if len(temp_c) != len(r_values):
        raise ValueError("temperature_c and resistance must have the same length.")
    if any(r <= 0 for r in r_values):
        raise ValueError("All resistance values must be positive.")

    temp_k = [t + 273.15 for t in temp_c]
    x = [1000.0 / t for t in temp_k]
    y = [math.log(r * t) for r, t in zip(r_values, temp_k)] if use_rt_correction else [math.log(r) for r in r_values]
    slope, intercept, r_squared = linear_regression(x, y)
    ea_ev = slope * 1000.0 * KB_EV_PER_K
    return ArrheniusResult(temp_k, x, y, slope, intercept, r_squared, ea_ev)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Fit Arrhenius resistance/ASR data and report Ea in eV.")
    parser.add_argument("--temperature-c", nargs="+", type=float, required=True, help="Temperatures in Celsius.")
    parser.add_argument("--resistance", nargs="+", type=float, required=True, help="Resistance, Rp, or ASR values.")
    parser.add_argument("--use-rt-correction", action="store_true", help="Fit ln(R*T) instead of ln(R).")
    return parser


def main() -> None:
    args = _build_parser().parse_args()
    result = arrhenius_fit(args.temperature_c, args.resistance, args.use_rt_correction)
    label = "ln(R*T)" if args.use_rt_correction else "ln(R)"
    print("Arrhenius fitting result")
    print("------------------------")
    print(f"Fitted quantity: {label}")
    print(f"Slope: {result.slope:.6f}")
    print(f"Intercept: {result.intercept:.6f}")
    print(f"R^2: {result.r_squared:.6f}")
    print(f"Ea: {result.ea_ev:.6f} eV")


if __name__ == "__main__":
    main()
