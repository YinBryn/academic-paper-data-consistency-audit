import math

import pytest

from paper_audit.checks import check_component_sum


def test_component_sum_within_tolerance():
    result = check_component_sum(
        reported_total=0.151,
        components=[0.052, 0.061, 0.038],
        tolerance_pct=1.0,
    )
    assert math.isclose(result.component_sum, 0.151)
    assert math.isclose(result.absolute_difference, 0.0)
    assert result.within_tolerance is True


def test_component_sum_flags_difference():
    result = check_component_sum(
        reported_total=0.180,
        components=[0.052, 0.061, 0.038],
        tolerance_pct=1.0,
    )
    assert math.isclose(result.component_sum, 0.151)
    assert result.relative_difference_pct > 1.0
    assert result.within_tolerance is False


def test_component_sum_rejects_negative_component():
    with pytest.raises(ValueError, match="component values must be non-negative"):
        check_component_sum(reported_total=0.1, components=[0.05, -0.02])
