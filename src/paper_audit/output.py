"""Output formatting helpers for CLI commands."""

from __future__ import annotations

import csv
import json
import math
import sys
from collections.abc import Mapping, Sequence
from typing import Any

OUTPUT_FORMATS = ("text", "json", "markdown", "csv")


def normalize_value(value: Any) -> Any:
    """Return a stable scalar value for JSON/CSV/Markdown output."""
    if isinstance(value, float):
        if math.isnan(value):
            return "nan"
        if math.isinf(value):
            return "inf" if value > 0 else "-inf"
        return value
    if isinstance(value, (str, int, bool)) or value is None:
        return value
    return str(value)


def normalize_record(record: Mapping[str, Any]) -> dict[str, Any]:
    """Normalize a mapping into plain serializable scalar values."""
    return {key: normalize_value(value) for key, value in record.items()}


def format_scalar(value: Any) -> str:
    """Format a scalar value for human-readable text output."""
    value = normalize_value(value)
    if isinstance(value, float):
        return f"{value:.6f}"
    return str(value)


def emit_record(title: str, record: Mapping[str, Any], output: str = "text") -> None:
    """Print a single-record result in text, JSON, Markdown, or CSV format."""
    normalized = normalize_record(record)
    if output == "json":
        print(json.dumps(normalized, indent=2, sort_keys=True))
        return
    if output == "csv":
        writer = csv.DictWriter(sys.stdout, fieldnames=list(normalized.keys()))
        writer.writeheader()
        writer.writerow(normalized)
        return
    if output == "markdown":
        print(f"## {title}")
        print()
        print("| field | value |")
        print("|---|---:|")
        for key, value in normalized.items():
            print(f"| {key} | {format_scalar(value)} |")
        return

    print(title)
    print("-" * len(title))
    for key, value in normalized.items():
        print(f"{key}: {format_scalar(value)}")


def emit_table(
    title: str,
    summary: Mapping[str, Any],
    rows: Sequence[Mapping[str, Any]],
    output: str = "text",
) -> None:
    """Print a summary plus row table in text, JSON, Markdown, or CSV format."""
    normalized_summary = normalize_record(summary)
    normalized_rows = [normalize_record(row) for row in rows]

    if output == "json":
        print(json.dumps({"summary": normalized_summary, "rows": normalized_rows}, indent=2, sort_keys=True))
        return

    if output == "csv":
        if not normalized_rows:
            emit_record(title, normalized_summary, output="csv")
            return
        writer = csv.DictWriter(sys.stdout, fieldnames=list(normalized_rows[0].keys()))
        writer.writeheader()
        writer.writerows(normalized_rows)
        return

    if output == "markdown":
        print(f"## {title}")
        print()
        for key, value in normalized_summary.items():
            print(f"- **{key}:** {format_scalar(value)}")
        if normalized_rows:
            print()
            headers = list(normalized_rows[0].keys())
            print("| " + " | ".join(headers) + " |")
            print("|" + "|".join("---" for _ in headers) + "|")
            for row in normalized_rows:
                print("| " + " | ".join(format_scalar(row.get(header, "")) for header in headers) + " |")
        return

    print(title)
    print("-" * len(title))
    for key, value in normalized_summary.items():
        print(f"{key}: {format_scalar(value)}")
    if normalized_rows:
        print()
        headers = list(normalized_rows[0].keys())
        print("\t".join(headers))
        for row in normalized_rows:
            print("\t".join(format_scalar(row.get(header, "")) for header in headers))
