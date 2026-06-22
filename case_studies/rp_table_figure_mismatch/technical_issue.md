# Technical Issue: Rp Table/Figure/Source-Data Mismatch

## Location

Synthetic Figure 3b, Synthetic Table 1, and synthetic source-data file for `Synthetic-Electrode-A` at 600 °C.

## Observation

For the same sample and temperature condition, the synthetic values are:

| Location | Rp (Ω·cm²) |
|---|---:|
| source data | 0.082 |
| plotted figure value | 0.080 |
| table-listed value | 0.120 |

The source-data and plotted figure values are close to each other, while the table-listed value differs.

## Check / Recalculation

The relative difference between the source-data value and the table-listed value is:

```text
abs(0.120 - 0.082) / 0.082 × 100% = 46.3%
```

## Why It Matters

Polarization resistance is commonly used to compare electrode kinetics. If figure, table, and source-data values differ for the same sample and condition, downstream comparisons or activation-energy fits may depend on which value is used.

## Evidence Level

L1 — direct numerical inconsistency.
