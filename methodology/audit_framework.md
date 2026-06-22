# Technical Audit Framework

This document outlines the structured technical audit framework for published materials electrochemistry papers. The audit is designed to assess data consistency, calculation reproducibility, physical feasibility, and claim-evidence alignment in a rigorous, objective, and non-accusatory manner.

Findings are classified into four hierarchical categories.

---

## Category I: Core Data Inconsistencies
This category covers direct discrepancies in data presentation across different sections of a paper.
*   **Definition**: Contradictions between figures, tables, text, supplementary information (SI), or raw data files where the same sample under identical conditions is described with different values.
*   **Audit Scope**:
    *   Numerical values of key properties (e.g., polarization resistance $R_p$, conductivity, peak power density) mismatching between text and tables.
    *   Discrepancies in sample naming or labeling across figures and supplementary tables.
    *   Repeated use of the same data plot representing different samples or experimental conditions without disclosure.

## Category II: Calculation Reproducibility
This category assesses whether reported secondary (derived) physical quantities can be mathematically reproduced using the disclosed primary data and equations.
*   **Definition**: Discrepancies between the reported calculated values (e.g., activation energy $E_a$, standard deviations, improvement ratios) and the values obtained by independent recalculation using the same input data.
*   **Audit Scope**:
    *   Arrhenius fitting slope and corresponding activation energy values.
    *   Statistical metrics (mean, standard deviation, error bars) recalculation from source datasets.
    *   Reported improvement percentages or ratios compared to control/baseline samples.
    *   Completeness of disclosed equations, constants, and fitting parameters.

## Category III: Physical Reasonableness and Disclosure
This category evaluates the physical feasibility of the reported parameters under the laws of electrochemistry and thermodynamics, alongside the disclosure of key input boundaries.
*   **Definition**: Scientific anomalies where values or trends violate physical constraints, conservation laws, or fall outside established physical ranges without adequate scientific explanation.
*   **Audit Scope**:
    *   Dimensional analysis and unit consistency across axes, equations, and tables.
    *   Current–voltage–power density relationship consistency ($P = I \times V$).
    *   Conservation of mass and charge under high-rate or long-term operations.
    *   Apparent diffusion coefficients ($D_{app}$) and transport parameters falling into physically implausible regimes.
    *   Electrochemical Impedance Spectroscopy (EIS) equivalent circuit modeling parameters matching the physical geometry and dimensions of the cell.

## Category IV: Evidence–Claim Alignment
This category examines whether the qualitative and mechanistic claims asserted in the paper are fully supported by the provided experimental or computational data.
*   **Definition**: Mismatch between the strength of the qualitative assertions made in the text (e.g., abstract, conclusions) and the actual resolution or scope of the evidence presented.
*   **Audit Scope**:
    *   Mechanistic claims (e.g., "rate-determining step shift") stated as fact when only indirect, non-exclusive evidence is provided.
    *   Overgeneralizations of material performance across wide temperature or voltage ranges where data was only collected at limited points.
    *   Assertions of enhanced phase stability or structural integrity based purely on simulations or fittings without post-mortem experimental validation.
