# Commands

This case checks whether measured H2 flow is consistent with current and reported Faradaic efficiency.

For `Synthetic-Electrolyzer-A`:

```bash
paper-audit faradaic-efficiency \
  --current-density-a-cm2 0.5 \
  --area-cm2 1.0 \
  --measured-flow-ml-min 3.30 \
  --electrons-per-molecule 2 \
  --reported-fe-pct 95.0
```

For `Synthetic-Electrolyzer-B`:

```bash
paper-audit faradaic-efficiency \
  --current-density-a-cm2 0.5 \
  --area-cm2 1.0 \
  --measured-flow-ml-min 2.45 \
  --electrons-per-molecule 2 \
  --reported-fe-pct 95.0
```

Expected interpretation:

- `Synthetic-Electrolyzer-A`: calculated FE is approximately 94.7%, close to the reported 95.0%.
- `Synthetic-Electrolyzer-B`: calculated FE is approximately 70.3%, which differs from the reported 95.0%.
