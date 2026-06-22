# Commands

This case checks whether a reported total Rp equals the sum of fitted or listed resistance components.

```bash
paper-audit resistance-sum \
  --reported-total 0.180 \
  --components 0.052 0.061 0.038 \
  --tolerance-pct 1.0
```

Expected interpretation:

- component sum = 0.151 Ω·cm²
- reported total = 0.180 Ω·cm²
- relative difference ≈ 19.2%
- outside a 1% tolerance
