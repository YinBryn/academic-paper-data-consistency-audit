import csv
import json
from io import StringIO

from paper_audit.cli import main


def test_ratio_json_output(capsys) -> None:
    exit_code = main(["ratio", "--new", "3.53", "--baseline", "2.74", "--output", "json"])
    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["mode"] == "improvement"
    assert payload["ratio_pct"] > 0


def test_resistance_sum_csv_output(capsys) -> None:
    exit_code = main([
        "resistance-sum",
        "--reported-total",
        "0.151",
        "--components",
        "0.052",
        "0.061",
        "0.038",
        "--output",
        "csv",
    ])
    captured = capsys.readouterr()
    rows = list(csv.DictReader(StringIO(captured.out)))

    assert exit_code == 0
    assert len(rows) == 1
    assert rows[0]["within_tolerance"] == "True"


def test_statistics_markdown_output(capsys) -> None:
    exit_code = main([
        "statistics",
        "--values",
        "4.65",
        "4.83",
        "4.84",
        "4.76",
        "4.77",
        "--reported-mean",
        "4.79",
        "--output",
        "markdown",
    ])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "## Statistics recalculation result" in captured.out
    assert "| field | value |" in captured.out
    assert "reported_mean_within_tolerance" in captured.out


def test_tolerance_report_json_output(capsys) -> None:
    exit_code = main([
        "tolerance-report",
        "--csv",
        "case_studies/tolerance_report/input.csv",
        "--reported-column",
        "reported_Rp_ohm_cm2",
        "--reference-column",
        "source_Rp_ohm_cm2",
        "--id-column",
        "sample",
        "--output",
        "json",
    ])
    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert "summary" in payload
    assert "rows" in payload
    assert payload["summary"]["total_rows"] == len(payload["rows"])
