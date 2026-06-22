# Technical Issue: Resistance Component-Sum Consistency

## Location

Synthetic Table 4, `Synthetic-Electrode-B` at 600 °C.

## Observation

The synthetic table reports:

- total Rp: 0.180 Ω·cm²
- component 1: 0.052 Ω·cm²
- component 2: 0.061 Ω·cm²
- component 3: 0.038 Ω·cm²

## Check / Recalculation

The sum of listed components is:

```text
0.052 + 0.061 + 0.038 = 0.151 Ω·cm²
```

The relative difference between the reported total and the component sum is:

```text
abs(0.180 - 0.151) / 0.151 × 100% = 19.2%
```

This is outside a 1% tolerance.

## Why It Matters

Rp or ASR component tables are often used to assign electrochemical limitations to specific processes. If the reported total does not match the listed components, the quantitative process assignment may require clarification.

## Evidence Level

L1 — direct numerical inconsistency.
