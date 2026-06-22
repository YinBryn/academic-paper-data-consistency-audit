import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1] / "scripts"))

from arrhenius_fit import arrhenius_fit, linear_regression


def test_linear_regression_exact_line():
    slope, intercept, r2 = linear_regression([1, 2, 3], [3, 5, 7])
    assert slope == pytest.approx(2.0)
    assert intercept == pytest.approx(1.0)
    assert r2 == pytest.approx(1.0)


def test_arrhenius_fit_positive_ea():
    result = arrhenius_fit([800, 750, 700], [0.022, 0.053, 0.103])
    assert result.ea_ev > 0
    assert result.r_squared > 0.95
    assert len(result.x_1000_over_t) == 3


def test_arrhenius_fit_requires_positive_resistance():
    with pytest.raises(ValueError):
        arrhenius_fit([800, 750], [0.1, 0.0])
