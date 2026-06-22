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
```

Available subcommands:

| Command | Purpose |
|---|---|
| `paper-audit arrhenius` | Fit Arrhenius data and report activation energy |
| `paper-audit statistics` | Recalculate mean and standard deviation |
| `paper-audit ratio` | Calculate improvement or reduction ratios |
| `paper-audit dimensional` | Check dimensional and `P = j × V` consistency |

## 5. Run tests

```bash
pytest tests/
```

## Example

```bash
paper-audit dimensional \
  --power-density 2.6 \
  --current-density 2.0 \
  --voltage 1.3
```

Expected interpretation: if the reported power density equals `current density × voltage` within tolerance, the relation is numerically consistent.
