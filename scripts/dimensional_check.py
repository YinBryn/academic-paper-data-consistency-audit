#!/usr/bin/env python3
"""Dimensional and physics-consistency checks."""

from __future__ import annotations

import argparse
import re


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


def check_current_density_power_density_relation(power_density: float, current_density: float, voltage: float, tolerance_pct: float = 1.0) -> tuple[bool, float, float]:
    """Check P = j*V for W/cm^2, A/cm^2, and V."""
    calculated = current_density * voltage
    diff_pct = 0.0 if calculated == 0 and power_density == 0 else (float("inf") if calculated == 0 else abs(power_density - calculated) / abs(calculated) * 100.0)
    return diff_pct <= tolerance_pct, calculated, diff_pct


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run simple dimensional and P=jV checks.")
    parser.add_argument("--diffusion-unit", type=str, help="Check diffusion unit, e.g. 'cm^2/s'.")
    parser.add_argument("--potential-unit", type=str, help="Check potential unit, e.g. 'V' or 'eV'.")
    parser.add_argument("--power-density", type=float, help="Reported power density in W/cm^2.")
    parser.add_argument("--current-density", type=float, help="Current density in A/cm^2.")
    parser.add_argument("--voltage", type=float, help="Cell voltage in V.")
    parser.add_argument("--tolerance-pct", type=float, default=1.0, help="Tolerance in percent.")
    return parser


def main() -> None:
    args = _build_parser().parse_args()
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
        ok, calculated, diff = check_current_density_power_density_relation(args.power_density, args.current_density, args.voltage, args.tolerance_pct)
        print(f"calculated_power_density: {calculated:.6f}")
        print(f"difference_pct: {diff:.6f}")
        print(f"relation_consistent: {ok}")


if __name__ == "__main__":
    main()
