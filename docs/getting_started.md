# Getting Started

This page shows the minimum steps needed to run the toolkit locally.

## 1. Clone the repository

```bash
git clone https://github.com/YinBryn/academic-paper-data-consistency-audit.git
cd academic-paper-data-consistency-audit
```

## 2. Create an environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

## 3. Install dependencies and CLI

```bash
pip install -r requirements.txt
pip install -e .
```

## 4. Run the CLI

```bash
paper-audit --help
paper-audit demo
```

The `demo` command runs a compact synthetic smoke test across representative checks. It is the fastest way to confirm that the installed CLI is working.

Available subcommands:

| Command | Purpose |
|---|---|
| `paper-audit demo` | Run a one-command synthetic smoke test |
| `paper-audit arrhenius` | Fit Arrhenius data and report activation energy |
| `paper-audit statistics` | Recalculate mean and standard deviation |
| `paper-audit ratio` | Calculate improvement or reduction ratios |
| `paper-audit dimensional` | Check dimensional and `P = j × V` consistency |
| `paper-audit tolerance-report` | Batch compare reported values against source/reference values |
| `paper-audit resistance-sum` | Check whether total Rp/ASR equals the sum of listed components |
| `paper-audit faradaic-efficiency` | Calculate gas-flow-based Faradaic efficiency from current |
| `paper-audit conductivity-geometry` | Calculate conductivity from resistance, thickness, and area |

## 5. Run tests

```bash
pytest tests/
```

## Example: one-command demo

```bash
paper-audit demo
```

Expected interpretation: the demo runs representative checks using synthetic values only and prints a compact pass-style smoke-test report.

## Example

```bash
paper-audit dimensional \
  --power-density 2.6 \
  --current-density 2.0 \
  --voltage 1.3
```

Expected interpretation: if the reported power density equals `current density × voltage` within tolerance, the relation is numerically consistent.

## Example: tolerance report

```bash
paper-audit tolerance-report \
  --csv case_studies/tolerance_report/input.csv \
  --reported-column reported_Rp_ohm_cm2 \
  --reference-column source_Rp_ohm_cm2 \
  --id-column sample \
  --tolerance-pct 5.0
```

Expected interpretation: each row is marked as within or outside the selected relative tolerance.

## Example: resistance component-sum check

```bash
paper-audit resistance-sum \
  --reported-total 0.180 \
  --components 0.052 0.061 0.038
```

Expected interpretation: if the reported total equals the sum of listed components within tolerance, the component-sum relation is numerically consistent.

## Example: Faradaic efficiency check

```bash
paper-audit faradaic-efficiency \
  --current-density-a-cm2 0.5 \
  --area-cm2 1.0 \
  --measured-flow-ml-min 3.30 \
  --electrons-per-molecule 2 \
  --reported-fe-pct 95.0
```

Expected interpretation: the measured product-gas flow is converted into a calculated Faradaic efficiency and compared with the reported value when provided.

## Example: conductivity geometry check

```bash
paper-audit conductivity-geometry \
  --resistance-ohm 10.0 \
  --thickness-mm 0.33 \
  --diameter-mm 6.0 \
  --reported-conductivity-s-cm 0.01167
```

Expected interpretation: conductivity is recalculated from resistance, thickness, and area, then compared with the reported value when provided.
