"""Reusable technical consistency checks for the paper-audit CLI."""

from __future__ import annotations

import math
import re
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


@dataclass(frozen=True)
class StatisticsResult:
    n: int
    mean: float
    sample_std: float | None
    population_std: float


def _as_float_list(values: Iterable[float], minimum: int = 1) -> list[float]:
    parsed = [float(v) for v in values]
    if len(parsed) < minimum:
        raise ValueError(f"At least {minimum} value(s) are required.")
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
    temp_c = _as_float_list(temperature_c, minimum=2)
    r_values = _as_float_list(resistance, minimum=2)
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


def calculate_statistics(values: Iterable[float]) -> StatisticsResult:
    """Return mean, sample standard deviation, and population standard deviation."""
    data = _as_float_list(values, minimum=1)
    n = len(data)
    mean = sum(data) / n
    population_std = math.sqrt(sum((x - mean) ** 2 for x in data) / n)
    sample_std = math.sqrt(sum((x - mean) ** 2 for x in data) / (n - 1)) if n > 1 else None
    return StatisticsResult(n=n, mean=mean, sample_std=sample_std, population_std=population_std)


def relative_difference_pct(reported: float | None, calculated: float | None) -> float | None:
    """Return absolute relative difference in percent."""
    if reported is None or calculated is None:
        return None
    if calculated == 0:
        return 0.0 if reported == 0 else math.inf
    return abs(reported - calculated) / abs(calculated) * 100.0


def improvement_ratio(new: float, baseline: float) -> float:
    """Return percentage change from baseline to new."""
    if baseline == 0:
        raise ZeroDivisionError("baseline cannot be zero.")
    return (new - baseline) / baseline * 100.0


def reduction_ratio(new: float, baseline: float) -> float:
    """Return percentage reduction from baseline to new."""
    if baseline == 0:
        raise ZeroDivisionError("baseline cannot be zero.")
    return (baseline - new) / baseline * 100.0


def _normalize_unit(unit: str) -> str:
    return unit.strip().replace(" ", "").replace("·", "").replace("*", "").replace("²", "2").replace("^", "").replace("⁻¹", "-1").lower()


def check_diffusion_unit(unit: str) -> tuple[bool, str]:
    """Check whether a diffusion coefficient unit has length^2/time dimensions."""
    normalized = _normalize_unit(unit)
    valid_patterns = {"cm2/s", "m2/s", "a2/ps", "ang2/ps", "cm2s-1", "m2s-1", "a2ps-1", "å2ps-1"}
    if normalized in valid_patterns:
        return True, unit
    velocity_like = bool(re.fullmatch(r"(cm|m|a|ang|å)/(s|ps)", normalized))
    if velocity_like or normalized in {"cms-1", "ms-1", "aps-1", "angps-1"}:
        return False, "Diffusion coefficients should use length^2/time, e.g. cm^2/s or A^2/ps."
    return False, "Expected length^2/time, e.g. cm^2/s, m^2/s, or A^2/ps."


def check_potential_unit(unit: str) -> tuple[bool, str]:
    """Check whether a potential unit is V or mV rather than an energy unit."""
    normalized = _normalize_unit(unit)
    if normalized in {"v", "mv"}:
        return True, unit
    if normalized == "ev":
        return False, "Potential difference should be reported in V or mV; eV is an energy unit."
    return False, "Expected V or mV."


def check_current_density_power_density_relation(
    power_density: float,
    current_density: float,
    voltage: float,
    tolerance_pct: float = 1.0,
) -> tuple[bool, float, float]:
    """Check P = j*V for W/cm^2, A/cm^2, and V."""
    calculated = current_density * voltage
    if calculated == 0 and power_density == 0:
        diff_pct = 0.0
    elif calculated == 0:
        diff_pct = math.inf
    else:
        diff_pct = abs(power_density - calculated) / abs(calculated) * 100.0
    return diff_pct <= tolerance_pct, calculated, diff_pct
