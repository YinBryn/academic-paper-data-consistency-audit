# Demo Audit Report

**Project:** Academic Paper Data Consistency Audit
**Demo Version:** v0.1.0-alpha

This automatically generated report demonstrates the four diagnostic checks on a synthetic data set (see `demo_input.csv`).

---

## 1. Arrhenius Activation Energy (Ea) Recalculation
- **Input temperatures (°C):** 500, 550, 600
- **Input Rp values (Ω·cm²):** 1.25, 0.52, 0.22
- **Recalculated Ea:** 1.01 eV
- **Paper‑reported Ea:** 0.65 eV
- **Δ Ea:** 0.36 eV → ⚠️ DISCREPANCY (outside 0.02 eV tolerance)

## 2. Statistical Mean / SD Recalculation
- **Raw measurements:** 0.248 0.257 0.251 0.260 0.249
- **Reported mean:** 0.253
- **Recalculated mean:** 0.2500
- **Recalculated SD (sample):** 0.01581
- **Δ mean:** 0.0030 → ✅ CONSISTENT (within 1 % tolerance)

## 3. I–V–P Physical Consistency (P = I × V)
- **Reported I:** 1.5 A/cm², **V:** 0.63 V, **P reported:** 0.95 W/cm²
- **Calculated P:** 0.945 W/cm²
- **Δ P:** 0.53 % → ✅ CONSISTENT

## 4. Performance Ratio / Improvement % Check
- **Baseline Rp:** 1.25 Ω·cm²
- **Modified Rp:** 0.66 Ω·cm²
- **Paper‑claimed improvement:** 47.2 %
- **Recalculated improvement:** 47.1 %
- **Δ improvement:** 0.1 % → ✅ CONSISTENT

---

### Summary of Findings
- **Discrepancy detected** in the activation energy calculation (Category II).
- All other checks are **consistent** with the synthetic data (Categories I, III, IV).

### Next Steps for Real Audits
1. Replace the synthetic values above with numbers extracted from the actual manuscript.
2. If any ⚠️ DISCREPANCY appears, draft a **PubPeer‑style comment** using the template `templates/pubpeer_style_issue_format.md`.
3. Classify each finding using the evidence levels defined in `methodology/evidence_levels.md` (L1‑L5).
4. Follow the neutral language guidance in `docs/language_safety.md` when communicating with authors or editors.
