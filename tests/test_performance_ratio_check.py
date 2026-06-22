import sys
from pathlib import Path
import pytest

# Add scripts directory to path
scripts_dir = Path(__file__).resolve().parent.parent / "scripts"
sys.path.append(str(scripts_dir))

from performance_ratio_check import improvement_ratio, reduction_ratio

def test_improvement_ratio():
    baseline = 0.50
    new_val = 1.25
    
    ratio = improvement_ratio(new_val, baseline)
    assert pytest.approx(ratio) == 150.0

def test_reduction_ratio():
    baseline = 0.85
    new_val = 0.17
    
    ratio = reduction_ratio(new_val, baseline)
    assert pytest.approx(ratio) == 80.0

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        improvement_ratio(1.0, 0.0)
    with pytest.raises(ZeroDivisionError):
        reduction_ratio(1.0, 0.0)
