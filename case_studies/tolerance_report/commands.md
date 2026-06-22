# Commands

This case compares multiple table-reported Rp values against synthetic source-data values.

```bash
paper-audit tolerance-report \
  --csv case_studies/tolerance_report/input.csv \
  --reported-column reported_Rp_ohm_cm2 \
  --reference-column source_Rp_ohm_cm2 \
  --id-column sample \
  --tolerance-pct 5.0
```

Expected interpretation:

- `Synthetic-A` is within tolerance.
- `Synthetic-B` is outside tolerance.
- `Synthetic-C` is within tolerance.
