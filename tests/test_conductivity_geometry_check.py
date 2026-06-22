import math

import pytest

from paper_audit.checks import calculate_conductivity_from_geometry


def test_conductivity_geometry_calculation_matches_reported():
    result = calculate_conductivity_from_geometry(
        resistance_ohm=10.0,
        thickness_cm=0.033,
        area_cm2=0.2827433388230814,
        reported_conductivity_s_cm=0.01167,
        tolerance_pct=1.0,
    )
    assert math.isclose(result.calculated_conductivity_s_cm, 0.01167112211314011)
    assert result.within_tolerance is True


def test_conductivity_geometry_flags_difference():
    result = calculate_conductivity_from_geometry(
        resistance_ohm=10.0,
        thickness_cm=0.033,
        area_cm2=0.2827433388230814,
        reported_conductivity_s_cm=0.020,
        tolerance_pct=5.0,
    )
    assert result.relative_difference_pct > 5.0
    assert result.within_tolerance is False


def test_conductivity_geometry_rejects_zero_resistance():
    with pytest.raises(ValueError, match="resistance_ohm must be positive"):
        calculate_conductivity_from_geometry(
            resistance_ohm=0.0,
            thickness_cm=0.033,
            area_cm2=0.2827433388230814,
        )
