# Commands

This case demonstrates a direct physical consistency check using:

```text
P = j × V
```

For `Synthetic-Cell-A`:

```bash
paper-audit dimensional \
  --power-density 0.95 \
  --current-density 1.50 \
  --voltage 0.63
```

For `Synthetic-Cell-B`:

```bash
paper-audit dimensional \
  --power-density 1.10 \
  --current-density 2.00 \
  --voltage 0.70
```

Expected interpretation:

- `Synthetic-Cell-A`: calculated power density = 0.945 W/cm², close to 0.95 W/cm².
- `Synthetic-Cell-B`: calculated power density = 1.40 W/cm², which differs from the reported 1.10 W/cm².
