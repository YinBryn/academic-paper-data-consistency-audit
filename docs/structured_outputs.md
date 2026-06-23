# Structured Outputs

Most calculation commands support a common output option:

```bash
--output text
--output json
--output markdown
--output csv
```

The default is `text`.

## Why structured output matters

Structured outputs make it easier to:

- save recalculation results in a reproducible form
- paste results into reports
- parse results in downstream scripts
- compare repeated checks across several examples

## JSON example

```bash
paper-audit ratio \
  --new 3.53 \
  --baseline 2.74 \
  --output json
```

Expected output shape:

```json
{
  "mode": "improvement",
  "ratio_pct": 28.832117
}
```

## Markdown example

```bash
paper-audit resistance-sum \
  --reported-total 0.151 \
  --components 0.052 0.061 0.038 \
  --output markdown
```

Expected output shape:

```markdown
## Resistance component-sum result

| field | value |
|---|---:|
| reported_total | ... |
| component_sum | ... |
| within_tolerance | True |
```

## CSV example

```bash
paper-audit tolerance-report \
  --csv case_studies/tolerance_report/input.csv \
  --reported-column reported_Rp_ohm_cm2 \
  --reference-column source_Rp_ohm_cm2 \
  --id-column sample \
  --output csv
```

Expected output shape:

```csv
row_id,reported,reference,abs_diff,rel_diff_pct,pass
...
```

## Supported commands

The following commands support structured output:

- `paper-audit arrhenius`
- `paper-audit statistics`
- `paper-audit ratio`
- `paper-audit dimensional`
- `paper-audit resistance-sum`
- `paper-audit faradaic-efficiency`
- `paper-audit conductivity-geometry`
- `paper-audit tolerance-report`

`paper-audit demo` remains a compact human-readable smoke test.

## Recommended usage

- Use `text` for interactive terminal checks.
- Use `json` for scripts and downstream tools.
- Use `markdown` for technical notes and documentation.
- Use `csv` for row-level tabular exports.
