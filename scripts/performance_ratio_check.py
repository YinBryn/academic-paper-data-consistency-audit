#!/usr/bin/env python3
"""Performance improvement ratio helper."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


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


def batch_comparison_from_csv(path: str | Path, new_sample: str, baseline_sample: str, column: str) -> list[dict[str, str | float]]:
    """Compare two samples by matching rows with the same temperature_C value."""
    with open(path, newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    grouped: dict[str, dict[str, float]] = {}
    for row in rows:
        condition = row.get("temperature_C") or row.get("condition") or "all"
        sample = row.get("sample", "")
        if sample:
            grouped.setdefault(str(condition), {})[sample] = float(row[column])
    output = []
    for condition, values in sorted(grouped.items()):
        if new_sample in values and baseline_sample in values:
            baseline = values[baseline_sample]
            new = values[new_sample]
            output.append({"condition": condition, "baseline": baseline, "new": new, "improvement_pct": improvement_ratio(new, baseline)})
    return output


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Calculate performance improvement ratios.")
    parser.add_argument("--new", type=float, help="New or modified value.")
    parser.add_argument("--baseline", type=float, help="Baseline value.")
    parser.add_argument("--csv", type=str, help="Optional CSV file for batch comparison.")
    parser.add_argument("--new-sample", type=str, help="Sample name for the new/modified case.")
    parser.add_argument("--baseline-sample", type=str, help="Sample name for the baseline case.")
    parser.add_argument("--column", type=str, help="CSV column to compare.")
    return parser


def main() -> None:
    args = _build_parser().parse_args()
    if args.csv:
        if not (args.new_sample and args.baseline_sample and args.column):
            raise SystemExit("--csv requires --new-sample, --baseline-sample, and --column.")
        rows = batch_comparison_from_csv(args.csv, args.new_sample, args.baseline_sample, args.column)
        print("condition,baseline,new,improvement_pct")
        for row in rows:
            print(f"{row['condition']},{row['baseline']},{row['new']},{row['improvement_pct']:.6f}")
        return
    if args.new is None or args.baseline is None:
        raise SystemExit("Provide --new and --baseline, or use --csv mode.")
    print(f"Improvement ratio: {improvement_ratio(args.new, args.baseline):.6f}%")


if __name__ == "__main__":
    main()
