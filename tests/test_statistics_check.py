import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1] / "scripts"))

from statistics_check import calculate_statistics, compare_reported_value


def test_calculate_statistics():
    result = calculate_statistics([1, 2, 3, 4, 5])
    assert result.n == 5
    assert result.mean == pytest.approx(3.0)
    assert result.sample_std == pytest.approx(1.58113883008)
    assert result.population_std == pytest.approx(1.41421356237)


def test_compare_reported_value_within_tolerance():
    comparison = compare_reported_value(3.0, 1.58, [1, 2, 3, 4, 5], tolerance_pct=1.0)
    assert comparison["mean_within_tolerance"] is True
    assert comparison["std_within_tolerance"] is True


def test_compare_reported_value_outside_tolerance():
    comparison = compare_reported_value(3.5, 1.0, [1, 2, 3, 4, 5], tolerance_pct=1.0)
    assert comparison["mean_within_tolerance"] is False
    assert comparison["std_within_tolerance"] is False
