# Evidence Levels in Technical Auditing

To maintain objective and structured technical comments, all identified concerns are classified into five distinct Levels of Evidence. This classification helps differentiate between clear, incontrovertible errors and open scientific discussions.

---

## Level 1 (L1): Direct Numerical Inconsistency
*   **Definition**: Incontrovertible discrepancies where identical parameters or data points representing the same sample under the same conditions are described with conflicting values in different parts of the publication.
*   **Characteristics**:
    *   Factual and mathematical contradictions that do not depend on interpretation or modeling assumptions.
    *   *Examples*: A value in Table 1 is different from the plotted point in Figure 3; main text text claims a value of $0.15\ \Omega\ \text{cm}^2$ while Figure 4 lists it as $0.25\ \Omega\ \text{cm}^2$.

## Level 2 (L2): Recalculation Discrepancy
*   **Definition**: Discrepancies between reported derived parameters and values calculated independently using the published equations and raw data.
*   **Characteristics**:
    *   The raw data is present and clear, but the mathematical operation used to obtain the final parameter appears to contain an error or remains unexplained.
    *   *Examples*: The slope of $\ln(\sigma T)$ vs $1000/T$ yields $1.01\ \text{eV}$ upon recalculation, but the paper reports $0.85\ \text{eV}$; the standard deviation plotted as error bars does not match the sample standard deviation calculated from the raw dataset.

## Level 3 (L3): Dimensional or Physical-Unit Issue
*   **Definition**: Technical anomalies where the reported units are mathematically inconsistent, dimensionally incorrect, or physically implausible for the system under study.
*   **Characteristics**:
    *   Incorrect axis scaling or labeling errors that violate dimensional analysis.
    *   *Examples*: Reporting a chemical diffusion coefficient ($D_{chem}$) in units of $\text{cm}\ \text{s}^{-1}$ (velocity) rather than $\text{cm}^2\ \text{s}^{-1}$ (area-rate); polarization curves where current-voltage product ($I \times V$) does not equal the co-plotted power density.

## Level 4 (L4): Evidence–Claim Overextension
*   **Definition**: Qualitative or mechanistic assertions made in the text that exceed the resolution, duration, or scope of the provided empirical data.
*   **Characteristics**:
    *   The qualitative conclusions overshoot the experimental limits or rely on non-exclusive assumptions.
    *   *Examples*: Claiming "excellent long-term stability" when the presented stability test only lasted 50 hours; claiming a specific "rate-determining step shift" based purely on equivalent circuit fit results without physical, chemical, or isotopic validation.

## Level 5 (L5): Hypothesis or Concern Requiring Additional Data
*   **Definition**: Open scientific inquiries where the presented data is self-consistent and mathematically correct, but further experimental parameters or raw datasets are necessary to fully verify the physical feasibility of the claims.
*   **Characteristics**:
    *   Requires author clarification regarding experimental setup, modeling boundary conditions, or missing inputs.
    *   *Examples*: Evaluating whether equivalent circuit models represent the physical geometry of the cell (requiring disclosure of electrode thicknesses and local porosities); assessing charge conservation under high fuel utilization without feed flow rate disclosures.
