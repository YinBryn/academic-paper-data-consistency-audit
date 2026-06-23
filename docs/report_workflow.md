# Report Workflow

`paper-audit report` builds a compact synthetic audit report from a JSON configuration file.

## Basic command

```bash
paper-audit report --config examples/report_config.json
```

The default output is Markdown.

```bash
paper-audit report \
  --config examples/report_config.json \
  --output markdown
```

JSON output is also available:

```bash
paper-audit report \
  --config examples/report_config.json \
  --output json
```

## Configuration format

A report configuration contains a title, description, and a list of checks:

```json
{
  "title": "Synthetic Audit Report",
  "description": "A compact report generated from synthetic checks.",
  "checks": [
    {
      "id": "ivp_consistency",
      "type": "dimensional",
      "title": "I-V-P consistency",
      "params": {
        "power_density": 2.6,
        "current_density": 2.0,
        "voltage": 1.3,
        "tolerance_pct": 1.0
      }
    }
  ]
}
```

## Supported check types

- `arrhenius`
- `statistics`
- `ratio`
- `dimensional`
- `resistance-sum`
- `faradaic-efficiency`
- `conductivity-geometry`
- `tolerance-report`

## Report statuses

| Status | Meaning |
|---|---|
| `PASS` | The configured numerical comparison is within tolerance |
| `FLAG` | The configured numerical comparison is outside tolerance |
| `INFO` | The check produces a calculated value but does not define a pass/fail threshold |

These statuses are workflow labels only. They are not severity labels.

## Recommended workflow

1. Put all values into a JSON configuration file.
2. Run `paper-audit report --config ...`.
3. Save the Markdown or JSON output.
4. Use the report as a reproducible calculation record.
5. Keep public examples synthetic and neutral.

## Example output

A representative output file is available at:

```text
examples/cli_output/report_output.md
```
