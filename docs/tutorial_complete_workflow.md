# Complete Synthetic Audit Workflow

This tutorial shows a compact end-to-end workflow using synthetic data only.

The goal is to move from a reported value, through an independent recalculation, to a short neutral technical note.

## 1. Start with a reported relation

Suppose a synthetic table reports the following cell values:

| quantity | value |
|---|---:|
| current density | 2.0 A cm^-2 |
| voltage | 1.3 V |
| power density | 2.6 W cm^-2 |

The physical relation is:

```text
power density = current density x voltage
```

## 2. Run a dimensional consistency check

```bash
paper-audit dimensional \
  --power-density 2.6 \
  --current-density 2.0 \
  --voltage 1.3
```

Expected output pattern:

```text
calculated_power_density: 2.600000
difference_pct: 0.000000
relation_consistent: True
```

Interpretation: the reported power density is consistent with the current density and voltage under the selected tolerance.

## 3. Check a resistance component sum

Suppose a synthetic table lists three polarization-resistance components and one total:

| component | value |
|---|---:|
| R1 | 0.052 |
| R2 | 0.061 |
| R3 | 0.038 |
| reported total | 0.151 |

Run:

```bash
paper-audit resistance-sum \
  --reported-total 0.151 \
  --components 0.052 0.061 0.038 \
  --tolerance-pct 1.0
```

Expected output pattern:

```text
component_sum: 0.151000
relative_difference_pct: 0.000000
within_tolerance: True
```

Interpretation: the reported total is consistent with the listed components.

## 4. Generate a batch tolerance report

Use the synthetic tolerance-report case study:

```bash
paper-audit tolerance-report \
  --csv case_studies/tolerance_report/input.csv \
  --reported-column reported_Rp_ohm_cm2 \
  --reference-column source_Rp_ohm_cm2 \
  --id-column sample \
  --tolerance-pct 5.0
```

Expected output pattern:

```text
Tolerance report
----------------
total_rows: ...
pass_count: ...
fail_count: ...
```

Interpretation: rows outside the selected tolerance are candidates for closer technical review.

## 5. Convert the check into a neutral note

A compact note should separate location, observation, recalculation, and clarification request:

```text
Location: synthetic Table S1, row A.
Observation: the reported value differs from the reference value by more than the selected tolerance.
Check: recalculation with paper-audit tolerance-report gives a relative difference above the configured threshold.
Why it matters: the value is used in a later comparison, so the numerical basis should be clear.
Clarification request: please clarify which value should be used for the comparison.
```

## 6. Recommended workflow order

1. Extract the reported values into a small table.
2. Identify the governing relation or recalculation formula.
3. Run the relevant CLI check.
4. Save the command and output.
5. Write a short neutral note.
6. Keep examples synthetic when documenting the workflow publicly.

## 7. Quick smoke test

After installation, run:

```bash
paper-audit demo
```

This confirms that the installed command-line interface works and that representative checks can run in the current environment.
