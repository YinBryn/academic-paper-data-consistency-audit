from paper_audit.cli import main
from paper_audit.demo import build_demo_report, build_demo_steps


def test_demo_steps_cover_representative_checks() -> None:
    steps = build_demo_steps()
    names = [step.name for step in steps]

    assert len(steps) == 7
    assert "Arrhenius recalculation" in names
    assert "Statistics recalculation" in names
    assert "I-V-P dimensional check" in names
    assert "Resistance component-sum check" in names
    assert "Faradaic efficiency check" in names
    assert "Conductivity geometry check" in names
    assert "Batch tolerance report" in names


def test_demo_report_is_compact_and_synthetic() -> None:
    report = build_demo_report()

    assert "Academic Paper Data Consistency Audit Demo" in report
    assert "Synthetic data only" in report
    assert "[PASS] Arrhenius recalculation" in report
    assert "[PASS] Batch tolerance report" in report
    assert "Demo completed: 7 synthetic checks passed." in report


def test_cli_demo_command(capsys) -> None:
    exit_code = main(["demo"])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Academic Paper Data Consistency Audit Demo" in captured.out
    assert "[PASS] Faradaic efficiency check" in captured.out
    assert "Synthetic data only" in captured.out
