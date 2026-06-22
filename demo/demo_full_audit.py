"""
demo_full_audit.py
==================
End-to-end demonstration of the Academic Paper Data Consistency Audit toolkit.

This script runs all four diagnostic scripts on synthetic (mock) data and
prints a concise audit summary.  No real paper data is used.

Usage
-----
    python demo/demo_full_audit.py

Requirements
------------
    pip install -r requirements.txt
"""

import sys
import os
import math

# Make sure we can import from scripts/
ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from arrhenius_fit import arrhenius_fit          # noqa: E402
from statistics_check import check_statistics    # noqa: E402
from performance_ratio_check import compute_ratio  # noqa: E402
from dimensional_check import check_ivp          # noqa: E402


SEPARATOR = "=" * 60

def section(title: str):
    print(f"\n{SEPARATOR}")
    print(f"  {title}")
    print(SEPARATOR)


def main():
    print("\n" + SEPARATOR)
    print("  Academic Paper Data Consistency Audit — Demo")
    print("  Toolkit version: v0.1.0-alpha")
    print(SEPARATOR)

    # ------------------------------------------------------------------
    # STEP 1: Arrhenius Activation Energy Check
    # Scenario: Paper reports Ea = 0.65 eV from conductivity data at
    #           600, 650, 700 °C.  We reproduce the fit.
    # ------------------------------------------------------------------
    section("Step 1 · Arrhenius Activation Energy (Ea) Recalculation")

    temps_C = [600, 650, 700]
    rp_values = [1.25, 0.55, 0.24]   # mock Ω·cm²
    print(f"  Input temperatures (°C) : {temps_C}")
    print(f"  Input Rp values (Ω·cm²) : {rp_values}")

    ea_result = arrhenius_fit(temps_C, rp_values, mode="kinetic")
    print(f"  Recalculated Ea         : {ea_result['Ea_eV']:.4f} eV")
    paper_ea = 0.65
    delta_ea = abs(ea_result['Ea_eV'] - paper_ea)
    status = "✅ CONSISTENT" if delta_ea < 0.02 else "⚠️  DISCREPANCY"
    print(f"  Paper-reported Ea       : {paper_ea:.4f} eV")
    print(f"  Δ Ea                    : {delta_ea:.4f} eV  →  {status}")

    # ------------------------------------------------------------------
    # STEP 2: Statistical Data Consistency Check
    # Scenario: Paper reports mean = 0.253 ± 0.012 from 5 measurements.
    # ------------------------------------------------------------------
    section("Step 2 · Statistical Mean / SD Recalculation")

    raw_data = [0.248, 0.257, 0.251, 0.260, 0.249]
    reported_mean = 0.253
    print(f"  Raw measurements : {raw_data}")
    print(f"  Reported mean    : {reported_mean}")

    stat_result = check_statistics(raw_data, reported_mean)
    print(f"  Recalculated mean: {stat_result['calculated_mean']:.4f}")
    print(f"  Recalculated SD  : {stat_result['calculated_sd']:.4f}")
    print(f"  Δ mean           : {stat_result['delta_mean']:.4f}  →  {stat_result['status']}")

    # ------------------------------------------------------------------
    # STEP 3: I–V–P Physical Consistency Check
    # Scenario: Paper reports I = 1.5 A/cm², V = 0.63 V, P = 0.95 W/cm².
    #           Physical expectation: P = I × V = 0.945 W/cm².
    # ------------------------------------------------------------------
    section("Step 3 · I–V–P Physical Consistency (P = I × V)")

    I, V, P_reported = 1.5, 0.63, 0.95
    print(f"  Reported I = {I} A/cm², V = {V} V, P = {P_reported} W/cm²")

    ivp_result = check_ivp(I, V, P_reported, tolerance_pct=1.0)
    print(f"  Expected P (I×V) : {ivp_result['expected_P']:.4f} W/cm²")
    print(f"  Δ P              : {ivp_result['delta_pct']:.2f}%  →  {ivp_result['status']}")

    # ------------------------------------------------------------------
    # STEP 4: Performance Ratio (Improvement %) Check
    # Scenario: Paper claims "47% improvement" from baseline Rp to
    #           modified-cathode Rp.
    # ------------------------------------------------------------------
    section("Step 4 · Performance Ratio / Improvement % Check")

    baseline_rp = 1.25
    modified_rp = 0.66
    claimed_improvement = 47.2   # % as stated in paper

    ratio_result = compute_ratio(baseline_rp, modified_rp)
    recalc_improvement = ratio_result['improvement_pct']
    delta_ratio = abs(recalc_improvement - claimed_improvement)
    r_status = "✅ CONSISTENT" if delta_ratio < 1.0 else "⚠️  DISCREPANCY"
    print(f"  Baseline Rp       : {baseline_rp} Ω·cm²")
    print(f"  Modified Rp       : {modified_rp} Ω·cm²")
    print(f"  Paper claims      : {claimed_improvement:.1f}% improvement")
    print(f"  Recalculated      : {recalc_improvement:.1f}% improvement")
    print(f"  Δ improvement     : {delta_ratio:.1f}%  →  {r_status}")

    # ------------------------------------------------------------------
    # SUMMARY
    # ------------------------------------------------------------------
    section("Audit Summary")
    print("""
  All four diagnostic checks completed.

  In a real audit workflow you would:
    1. Replace synthetic values above with numbers extracted from the paper.
    2. Note any ⚠️ DISCREPANCY findings for follow-up.
    3. Use templates/pubpeer_style_issue_format.md to draft a neutral
       technical comment for each unresolved discrepancy.
    4. Classify each finding using methodology/evidence_levels.md (L1–L5).
    5. Follow docs/language_safety.md when writing the final report.
    """)
    print(SEPARATOR + "\n")


if __name__ == "__main__":
    main()
