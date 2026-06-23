# Contributing Guidelines

Thank you for your interest in contributing to Academic Paper Data Consistency Audit. Contributions are welcome when they improve technical clarity, reproducibility, documentation quality, templates, synthetic examples, report workflows, or CLI behavior.

The project focuses on neutral technical clarification. It does not judge author intent and does not make ethical allegations.

---

## 1. Professional and Neutral Tone

The primary goal of this repository is to provide objective, physics-informed, and reproducible checks of data consistency and evidence-claim alignment.

Contributors should:

- focus on data, calculations, units, methods, evidence, and documentation
- distinguish observation, recalculation, and interpretation
- use neutral wording such as `requires clarification`, `appears to differ`, `reported value`, and `recalculated value`
- avoid intent-based claims or accusatory wording

Pull requests, issues, or examples that contain unsupported allegations or inflammatory language may be edited, closed, or rejected.

---

## 2. Good First Contributions

Useful first contributions include:

- documentation clarity improvements
- new synthetic case-study inputs
- expected CLI output examples
- tests for existing commands
- small CLI help-text improvements
- report configuration examples
- Markdown or JSON output examples

---

## 3. Issues

Use the issue templates under `.github/ISSUE_TEMPLATE/`:

- **Technical audit issue** — one locatable technical concern, one reproducible check, one neutral clarification request
- **Bug report** — code, CLI, test, or documentation problems
- **Feature request** — proposed checks, workflows, templates, or documentation improvements

For technical audit issues, follow the one-issue-per-comment principle:

1. exact location
2. factual observation
3. reproducible check
4. technical significance
5. clarification request

---

## 4. Case Studies and Examples

Synthetic examples are encouraged. They should be clearly marked as synthetic and should not include:

- real paper titles
- real author names
- real DOIs
- copyrighted publisher PDFs
- proprietary source data
- private personal information

A recommended case-study structure is:

```text
input.csv or evidence_table.md
commands.md
technical_issue.md
neutral_comment.md
```

For report-oriented examples, use:

```text
examples/report_config.json
examples/cli_output/report_output.md
```

---

## 5. Pull Request Process

1. Fork the repository or create a feature branch from `main`.
2. Keep each pull request focused on one purpose.
3. Add or update tests when changing code or CLI behavior.
4. Update documentation when changing user-facing behavior.
5. Run tests locally when possible:

```bash
pytest tests/
paper-audit demo
paper-audit report --config examples/report_config.json
```

6. Use the pull request template and complete the responsible-use checklist.

---

## 6. Development Setup

```bash
git clone https://github.com/YinBryn/academic-paper-data-consistency-audit.git
cd academic-paper-data-consistency-audit
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
pytest tests/
paper-audit demo
```

---

## 7. Adding or Changing CLI Commands

When adding a command or changing user-facing CLI behavior:

- keep the calculation logic reusable under `src/paper_audit/`
- add unit tests or CLI tests
- preserve default text output when possible
- add structured output support when it is useful
- update docs and expected output examples
- add CI smoke coverage after the command is stable

---

## 8. Responsible Use

See `docs/responsible_use.md` and `CODE_OF_CONDUCT.md` for project-wide expectations.
