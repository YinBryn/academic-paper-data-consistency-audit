# Data Consistency Checks (Category I)

This document provides guidelines for auditing core data inconsistencies across figures, tables, main text, and supplementary information.

---

## 1. Figure vs. Table Comparison
*   **Audit Procedure**: Identify key performance parameters (e.g., peak power density, polarization resistance, conductivity, overpotential) presented in figures, and cross-reference them with the corresponding values reported in tables.
*   **Key Checks**:
    *   Compare the coordinates of data points in plots (using digital digitizers if necessary) with the numerical values tabulated in the main text or SI.
    *   Verify that error bars shown in figures match the standard deviation values listed in the tables.
    *   Ensure that the temperature, atmosphere, and bias voltage parameters match exactly between the plot legends and table headers.

## 2. Main Text vs. Supplementary Information (SI)
*   **Audit Procedure**: Perform a systematic comparison of data statements in the main text with the raw datasets or supplementary figures/tables in the SI.
*   **Key Checks**:
    *   Check if values highlighted in the Abstract or Introduction (e.g., "ASR of $0.1\ \Omega\ \text{cm}^2$ at $600^\circ\text{C}$") are supported by the actual datasets presented in the SI.
    *   Confirm that supplementary figures referenced in the main text actually contain the discussed data and trends.
    *   Check for discrepancies in operating conditions (e.g., fuel flow rates, gas composition, cell active area) reported in the main text Experimental section versus the SI captions.

## 3. Source Data vs. Plotted Data
*   **Audit Procedure**: When raw source data (e.g., Excel, CSV files) is provided by the authors or publisher, map the raw numerical values directly to the plotted coordinates.
*   **Key Checks**:
    *   Verify that no data points have been selectively omitted or filtered out from the plot without scientific justification (e.g., removing low-performance outliers to artificially reduce standard deviation).
    *   Check that the mathematical transformation applied to raw data (e.g., normalizing current by cell area, converting resistance to area-specific resistance) is consistent across all data points.

## 4. Sample Naming Consistency
*   **Audit Procedure**: Track the naming conventions of all control and modified samples throughout the manuscript, figures, tables, and SI.
*   **Key Checks**:
    *   Confirm that shorthand sample labels (e.g., "LSCF-10", "LSCF-20", "Modified-Cell") refer to the exact same chemical compositions and cell configurations in all figures and tables.
    *   Verify that sample identifiers do not shift or switch roles between different characterization techniques (e.g., a sample labeled as "high-performance" in electrochemical tests should not match the characterization data of a "baseline" sample in XRD/SEM analysis).

## 5. Units and Axis Labels
*   **Audit Procedure**: Audit all figure axes, table columns, and text descriptions to ensure correct physical units and axis scaling.
*   **Key Checks**:
    *   Check for mathematical consistency in scaled units (e.g., milli- versus micro-, $\text{mA}\ \text{cm}^{-2}$ versus $\text{A}\ \text{cm}^{-2}$).
    *   Ensure axis labels match the physical quantity being discussed (e.g., plotting "Impedance" but labeling the axis as "Resistance", or plotting "Conductivity" with units of resistance).
    *   Verify that normalization factors (e.g., active area, weight, volume) are explicitly defined and consistently applied to the units.

## 6. Repeated or Conflicting Values
*   **Audit Procedure**: Scan the document for identical numerical values or identical plot curves representing different conditions, as well as conflicting statements.
*   **Key Checks**:
    *   Verify that noise patterns, experimental fluctuations, or baseline offsets in electrochemical curves (e.g., Nyquist plots, CV curves) are not identical across supposedly independent samples or different temperatures.
    *   Check if the text makes contradictory statements regarding the same data point (e.g., claiming a degradation rate of "0.5% per 100 hours" in one section, but "5% per 100 hours" in another).
