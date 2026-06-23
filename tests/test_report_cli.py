import json

from paper_audit.cli import main
from paper_audit.report import build_report_from_json, format_report_markdown


def test_build_report_from_json_example() -> None:
    report = build_report_from_json("examples/report_config.json")

    assert report["title"] == "Synthetic Audit Report"
    assert report["summary"]["checks_run"] == 5
    assert len(report["checks"]) == 5
    assert {check["status"] for check in report["checks"]} <= {"PASS", "FLAG", "INFO"}


def test_format_report_markdown() -> None:
    report = build_report_from_json("examples/report_config.json")
    markdown = format_report_markdown(report)

    assert markdown.startswith("# Synthetic Audit Report")
    assert "## Summary" in markdown
    assert "## Check 1: I-V-P consistency" in markdown
    assert "| field | value |" in markdown


def test_cli_report_markdown(capsys) -> None:
    exit_code = main(["report", "--config", "examples/report_config.json"])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "# Synthetic Audit Report" in captured.out
    assert "## Check 1: I-V-P consistency" in captured.out


def test_cli_report_json(capsys) -> None:
    exit_code = main(["report", "--config", "examples/report_config.json", "--output", "json"])
    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["title"] == "Synthetic Audit Report"
    assert payload["summary"]["checks_run"] == len(payload["checks"])
