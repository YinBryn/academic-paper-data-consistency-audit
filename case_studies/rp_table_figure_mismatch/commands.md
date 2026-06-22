# Workflow

This case demonstrates a structured manual cross-check across three sources:

1. source data
2. plotted figure value
3. table-listed value

The synthetic data are in `source_data.csv`.

Suggested review steps:

```text
1. Identify the same sample and operating condition across all sources.
2. Extract the reported value from each location.
3. Check whether the values are numerically consistent within a stated tolerance.
4. If not, draft a neutral clarification request.
```

For the 600 °C row:

| Source | Rp (Ω·cm²) |
|---|---:|
| source data | 0.082 |
| figure plotted value | 0.080 |
| table listed value | 0.120 |

The source-data and figure values are close, but the table-listed value is materially higher.
