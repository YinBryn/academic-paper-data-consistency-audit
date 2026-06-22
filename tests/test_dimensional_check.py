import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1] / "scripts"))

from dimensional_check import (
    check_current_density_power_density_relation,
    check_diffusion_unit,
    check_potential_unit,
)


def test_diffusion_units():
    assert check_diffusion_unit("cm^2/s")[0] is True
    assert check_diffusion_unit("A2/ps")[0] is True
    assert check_diffusion_unit("cm/s")[0] is False


def test_potential_units():
    assert check_potential_unit("V")[0] is True
    assert check_potential_unit("mV")[0] is True
    ok, message = check_potential_unit("eV")
    assert ok is False
    assert "energy" in message


def test_power_current_voltage_relation():
    ok, calculated, diff = check_current_density_power_density_relation(2.6, 2.0, 1.3)
    assert ok is True
    assert calculated == pytest.approx(2.6)
    assert diff == pytest.approx(0.0)
    ok, calculated, diff = check_current_density_power_density_relation(2.0, 2.0, 1.3)
    assert ok is False
    assert calculated == pytest.approx(2.6)
    assert diff > 20
