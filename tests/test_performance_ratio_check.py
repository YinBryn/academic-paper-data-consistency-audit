import csv
import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1] / "scripts"))

from performance_ratio_check import batch_comparison_from_csv, improvement_ratio, reduction_ratio


def test_improvement_ratio():
    assert improvement_ratio(3.0, 2.0) == pytest.approx(50.0)


def test_reduction_ratio():
    assert reduction_ratio(1.0, 2.0) == pytest.approx(50.0)


def test_batch_comparison_from_csv(tmp_path):
    csv_path = tmp_path / "data.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["sample", "temperature_C", "Pmax"])
        writer.writeheader()
        writer.writerow({"sample": "Baseline", "temperature_C": "800", "Pmax": "2.0"})
        writer.writerow({"sample": "Modified", "temperature_C": "800", "Pmax": "3.0"})
    rows = batch_comparison_from_csv(csv_path, "Modified", "Baseline", "Pmax")
    assert len(rows) == 1
    assert rows[0]["improvement_pct"] == pytest.approx(50.0)
