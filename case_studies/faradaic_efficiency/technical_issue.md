# Technical Issue: Faradaic Efficiency Consistency

## Location

Synthetic Table 5, `Synthetic-Electrolyzer-B`.

## Observation

The synthetic row lists a current density of 0.5 A/cm², an active area of 1.0 cm², a measured product flow of 2.45 mL/min, and a reported Faradaic efficiency of 95.0%.

## Check / Recalculation

The total current is 0.5 A.

Using 2 electrons per product molecule, the theoretical product flow at 100% FE is approximately 3.485 mL/min under the default molar-volume convention used by the CLI.

The calculated FE from the listed product flow is approximately 70.3%, which differs from the synthetic reported value of 95.0%.

## Why It Matters

Faradaic efficiency connects current and product formation. A mismatch between measured product flow and reported FE may affect performance interpretation.

## Evidence Level

L2 — recalculation discrepancy.
