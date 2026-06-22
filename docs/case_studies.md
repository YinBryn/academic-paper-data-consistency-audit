# Synthetic Case Studies

The case studies are fully synthetic. They are designed for training, demonstration, and reproducible workflow development.

No real paper, author, DOI, journal, or publisher-provided data set is included.

## Available cases

| Case | Focus | Use it to learn |
|---|---|---|
| `arrhenius_discrepancy/` | Activation-energy recalculation | how to report an Ea mismatch neutrally |
| `ivp_consistency/` | `P = j × V` consistency | how to check current-density, voltage, and power-density values |
| `rp_table_figure_mismatch/` | Figure/table/source-data consistency | how to isolate one numerical discrepancy |
| `evidence_claim_overreach/` | Evidence-claim alignment | how to narrow a mechanistic claim to what the data support |

## Recommended case-study structure

Each case should include:

```text
input.csv or evidence_table.md
commands.md
technical_issue.md
neutral_comment.md
```

## Writing rule

A case study should not imply author intent. It should only show:

1. where the value or claim appears
2. what was extracted
3. what was recalculated or compared
4. why the point matters technically
5. what clarification is requested
