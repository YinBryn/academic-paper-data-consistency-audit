import sys
from pathlib import Path
import pytest

# Add scripts directory to path
scripts_dir = Path(__file__).resolve().parent.parent / "scripts"
sys.path.append(str(scripts_dir))

from dimensional_check import (
    check_diffusion_unit,
    check_potential_unit,
    check_current_density_power_density_relation
)

def test_diffusion_unit_check():
    # Valid units
    assert check_diffusion_unit("cm2/s")[0] is True
    assert check_diffusion_unit("cm^2/s")[0] is True
    assert check_diffusion_unit("m2/s")[0] is True
    assert check_diffusion_unit("cm2 s-1")[0] is True
    
    # Invalid units
    assert check_diffusion_unit("cm/s")[0] is False
    assert "velocity" in check_diffusion_unit("cm/s")[1]
    assert check_diffusion_unit("m/s")[0] is False

def test_potential_unit_check():
    # Valid units
    assert check_potential_unit("V")[0] is True
    assert check_potential_unit("mV")[0] is True
    assert check_potential_unit("V (vs. OCV)")[0] is True
    
    # Invalid units
    assert check_potential_unit("amperes")[0] is False
    assert check_potential_unit("W")[0] is False

def test_ivp_relation_check():
    # P = I * V => 1.5 A/cm2 * 0.6 V = 0.9 W/cm2
    ok1, calc1, err1 = check_current_density_power_density_relation(1.5, 0.6, 0.9, tolerance_pct=1.0)
    assert ok1 is True
    assert pytest.approx(calc1) == 0.9
    assert pytest.approx(err1) == 0.0
    
    # Non-matching: 1.5 A/cm2 * 0.6 V = 0.9 W/cm2, but reported is 1.1 W/cm2
    ok2, calc2, err2 = check_current_density_power_density_relation(1.5, 0.6, 1.1, tolerance_pct=1.0)
    assert ok2 is False
    assert pytest.approx(calc2) == 0.9
    assert err2 > 20.0
