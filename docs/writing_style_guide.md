# Writing Style Guide

This document establishes the linguistic and stylistic standards for drafting technical comments, audit reports, and author inquiries. Adherence to this guide ensures that all communications are scientific, objective, and constructive.

---

## 1. Core Principles

### 1.1. Neutral Tone
*   **Guideline**: Describe data discrepancies and mathematical errors as facts without attributing intent. Use standard scientific vocabulary rather than emotive or critical language.
*   **Examples**:
    *   *Avoid*: "The authors fabricated the stability data because Figure 8 is obviously fake."
    *   *Use*: "The stability dataset in Figure 8 is presented up to 100 hours, whereas the main text asserts a testing duration of 1000 hours. Clarification is required to reconcile this discrepancy."

### 1.2. Specificity
*   **Guideline**: Pinpoint the exact location (page, column, figure, table, line) of the data being discussed, and provide the exact numbers.
*   **Examples**:
    *   *Avoid*: "The polarization resistance numbers do not match."
    *   *Use*: "The polarization resistance ($R_p$) of the MCO-10 cathode at $600^\circ\text{C}$ is reported as $0.22\ \Omega\ \text{cm}^2$ in Table S3, but appears as approximately $0.10\ \Omega\ \text{cm}^2$ in Figure 5."

### 1.3. Reproducibility
*   **Guideline**: Always disclose the exact equations, mathematical constants, and calculations used to verify a parameter. Anyone reading the audit report should be able to replicate the auditor's calculations.

## 2. Permitted and Prohibited Vocabulary

### 2.1. Prohibited Terms (Strong Allegations)
Do not use words that imply moral, ethical, or legal misconduct. The audit process focuses on data accuracy, not intent.
*   **Do not use**: *fraud*, *misconduct*, *fabrication*, *manipulation*, *falsified*, *deception*, *cheating*, *copy-paste*, *plagiarism*, *manipulated*.

### 2.2. Preferred Terms (Objective Science)
Use neutral descriptors that characterize the relationship between data points or statements.
*   **Use instead**: *data inconsistency*, *discrepancy*, *calculation mismatch*, *unreproducible*, *unresolved*, *requires clarification*, *appears to differ*, *overstatement*, *overgeneralized*.

## 3. Hedging and Scientific Caution
Since errors can sometimes arise from formatting, typesetting, or file truncation, always express findings with appropriate scientific caution.
*   Use terms like **"appears to"**, **"may indicate"**, **"suggests that"**, and **"requires clarification"** to avoid making absolute statements where minor formatting errors might be the cause.
*   **Example**: "The power density curve in Figure 4b appears to exceed the product of current density and voltage. This may stem from a scaling offset on the right y-axis or an area normalization discrepancy."
