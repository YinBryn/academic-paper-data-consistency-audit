# CLI Expected Outputs

This page summarizes the expected output shape for the main `paper-audit` commands. Exact numeric values may change if input values change, but the field names should remain stable.

## `paper-audit demo`

```bash
paper-audit demo
```

Expected output shape:

```text
Academic Paper Data Consistency Audit Demo
===========================================
Synthetic data only. No real article data is used.

[PASS] Arrhenius recalculation - ...
[PASS] Statistics recalculation - ...
[PASS] I-V-P dimensional check - ...
[PASS] Resistance component-sum check - ...
[PASS] Faradaic efficiency check - ...
[PASS] Conductivity geometry check - ...
[PASS] Batch tolerance report - ...

Demo completed: 7 synthetic checks passed.
```

## `paper-audit arrhenius`

```bash
paper-audit arrhenius \
  --temperature-c 800 750 700 \
  --resistance 0.022 0.053 0.103
```

Expected fields:

```text
Arrhenius fitting result
------------------------
Fitted quantity: ln(R)
Slope: ...
Intercept: ...
R^2: ...
Ea: ... eV
```

## `paper-audit statistics`

```bash
paper-audit statistics \
  --values 4.65 4.83 4.84 4.76 4.77 \
  --reported-mean 4.79 \
  --reported-std 0.04
```

Expected fields:

```text
Statistics recalculation result
-------------------------------
n: ...
mean: ...
sample_std: ...
population_std: ...
reported_mean_difference_pct: ...
reported_mean_within_tolerance: ...
reported_std_difference_pct: ...
reported_std_within_tolerance: ...
```

## `paper-audit ratio`

```bash
paper-audit ratio --new 3.53 --baseline 2.74
```

Expected field:

```text
Improvement ratio: ...%
```

## `paper-audit dimensional`

```bash
paper-audit dimensional \
  --power-density 2.6 \
  --current-density 2.0 \
  --voltage 1.3
```

Expected fields:

```text
calculated_power_density: ...
difference_pct: ...
relation_consistent: ...
```

## `paper-audit tolerance-report`

```bash
paper-audit tolerance-report \
  --csv case_studies/tolerance_report/input.csv \
  --reported-column reported_Rp_ohm_cm2 \
  --reference-column source_Rp_ohm_cm2 \
  --id-column sample \
  --tolerance-pct 5.0
```

Expected fields:

```text
Tolerance report
----------------
total_rows: ...
pass_count: ...
fail_count: ...
tolerance_pct: ...
```

The command also prints a row-level Markdown-style table.

## `paper-audit resistance-sum`

```bash
paper-audit resistance-sum \
  --reported-total 0.180 \
  --components 0.052 0.061 0.038 \
  --tolerance-pct 1.0
```

Expected fields:

```text
Resistance component-sum result
-------------------------------
reported_total: ...
component_sum: ...
absolute_difference: ...
relative_difference_pct: ...
within_tolerance: ...
```

## `paper-audit faradaic-efficiency`

```bash
paper-audit faradaic-efficiency \
  --current-density-a-cm2 0.5 \
  --area-cm2 1.0 \
  --measured-flow-ml-min 3.30 \
  --electrons-per-molecule 2 \
  --reported-fe-pct 95.0
```

Expected fields:

```text
Faradaic efficiency result
--------------------------
current_a: ...
electrons_per_molecule: ...
theoretical_flow_100pct_ml_min: ...
measured_flow_ml_min: ...
calculated_fe_pct: ...
reported_fe_pct: ...
fe_difference_pct_points: ...
within_tolerance: ...
```

## `paper-audit conductivity-geometry`

```bash
paper-audit conductivity-geometry \
  --resistance-ohm 10.0 \
  --thickness-mm 0.33 \
  --diameter-mm 6.0 \
  --reported-conductivity-s-cm 0.01167
```

Expected fields:

```text
Conductivity geometry result
----------------------------
resistance_ohm: ...
thickness_cm: ...
area_cm2: ...
calculated_conductivity_s_cm: ...
reported_conductivity_s_cm: ...
relative_difference_pct: ...
within_tolerance: ...
```
