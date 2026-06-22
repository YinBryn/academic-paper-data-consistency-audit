import pytest

from paper_audit.tolerance_report import build_tolerance_report, format_tolerance_report


def test_tolerance_report_counts_pass_and_fail():
    report = build_tolerance_report(
        records=[
            {"sample": "A", "reported": "1.02", "source": "1.00"},
            {"sample": "B", "reported": "1.30", "source": "1.00"},
        ],
        reported_column="reported",
        reference_column="source",
        id_column="sample",
        tolerance_pct=5.0,
    )
    assert report.total_rows == 2
    assert report.pass_count == 1
    assert report.fail_count == 1
    assert report.rows[0].within_tolerance is True
    assert report.rows[1].within_tolerance is False


def test_tolerance_report_format_contains_summary_and_rows():
    report = build_tolerance_report(
        records=[{"sample": "A", "reported": "1.02", "source": "1.00"}],
        reported_column="reported",
        reference_column="source",
        id_column="sample",
        tolerance_pct=5.0,
    )
    text = format_tolerance_report(report)
    assert "Tolerance report" in text
    assert "pass_count: 1" in text
    assert "| A | 1.02 | 1 | 0.02 | 2.000000 | True |" in text


def test_tolerance_report_missing_column_raises():
    with pytest.raises(ValueError, match="Missing reference column"):
        build_tolerance_report(
            records=[{"reported": "1.02"}],
            reported_column="reported",
            reference_column="source",
        )
