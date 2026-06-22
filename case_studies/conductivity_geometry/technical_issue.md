# Technical Issue: Conductivity Geometry Normalization

## Location

Synthetic Table 6, `Synthetic-Electrolyte-B`.

## Observation

The synthetic row lists:

- resistance: 10.0 ohm
- thickness: 0.33 mm
- diameter: 6.0 mm
- reported conductivity: 0.02000 S/cm

## Check / Recalculation

The geometry-normalized conductivity is calculated using:

```text
sigma = L / (R × A)
```

For a 6.0 mm diameter circular sample, the area is approximately 0.28274 cm². The thickness is 0.033 cm.

```text
sigma = 0.033 / (10.0 × 0.28274) ≈ 0.01167 S/cm
```

This differs from the synthetic reported value of 0.02000 S/cm.

## Why It Matters

Conductivity values depend directly on sample geometry. A mismatch in thickness or area normalization can affect Arrhenius fits, activation energies, and cross-sample comparisons.

## Evidence Level

L2 — recalculation discrepancy.
