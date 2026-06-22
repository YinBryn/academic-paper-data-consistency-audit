# Commands

This case checks whether reported conductivity is consistent with resistance, sample thickness, and circular sample diameter.

For `Synthetic-Electrolyte-A`:

```bash
paper-audit conductivity-geometry \
  --resistance-ohm 10.0 \
  --thickness-mm 0.33 \
  --diameter-mm 6.0 \
  --reported-conductivity-s-cm 0.01167
```

For `Synthetic-Electrolyte-B`:

```bash
paper-audit conductivity-geometry \
  --resistance-ohm 10.0 \
  --thickness-mm 0.33 \
  --diameter-mm 6.0 \
  --reported-conductivity-s-cm 0.02000
```

Expected interpretation:

- calculated conductivity is approximately 0.01167 S/cm
- `Synthetic-Electrolyte-A` is consistent with the reported value
- `Synthetic-Electrolyte-B` differs from the calculated value
