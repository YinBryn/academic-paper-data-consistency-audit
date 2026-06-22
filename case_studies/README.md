# Synthetic Case Studies

This directory contains fully synthetic examples that demonstrate how to use the audit workflow without referencing any real paper, author, DOI, journal, or publisher-provided data set.

Each case study is designed to show one narrow technical issue at a time, following a PubPeer-style post-publication review principle:

> one issue, one location, one reproducible check, neutral wording.

## Included cases

| Case | Technical focus | Main tool or workflow |
|---|---|---|
| `arrhenius_discrepancy/` | Activation-energy recalculation | `paper-audit arrhenius` |
| `ivp_consistency/` | Power density consistency using `P = jV` | `paper-audit dimensional` |
| `tolerance_report/` | Batch table/source-data comparison | `paper-audit tolerance-report` |
| `resistance_component_sum/` | Rp/ASR component-sum consistency | `paper-audit resistance-sum` |
| `faradaic_efficiency/` | FE and product-flow consistency | `paper-audit faradaic-efficiency` |
| `conductivity_geometry/` | Conductivity geometry normalization | `paper-audit conductivity-geometry` |
| `rp_table_figure_mismatch/` | Figure/table/source-data mismatch | structured manual cross-check |
| `evidence_claim_overreach/` | Evidence-claim alignment | neutral technical reasoning template |

## Responsible-use note

These examples are not evidence of misconduct. They are training examples for technical clarification, recalculation, and reproducibility-oriented communication.
