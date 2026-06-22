from paper_audit.cli import main


def test_cli_arrhenius_outputs_ea(capsys):
    exit_code = main(["arrhenius", "--temperature-c", "800", "750", "700", "--resistance", "0.022", "0.053", "0.103"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Arrhenius fitting result" in captured.out
    assert "Ea:" in captured.out


def test_cli_statistics_compares_reported_values(capsys):
    exit_code = main([
        "statistics",
        "--values", "4.65", "4.83", "4.84", "4.76", "4.77",
        "--reported-mean", "4.79",
        "--reported-std", "0.08",
    ])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Statistics recalculation result" in captured.out
    assert "reported_mean_difference_pct" in captured.out


def test_cli_ratio_outputs_improvement(capsys):
    exit_code = main(["ratio", "--new", "3.53", "--baseline", "2.74"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Improvement ratio:" in captured.out


def test_cli_dimensional_checks_power_relation(capsys):
    exit_code = main(["dimensional", "--power-density", "2.6", "--current-density", "2.0", "--voltage", "1.3"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "calculated_power_density: 2.600000" in captured.out
    assert "relation_consistent: True" in captured.out
