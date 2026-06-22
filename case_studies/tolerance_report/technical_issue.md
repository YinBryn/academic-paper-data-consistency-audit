# Technical Issue: Batch Table/Source-Data Tolerance Report

## Location

Synthetic Table 7 and synthetic source-data comparison for Rp values.

## Observation

The synthetic comparison contains three rows. Two rows are within a 5% relative tolerance, while one row is outside the selected tolerance.

## Check / Recalculation

Using `paper-audit tolerance-report`, the row `Synthetic-B` shows:

- reported value: 0.120 Ω·cm²
- source-data value: 0.082 Ω·cm²
- relative difference: approximately 46.3%

## Why It Matters

Batch comparison helps identify whether a discrepancy is isolated to one row or affects multiple reported values. This is useful when checking tables against source data or digitized figure values.

## Evidence Level

L1 — direct numerical inconsistency.
