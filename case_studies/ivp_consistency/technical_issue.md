# Technical Issue: I–V–P Consistency Check

## Location

Synthetic Table 2, rows for fuel-cell power-density values.

## Observation

`Synthetic-Cell-B` lists:

- current density: 2.00 A/cm²
- voltage: 0.70 V
- reported power density: 1.10 W/cm²

## Check / Recalculation

For fuel-cell power density, the direct relation is:

```text
P = j × V
```

Using the reported current density and voltage:

```text
P = 2.00 A/cm² × 0.70 V = 1.40 W/cm²
```

This differs from the synthetic reported value of 1.10 W/cm².

## Why It Matters

Power-density values are often used to compare electrochemical cell performance. If a listed power density does not match the reported current density and voltage at the same operating point, the performance comparison may require clarification.

## Evidence Level

L1 — direct numerical inconsistency.
