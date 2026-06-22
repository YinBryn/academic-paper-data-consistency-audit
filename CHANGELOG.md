# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project follows Semantic Versioning during alpha development.

---

## [0.10.0-alpha] - 2026-06-22

### Added
*   Installable `paper-audit` CLI package.
*   CLI subcommands:
    *   `paper-audit arrhenius`
    *   `paper-audit statistics`
    *   `paper-audit ratio`
    *   `paper-audit dimensional`
    *   `paper-audit tolerance-report`
    *   `paper-audit resistance-sum`
    *   `paper-audit faradaic-efficiency`
    *   `paper-audit conductivity-geometry`
*   Reusable package-level checks under `src/paper_audit/`.
*   Batch reported-value/source-data tolerance report workflow.
*   Rp/ASR component-sum consistency check.
*   Faradaic-efficiency and gas-production consistency check.
*   Conductivity geometry-normalization check.
*   Synthetic case-study suite under `case_studies/`.
*   Representative CLI output examples under `examples/cli_output/`.
*   GitHub Pages documentation foundation under `docs/`.
*   Community health files and contribution templates:
    *   issue templates
    *   pull request template
    *   `CONTRIBUTING.md`
    *   `CODE_OF_CONDUCT.md`
    *   `SECURITY.md`
*   Citation metadata via `CITATION.cff`.
*   GitHub Actions CI for Python 3.10 and 3.11.

### Changed
*   README now presents the project as a reusable scientific audit toolkit.
*   Documentation now includes getting-started, workflow, responsible-use, roadmap, and release-checklist pages.
*   Synthetic examples are explicitly marked as synthetic and separated from real paper data.

### Fixed
*   Aligned synthetic demo report values with source CSV data.
*   Corrected conductivity-geometry test expectations for circular-sample area normalization.

---

## [0.1.0] - 2026-06-22

### Added
*   Initial project scaffold for materials electrochemistry paper technical auditing.
*   Structured methodology guidelines for 4-tier audit framework (`methodology/`).
*   Standard templates for report compilation (`templates/`).
*   Initial diagnostic Python scripts under `scripts/`.
*   Synthetic demo materials under `demo/`.
*   Reference unit test suite.
*   GitHub Actions CI workflow.
