# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] - 2026-06-22

### Added
*   Initial project scaffold for materials electrochemistry paper technical auditing.
*   Structured methodology guidelines for 4-tier audit framework (`methodology/`):
    *   `audit_framework.md` (General 4-tier classifications)
    *   `data_consistency_checks.md` (Category I checks)
    *   `reproducibility_checks.md` (Category II checks)
    *   `physics_consistency_checks.md` (Category III checks)
    *   `evidence_claim_alignment.md` (Category IV checks)
*   Standard templates for report compilation (`templates/`):
    *   `technical_audit_report_template.md` (Complete audit report layout)
    *   `editor_technical_comment_template.md` (Neutral inquiry letter to journal editors)
    *   `issue_log_template.md` (Tabular concern tracker)
    *   `pubpeer_style_issue_format.md` (Single-issue neutral technical comment format)
*   Four diagnostic Python scripts (`scripts/`):
    *   `arrhenius_fit.py` (ASR/Rp Arrhenius slope & Ea solver)
    *   `statistics_check.py` (Independent mean and std-dev verification)
    *   `performance_ratio_check.py` (Batch comparison of baseline vs modified cell)
    *   `dimensional_check.py` (Unit validation & I-V-P product check)
*   Synthetic demo materials under `demo/`.
*   Reference unit test suite with 12 passing tests (`tests/`).
*   GitHub Actions CI workflow for test automation on push/pull_request.
*   Citation metadata file (`CITATION.cff`) for software citation.
*   Short public project announcement draft under `docs/project_announcement.md`.

### Fixed
*   Aligned the synthetic demo report with `demo/demo_input.csv` so the reported temperatures, Rp values, Arrhenius results, and comparison table use the same source data.
