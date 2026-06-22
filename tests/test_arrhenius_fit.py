import sys
from pathlib import Path
import pytest

# Add scripts directory to path
scripts_dir = Path(__file__).resolve().parent.parent / "scripts"
sys.path.append(str(scripts_dir))

from arrhenius_fit import linear_regression, KB

def test_linear_regression():
    # Simple linear relationship y = -2*x + 10
    x = [1, 2, 3, 4, 5]
    y = [8, 6, 4, 2, 0]
    
    m, c, r_sq = linear_regression(x, y)
    
    assert pytest.approx(m) == -2.0
    assert pytest.approx(c) == 10.0
    assert pytest.approx(r_sq) == 1.0

def test_arrhenius_values():
    # Test case from anonymized case study
    # 500C, 550C, 600C => 1000/T values:
    # 500C: 1000 / (500 + 273.15) = 1.29341
    # 550C: 1000 / (550 + 273.15) = 1.21485
    # 600C: 1000 / (600 + 273.15) = 1.14528
    temp_k = [773.15, 823.15, 873.15]
    inv_t = [1000.0 / tk for tk in temp_k]
    
    # Rp values: 1.25, 0.52, 0.22
    import math
    ln_y = [math.log(1.0 / r) for r in [1.25, 0.52, 0.22]]
    
    m, c, r_sq = linear_regression(inv_t, ln_y)
    ea = -m * 1000.0 * KB
    
    assert pytest.approx(ea, rel=1e-2) == 1.01
    assert r_sq > 0.99
