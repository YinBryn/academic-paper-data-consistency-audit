# Limitations and Ethics

This document outlines the ethical boundaries, operational limitations, and responsible disclosure guidelines for users of the technical audit framework.

---

## 1. Ethical Boundaries

### 1.1. No Determination of Intent or Misconduct
*   **Rule**: The tools and methodologies in this project are strictly designed to evaluate **data consistency** and **calculation reproducibility**. They do not assess whether an identified discrepancy is the result of an honest human error, formatting issues during production, or academic misconduct.
*   **Action**: Auditors must never declare a paper as "fraudulent" or accuse authors of "misconduct." The findings must remain purely technical and objective.

### 1.2. Prioritizing Author Clarification
*   **Rule**: Authors should always be given the first opportunity to clarify any identified discrepancies.
*   **Action**: Inquiries should be sent to the corresponding author or the journal editor in a polite, non-confrontational manner. Public postings or public flags should be avoided unless the authors or journal refuse to engage or correct confirmed errors after a reasonable period (typically 30–60 days).

### 1.3. Avoid Public Accusations
*   **Rule**: Do not use public platforms to make sensationalized claims about audited papers.
*   **Rationale**: Public accusations can damage reputations prematurely, especially when discrepancies can be explained by simple typesetting errors or minor variations in experimental batches.

## 2. Technical Limitations

### 2.1. Dependency on Disclosed Information
*   This audit workflow is limited to the data published within the article, the supplementary files, and open source repositories.
*   If a paper fails to disclose key experimental parameters (e.g., cell thickness, exact active area, or raw impedance fit spectra), the audit may report the calculations as "unverifiable" rather than "incorrect."

### 2.2. Requirement for Expert Validation
*   The scripts and automated checks are diagnostic helpers. They do not replace expert human judgment.
*   All audit reports must be reviewed by a researcher with domain expertise in electrochemistry and materials science to ensure the scientific validity of the comments.

## 3. Data Protection and Copyright

### 3.1. Respecting Copyright and Intellectual Property
*   When extracting figures or text from articles, comply with copyright fair use guidelines.
*   Do not redistribute full-text PDFs of proprietary or paywalled articles alongside the audit reports.

### 3.2. Proprietary Source Data
*   If authors share raw spreadsheet data privately to help resolve an inquiry, do not share or publish this data publicly without their explicit written consent.
