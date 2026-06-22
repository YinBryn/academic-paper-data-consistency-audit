import sys
from pathlib import Path
import pytest

# Add scripts directory to path
scripts_dir = Path(__file__).resolve().parent.parent / "scripts"
sys.path.append(str(scripts_dir))

from statistics_check import (
    calculate_mean,
    calculate_sample_std,
    calculate_population_std,
    compare_reported_value
)

def test_statistics_calculations():
    test_data = [0.24, 0.26, 0.25, 0.27, 0.23]
    
    mean = calculate_mean(test_data)
    sample_std = calculate_sample_std(test_data, mean)
    pop_std = calculate_population_std(test_data, mean)
    
    assert pytest.approx(mean) == 0.2500
    assert pytest.approx(sample_std, rel=1e-3) == 0.01581
    assert pytest.approx(pop_std, rel=1e-3) == 0.01414

def test_comparison_logic():
    calculated_val = 0.2500
    
    # Within 1% tolerance
    ok1, diff1 = compare_reported_value(0.251, calculated_val, tolerance_pct=1.0)
    assert ok1 is True
    assert pytest.approx(diff1) == 0.40
    
    # Outside 1% tolerance
    ok2, diff2 = compare_reported_value(0.260, calculated_val, tolerance_pct=1.0)
    assert ok2 is False
    assert pytest.approx(diff2) == 4.0
