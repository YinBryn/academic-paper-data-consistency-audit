"""Batch tolerance reports for reported values versus reference/source-data values."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class ToleranceReportRow:
    row_id: str
    reported_value: float
    reference_value: float
    absolute_difference: float
    relative_difference_pct: float
    tolerance_pct: float
    within_tolerance: bool


@dataclass(frozen=True)
class ToleranceReport:
    rows: list[ToleranceReportRow]
    total_rows: int
    pass_count: int
    fail_count: int
    tolerance_pct: float


def _relative_difference_pct(reported: float, reference: float) -> float:
    if reference == 0:
        return 0.0 if reported == 0 else float("inf")
    return abs(reported - reference) / abs(reference) * 100.0


def build_tolerance_report(
    records: Iterable[dict[str, str]],
    reported_column: str,
    reference_column: str,
    id_column: str | None = None,
    tolerance_pct: float = 5.0,
) -> ToleranceReport:
    """Build a tolerance report from row dictionaries."""
    if tolerance_pct < 0:
        raise ValueError("tolerance_pct must be non-negative.")

    rows: list[ToleranceReportRow] = []
    for index, record in enumerate(records, start=1):
        if reported_column not in record:
            raise ValueError(f"Missing reported column: {reported_column}")
        if reference_column not in record:
            raise ValueError(f"Missing reference column: {reference_column}")
        row_id = record.get(id_column, str(index)) if id_column else str(index)
        reported = float(record[reported_column])
        reference = float(record[reference_column])
        absolute_difference = reported - reference
        relative_pct = _relative_difference_pct(reported, reference)
        rows.append(
            ToleranceReportRow(
                row_id=row_id,
                reported_value=reported,
                reference_value=reference,
                absolute_difference=absolute_difference,
                relative_difference_pct=relative_pct,
                tolerance_pct=tolerance_pct,
                within_tolerance=relative_pct <= tolerance_pct,
            )
        )

    pass_count = sum(1 for row in rows if row.within_tolerance)
    fail_count = len(rows) - pass_count
    return ToleranceReport(
        rows=rows,
        total_rows=len(rows),
        pass_count=pass_count,
        fail_count=fail_count,
        tolerance_pct=tolerance_pct,
    )


def build_tolerance_report_from_csv(
    csv_path: str | Path,
    reported_column: str,
    reference_column: str,
    id_column: str | None = None,
    tolerance_pct: float = 5.0,
) -> ToleranceReport:
    """Build a tolerance report from a CSV file."""
    with Path(csv_path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError("CSV file must include a header row.")
        return build_tolerance_report(
            records=reader,
            reported_column=reported_column,
            reference_column=reference_column,
            id_column=id_column,
            tolerance_pct=tolerance_pct,
        )


def format_tolerance_report(report: ToleranceReport) -> str:
    """Format a tolerance report as a compact Markdown-style table."""
    lines = [
        "Tolerance report",
        "----------------",
        f"total_rows: {report.total_rows}",
        f"pass_count: {report.pass_count}",
        f"fail_count: {report.fail_count}",
        f"tolerance_pct: {report.tolerance_pct:.6f}",
        "",
        "| row_id | reported | reference | abs_diff | rel_diff_pct | pass |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for row in report.rows:
        rel = "inf" if row.relative_difference_pct == float("inf") else f"{row.relative_difference_pct:.6f}"
        lines.append(
            f"| {row.row_id} | {row.reported_value:.8g} | {row.reference_value:.8g} | "
            f"{row.absolute_difference:.8g} | {rel} | {row.within_tolerance} |"
        )
    return "\n".join(lines)
