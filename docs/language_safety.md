# Language Safety Guidelines

This document outlines the strict linguistic and stylistic rules that all auditors and contributors must follow when drafting technical comments, reviews, or inquiries. Adhering to these rules ensures that our findings are framed scientifically, legally, and ethically.

---

## 1. Prohibited Terms and Absolute Statements

We focus entirely on the **physical data** and **mathematical calculations**. We do not make assumptions about why an error occurred, nor do we accuse authors of dishonesty.

### 1.1. Absolute Prohibitions
Unless officially established by an institutional investigation or formal retraction notice, the following words and their synonyms are **strictly prohibited** in all reports and issues:
*   *Accusatory nouns*: **fraud**, **misconduct**, **fabrication**, **manipulation**, **plagiarism**, **falsification**, **deception**, **cheating**, **scam**.
*   *Accusatory verbs/adjectives*: **manipulated**, **fabricated**, **falsified**, **forged**, **tampered**, **doctored**, **fake**, **copied and pasted**.

### 1.2. The Danger of Inferring Author Intent
*   **Rule**: Never attempt to explain *why* the authors presented inconsistent data (e.g., "to make the cell performance look better").
*   **Action**: Describe only *what* is written and *what* the calculation shows.
*   *Avoid*: "The authors changed the activation energy in Figure 6 to match their DFT predictions."
*   *Use*: "The reported activation energy of $0.85\ \text{eV}$ in Figure 6 differs from the recalculated value of $1.01\ \text{eV}$ obtained from the data in Table S3. Clarification is requested to understand this difference."

## 2. Standard Hedging Vocabulary

Because typesetting, formatting, conversion, and rounding errors are common in publication pipelines, always state observations with appropriate scientific caution. Use the following phrases:

*   **"appears to"** or **"seems to"**:  
    *   *Example*: "Figure 3a and Figure 3b appear to display the same dataset under different labels."
*   **"difficult to reconcile"**:  
    *   *Example*: "The text assertion of $1.15\ \text{W}\ \text{cm}^{-2}$ is difficult to reconcile with the plotted peak of $0.95\ \text{W}\ \text{cm}^{-2}$ in Figure 4."
*   **"requires clarification"**:  
    *   *Example*: "The calculation of the chemical diffusion coefficient requires clarification regarding the cell thickness parameter used."
*   **"may indicate"**:  
    *   *Example*: "The overlapping coordinates may indicate a minor file duplication error."

## 3. Distinguishing Observation, Recalculation, and Interpretation

To maintain credibility, clearly separate objective observations from mathematical checks and interpretation.

| Stage | Objective | Language Example |
| :--- | :--- | :--- |
| **Observation** | State facts exactly as printed in the paper. | "Table 1 lists value A; Figure 2 plots value B." |
| **Recalculation** | State the math and equations used. | "Using equation (3) and the raw values in Table 1, the calculated value is C." |
| **Interpretation** | Explain the technical effect, not the intent. | "This discrepancy affects the input boundaries for secondary modeling." |

## 4. Checklist for Reviewing Comments Before Posting

Before submitting a technical comment or audit report, ask the following questions:
1.  Are there any accusatory words in the text? (If yes, delete or rephrase).
2.  Did I attribute any intent, motive, or state of mind to the authors? (If yes, delete).
3.  Are all equations, parameters, and numbers cited exactly from the paper? (If no, correct).
4.  Can another researcher replicate my recalculation using only the text and my comment? (If no, add more details).
5.  Is the tone polite, professional, and focused on scientific clarity? (If no, adjust).
