import math

import pytest

from paper_audit.checks import calculate_faradaic_efficiency


def test_faradaic_efficiency_from_measured_flow():
    result = calculate_faradaic_efficiency(
        current_a=0.5,
        measured_flow_ml_min=3.30,
        electrons_per_molecule=2,
        reported_fe_pct=95.0,
        tolerance_pct_points=5.0,
    )
    assert math.isclose(result.theoretical_flow_100pct_ml_min, 3.4845711012514466)
    assert math.isclose(result.calculated_fe_pct, 94.70319026679755)
    assert math.isclose(result.fe_difference_pct_points, 0.29680973320244904)
    assert result.within_tolerance is True


def test_faradaic_efficiency_flags_reported_difference():
    result = calculate_faradaic_efficiency(
        current_a=0.5,
        measured_flow_ml_min=3.30,
        electrons_per_molecule=2,
        reported_fe_pct=70.0,
        tolerance_pct_points=5.0,
    )
    assert result.fe_difference_pct_points > 5.0
    assert result.within_tolerance is False


def test_faradaic_efficiency_rejects_zero_current():
    with pytest.raises(ValueError, match="current_a must be positive"):
        calculate_faradaic_efficiency(
            current_a=0.0,
            measured_flow_ml_min=3.30,
            electrons_per_molecule=2,
        )
