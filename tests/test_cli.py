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


def test_cli_resistance_sum_flags_difference(capsys):
    exit_code = main([
        "resistance-sum",
        "--reported-total", "0.180",
        "--components", "0.052", "0.061", "0.038",
        "--tolerance-pct", "1.0",
    ])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Resistance component-sum result" in captured.out
    assert "component_sum: 0.151000" in captured.out
    assert "within_tolerance: False" in captured.out


def test_cli_faradaic_efficiency_outputs_calculated_fe(capsys):
    exit_code = main([
        "faradaic-efficiency",
        "--current-density-a-cm2", "0.5",
        "--area-cm2", "1.0",
        "--measured-flow-ml-min", "3.30",
        "--electrons-per-molecule", "2",
        "--reported-fe-pct", "95.0",
    ])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Faradaic efficiency result" in captured.out
    assert "calculated_fe_pct: 94.703190" in captured.out
    assert "within_tolerance: True" in captured.out


def test_cli_conductivity_geometry_outputs_conductivity(capsys):
    exit_code = main([
        "conductivity-geometry",
        "--resistance-ohm", "10.0",
        "--thickness-mm", "0.33",
        "--diameter-mm", "6.0",
        "--reported-conductivity-s-cm", "0.01167",
    ])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Conductivity geometry result" in captured.out
    assert "calculated_conductivity_s_cm: 0.01167136" in captured.out
    assert "within_tolerance: True" in captured.out


def test_cli_tolerance_report_outputs_summary(tmp_path, capsys):
    csv_path = tmp_path / "values.csv"
    csv_path.write_text(
        "sample,reported,source\nA,1.02,1.00\nB,1.30,1.00\n",
        encoding="utf-8",
    )
    exit_code = main([
        "tolerance-report",
        "--csv", str(csv_path),
        "--reported-column", "reported",
        "--reference-column", "source",
        "--id-column", "sample",
        "--tolerance-pct", "5.0",
    ])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Tolerance report" in captured.out
    assert "pass_count: 1" in captured.out
    assert "fail_count: 1" in captured.out
    assert "| B | 1.3 | 1 | 0.3 | 30.000000 | False |" in captured.out
