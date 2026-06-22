# Demo Audit Report

**Project:** Academic Paper Data Consistency Audit  
**Demo Version:** v0.1.0-alpha  
**Data source:** `demo/demo_input.csv`

This demo uses synthetic data only. It is not based on any real paper, author, DOI, journal article, or publisher-provided data set.

---

## 1. Synthetic Input Data

| Sample | Temperature (°C) | Rp (Ω·cm²) |
|---|---:|---:|
| Example-A | 800 | 0.025 |
| Example-A | 750 | 0.052 |
| Example-A | 700 | 0.110 |
| Example-B | 800 | 0.018 |
| Example-B | 750 | 0.041 |
| Example-B | 700 | 0.090 |

---

## 2. Arrhenius Activation Energy Recalculation

The demo fits `ln(Rp)` against `1000/T` using the same convention implemented in `scripts/arrhenius_fit.py`.

| Sample | Input temperatures (°C) | Input Rp values (Ω·cm²) | Recalculated Ea (eV) | R² |
|---|---|---|---:|---:|
| Example-A | 800, 750, 700 | 0.025, 0.052, 0.110 | 1.333 | 0.9995 |
| Example-B | 800, 750, 700 | 0.018, 0.041, 0.090 | 1.447 | 0.9983 |

Example command:

```bash
python ../scripts/arrhenius_fit.py --temperature-c 800 750 700 --resistance 0.025 0.052 0.110
```

---

## 3. Relative Rp Comparison

Using Example-A as the baseline and Example-B as the modified case:

| Temperature (°C) | Baseline Rp: Example-A | Modified Rp: Example-B | Rp reduction (%) |
|---:|---:|---:|---:|
| 800 | 0.025 | 0.018 | 28.00 |
| 750 | 0.052 | 0.041 | 21.15 |
| 700 | 0.110 | 0.090 | 18.18 |

Example command:

```bash
python ../scripts/performance_ratio_check.py \
  --csv demo_input.csv \
  --baseline-sample Example-A \
  --new-sample Example-B \
  --column Rp_ohm_cm2
```

---

## 4. Neutral Technical Reporting Example

A suitable neutral observation would be:

> In the synthetic demo table, Example-B has lower Rp than Example-A at all three temperatures. Recalculation gives an Rp reduction of 28.00%, 21.15%, and 18.18% at 800, 750, and 700 °C, respectively. The Arrhenius fits yield Ea values of 1.333 eV for Example-A and 1.447 eV for Example-B. These values should be reported as recalculated quantities, not as evidence of author intent or misconduct.

---

## 5. Next Steps for Real Audits

1. Replace the synthetic values with numbers extracted from the manuscript, figures, tables, Supplementary Information, or source data.
2. Keep each technical concern as a single, locatable issue.
3. Show equations, inputs, and recalculated values so the check can be reproduced.
4. Use the neutral reporting template in `templates/pubpeer_style_issue_format.md`.
5. Follow the language guidance in `docs/language_safety.md` when communicating with authors, journals, or public post-publication review platforms.
