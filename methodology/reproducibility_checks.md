# Calculation Reproducibility Checks (Category II)

This document describes the procedures for verifying the mathematical reproducibility of derived parameters and calculations reported in materials electrochemistry papers.

---

## 1. Arrhenius Fitting and Activation Energy Calculation
*   **Physical Principle**: Temperature-dependent properties (such as conductivity $\sigma$ or polarization resistance $R_p$) typically follow the Arrhenius relationship:
    $$\ln(\sigma T) = \ln(A) - \frac{E_a}{k_B T} \quad \text{or} \quad \ln\left(\frac{1}{R_p}\right) = \ln(A') - \frac{E_a}{k_B T}$$
    where $E_a$ is the activation energy, $k_B$ is the Boltzmann constant ($8.6173 \times 10^{-5}\ \text{eV}\ \text{K}^{-1}$), $T$ is the absolute temperature in Kelvin, and $A$ ($A'$) is the pre-exponential factor.
*   **Audit Procedure**:
    1.  Extract the reported temperature values (converted from Celsius to Kelvin: $T(K) = T(^\circ\text{C}) + 273.15$) and corresponding physical values ($\sigma$ or $R_p$).
    2.  Plot $\ln(\sigma T)$ or $\ln(1/R_p)$ against $1000/T$.
    3.  Perform a linear regression: $y = m x + c$, where $y = \ln(\sigma T)$ and $x = 1000/T$.
    4.  Calculate the activation energy: $E_a (\text{eV}) = -m \times 1000 \times k_B = -m \times 0.086173$.
    5.  Compare the calculated $E_a$ and the coefficient of determination ($R^2$) with the reported values in the paper.

## 2. Mean and Standard Deviation Recalculation
*   **Mathematical Formulas**:
    *   Sample Mean: $\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i$
    *   Sample Standard Deviation: $s = \sqrt{\frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2}$
*   **Audit Procedure**:
    1.  Where raw data points or replicates are available, recalculate the mean and sample standard deviation.
    2.  Check if the paper has mistakenly reported the population standard deviation ($\sigma_{pop}$, denominator $n$) instead of the sample standard deviation ($s$, denominator $n-1$), which is standard for experimental replicates.
    3.  Verify that error bar values represented in figures correspond exactly to the calculated standard deviations or standard errors, rather than arbitrary percentages.

## 3. Performance Improvement Ratio Recalculation
*   **Audit Formula**:
    $$\text{Improvement Ratio} = \frac{X_{\text{new}} - X_{\text{baseline}}}{X_{\text{baseline}}} \times 100\%$$
    or
    $$\text{Reduction Ratio} = \frac{R_{\text{baseline}} - R_{\text{new}}}{R_{\text{baseline}}} \times 100\%$$
*   **Audit Procedure**:
    1.  Locate the reported baseline value (e.g., peak power density of a standard cell) and the improved value (e.g., peak power density of the modified cell).
    2.  Recalculate the percentage improvement or resistance reduction.
    3.  Verify whether statements in the text (e.g., "showed a 3-fold increase" or "decreased by 80%") are numerically accurate and mathematically consistent with the data in the figures and tables.

## 4. Resistance Component Summation
*   **Physical Principle**: For an electrochemical cell, the total area-specific resistance ($ASR_{total}$ or $R_{total}$) is the sum of the ohmic resistance ($R_o$) and the polarization resistance ($R_p$):
    $$R_{total} = R_o + R_p$$
    If $R_p$ is resolved into high-frequency ($R_{HF}$) and low-frequency ($R_{LF}$) components via equivalent circuit fitting:
    $$R_p = R_{HF} + R_{LF}$$
*   **Audit Procedure**:
    1.  Verify that the sum of the individual fitted resistance components matches the total polarization resistance reported in the text and tables.
    2.  Cross-reference these sums with the intercepts on the real axis ($Z'$) of the corresponding Nyquist plots. The high-frequency intercept should equal $R_o$, and the low-frequency intercept should equal $R_o + R_p$.

## 5. Fitting Parameter Disclosure
*   **Audit Procedure**: Review the experimental and supplementary sections for the disclosure of fitting parameters (e.g., equivalent circuit model configuration, initial guess values, boundaries, and goodness-of-fit indicators like $\chi^2$ or weighted sum of squares).
*   **Key Checks**:
    *   Verify if the equivalent circuit model (e.g., $R_o(R_{HF}CPE_{HF})(R_{LF}CPE_{LF})$) is clearly defined.
    *   Check if all fitting values (resistance, capacitance, constant phase element exponent $n$) are provided in a table. Missing exponents or constant phase parameters render the impedance fitting unreproducible.
