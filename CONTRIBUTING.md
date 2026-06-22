# Contributing Guidelines

Thank you for your interest in contributing to the Academic Paper Data Consistency Audit project! We welcome contributions that improve our audit methodologies, expand templates, add python script validations, or correct documentation.

To maintain the scientific integrity and constructive nature of this project, all contributors must strictly adhere to the guidelines below.

---

## 1. Professional and Neutral Tone (Strict Requirement)

The primary goal of this repository is to provide **objective, physics-informed, and data-driven reviews** of published materials electrochemistry research. We focus exclusively on verifying data consistency and calculation reproducibility.

*   **No Accusatory Language**: We do not judge the authors' intent or make ethical/moral allegations.
*   **Prohibited Terms**: Do not use qualitative or accusatory terms such as **"fraud"**, **"misconduct"**, **"fabrication"**, **"falsified"**, **"manipulation"**, **"plagiarism"**, **"cheating"**, or similar qualitative labels.
*   **Preferred Terms**: Describe discrepancies using neutral, factual terms: **"data inconsistency"**, **"unreproducible calculation"**, **"discrepancy"**, **"requires clarification"**, **"appears to differ"**, **"overgeneralized claim"**.

Any pull requests, issue logs, or templates containing accusatory or qualitative allegations will be rejected immediately.

## 2. Issue Logs and Case Studies

When documenting or contributing issues, logs, or case studies (e.g., in templates or anonymized case files):
*   **Locatable**: Pinpoint the exact location of the issue (e.g., page number, column, paragraph, figure, or table).
*   **Evidenced**: Clearly state what the reported values are and what discrepancies you observed.
*   **Reproducible**: Provide the exact equations, constants, and raw values used. If you performed a recalculation, show the code or mathematical steps so others can reproduce your findings.
*   **Anonymized**: Do not post real DOIs, real authors, or real paper titles in general example folders. Use mock numbers and anonymized names (e.g., "MCO-10 cathode") to illustrate technical concepts.

## 3. Pull Request Process

1.  Fork the repository and create your branch from `main`.
2.  If you are contributing Python scripts under `scripts/`, ensure you write corresponding unit tests under `tests/`.
3.  Verify that all tests pass locally by running:
    ```bash
    pytest tests/
    ```
4.  Ensure your code conforms to PEP 8 standards and is cleanly documented.
5.  Submit a Pull Request describing your changes. Ensure the PR title and description strictly follow the neutral writing style guide.
