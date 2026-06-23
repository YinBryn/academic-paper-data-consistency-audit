# Examples Gallery

This page collects the main synthetic examples and output references in one place.

## Quick demo

```bash
paper-audit demo
```

## Report example

| Resource | Purpose |
|---|---|
| `examples/report_config.json` | JSON configuration for a multi-check report |
| `examples/cli_output/report_output.md` | Representative Markdown report output |
| `docs/report_workflow.md` | Report documentation |

Run:

```bash
paper-audit report --config examples/report_config.json
```

## Command references

| Command | Reference |
|---|---|
| `paper-audit arrhenius` | `docs/cli_expected_outputs.md` |
| `paper-audit statistics` | `docs/cli_expected_outputs.md` |
| `paper-audit ratio` | `docs/cli_expected_outputs.md` |
| `paper-audit dimensional` | `docs/cli_expected_outputs.md` |
| `paper-audit tolerance-report` | `docs/cli_expected_outputs.md` |
| `paper-audit resistance-sum` | `docs/cli_expected_outputs.md` |
| `paper-audit faradaic-efficiency` | `docs/cli_expected_outputs.md` |
| `paper-audit conductivity-geometry` | `docs/cli_expected_outputs.md` |

## Synthetic case folders

| Folder | Focus |
|---|---|
| `case_studies/arrhenius_discrepancy/` | Arrhenius recalculation |
| `case_studies/ivp_consistency/` | `P = jV` relation |
| `case_studies/tolerance_report/` | Row-level tolerance report |
| `case_studies/resistance_component_sum/` | Component-sum check |
| `case_studies/faradaic_efficiency/` | Current and flow relation |
| `case_studies/conductivity_geometry/` | Conductivity geometry normalization |
| `case_studies/rp_table_figure_mismatch/` | Table and figure consistency pattern |
| `case_studies/evidence_claim_overreach/` | Evidence and claim alignment pattern |

## Recommended path

1. Run `paper-audit demo`.
2. Read `docs/tutorial_complete_workflow.md`.
3. Run one single command.
4. Run `paper-audit report --config examples/report_config.json`.
5. Review `examples/cli_output/report_output.md`.
