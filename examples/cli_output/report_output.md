# Synthetic Audit Report

A compact report generated from synthetic checks.

## Summary

- **checks_run:** 5
- **pass_count:** 4
- **flag_count:** 1
- **info_count:** 0

## Check 1: I-V-P consistency

- **id:** ivp_consistency
- **type:** dimensional
- **status:** PASS
- **note:** Checked the P = j x V relation.

| field | value |
|---|---:|
| calculated_power_density | 2.6 |
| difference_pct | 0.0 |
| relation_consistent | True |

## Check 2: Resistance component sum

- **id:** resistance_component_sum
- **type:** resistance-sum
- **status:** PASS
- **note:** Checked reported total against listed components.

| field | value |
|---|---:|
| reported_total | 0.151 |
| component_sum | 0.151 |
| absolute_difference | 0.0 |
| relative_difference_pct | 0.0 |
| within_tolerance | True |

## Check 3: Faradaic efficiency recalculation

- **id:** faradaic_efficiency
- **type:** faradaic-efficiency
- **status:** FLAG
- **note:** Calculated flow-based Faradaic efficiency.

| field | value |
|---|---:|
| calculated_fe_pct | ... |
| reported_fe_pct | 95.0 |
| within_tolerance | False |

## Check 4: Conductivity geometry normalization

- **id:** conductivity_geometry
- **type:** conductivity-geometry
- **status:** PASS
- **note:** Calculated geometry-normalized conductivity.

| field | value |
|---|---:|
| calculated_conductivity_s_cm | ... |
| reported_conductivity_s_cm | 0.01167 |
| within_tolerance | True |

## Check 5: Batch tolerance summary

- **id:** batch_tolerance_report
- **type:** tolerance-report
- **status:** PASS
- **note:** Built a row-level tolerance summary.

| field | value |
|---|---:|
| total_rows | ... |
| pass_count | ... |
| fail_count | 0 |
