# Evidence-Claim Alignment Checks (Category IV)

This document provides a framework for auditing the alignment between the empirical evidence presented in a paper and the qualitative, mechanistic, or performance claims asserted in the text.

---

## 1. Claims Supported by Direct Data
*   **Definition**: Claims that are directly measured or verified through primary experimental characterization techniques.
*   **Audit Procedure**:
    *   Identify claims that state specific values or direct observations (e.g., "The XRD pattern confirms the formation of a single-phase cubic perovskite structure").
    *   Verify that the corresponding figure (e.g., the XRD pattern) contains all necessary reference peaks, is free of unindexed secondary phase peaks, and is clearly resolved.
    *   Ensure that the direct data supports the exact sample being discussed under the specified conditions.

## 2. Claims Supported by Indirect Inference
*   **Definition**: Claims that cannot be measured directly but are inferred from a combination of secondary data and physical models (e.g., inferring a change in the rate-determining step of an oxygen reduction reaction from changes in the slope of polarization resistance vs. oxygen partial pressure).
*   **Audit Procedure**:
    *   Evaluate the logical link between the measurement and the inference.
    *   Check whether alternative explanations or competing mechanisms have been discussed and ruled out.
    *   Verify that the model used for inference (e.g., equivalent circuit fitting) is physically valid for the system under study and that the fit quality is sufficient to support the inference.

## 3. Claims Requiring Additional Evidence
*   **Definition**: Assertions made in the text that are presented as established facts but lack sufficient experimental or computational proof in the manuscript or supplementary files.
*   **Audit Procedure**:
    *   Look for statements that assert structural or chemical changes during operation (e.g., "The dopant segregates to the surface to form catalytically active nanoparticles during testing") without accompanying post-mortem characterization (e.g., TEM, XPS after operation).
    *   Flag qualitative statements such as "the sample exhibited excellent long-term stability" when the stability test data is limited to a very short duration (e.g., less than 20 hours).

## 4. Overgeneralized Claims
*   **Definition**: Claims that extrapolate a specific local trend or performance metric to a much broader range of materials, operating conditions, or applications.
*   **Audit Procedure**:
    *   Compare the range of conditions tested (e.g., temperature range, partial pressure range, composition space) with the range claimed in the conclusions (e.g., "This cathode material is suitable for all intermediate-temperature solid oxide fuel cells").
    *   Check if a material is claimed to perform better than a state-of-the-art benchmark based on a comparison under non-standard or unequal testing conditions (e.g., comparing a thin-film electrolyte cell with a thick electrolyte baseline).

## 5. Mechanistic Claims Based Only on Fitting or Simulation
*   **Definition**: Proposing a detailed atomic or molecular mechanism based solely on equivalent circuit modeling or density functional theory (DFT) calculations, without direct experimental validation.
*   **Audit Procedure**:
    *   Identify claims proposing specific reaction pathways, charge transport paths, or active sites.
    *   Check if the authors present these findings as definitive experimental proof (e.g., "DFT calculations prove that oxygen vacancies migrate along the A-site path") rather than computational predictions.
    *   Ensure that the limitations of the fit or calculation (e.g., idealized crystal models, simplified gas atmospheres, non-uniqueness of equivalent circuit models) are disclosed and that the language reflects these limitations (e.g., using terms like "suggests", "is consistent with", "is supported by the computational model").
