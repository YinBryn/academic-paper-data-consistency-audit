# Commands

This case demonstrates a recalculation of activation energy from synthetic Rp data.

```bash
paper-audit arrhenius \
  --temperature-c 800 750 700 \
  --resistance 0.022 0.053 0.103
```

Expected key output:

```text
Ea: approximately 1.33 eV
```

The synthetic reported value in `input.csv` is 0.85 eV, so the recalculated value is materially different from the reported value.
