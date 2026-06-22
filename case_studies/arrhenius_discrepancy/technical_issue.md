# Technical Issue: Arrhenius Activation-Energy Recalculation

## Location

Synthetic Table 1, rows for `Synthetic-Cathode-A` at 800, 750, and 700 °C.

## Observation

The synthetic table reports an activation energy of 0.85 eV for `Synthetic-Cathode-A`.

## Check / Recalculation

Using the listed Rp values:

| Temperature (°C) | Rp (Ω·cm²) |
|---:|---:|
| 800 | 0.022 |
| 750 | 0.053 |
| 700 | 0.103 |

The Arrhenius check fits `ln(Rp)` against `1000/T`:

```bash
paper-audit arrhenius --temperature-c 800 750 700 --resistance 0.022 0.053 0.103
```

The recalculated activation energy is approximately 1.33 eV, which differs from the synthetic reported value of 0.85 eV.

## Why It Matters

Activation energy is commonly used to support mechanistic interpretation in electrochemical materials studies. A material difference between the reported and recalculated value may affect comparisons between samples or claims about rate-limiting processes.

## Evidence Level

L2 — recalculation discrepancy.
