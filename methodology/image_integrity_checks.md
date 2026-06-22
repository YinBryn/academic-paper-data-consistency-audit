# Image Integrity Checks in Materials Electrochemistry

This document outlines standard, objective screening procedures for evaluating the integrity of images (such as SEM, TEM, XRD patterns, and optical micrographs) in published scientific articles.

> [!IMPORTANT]
> **Core Policy**: Image observations and findings identified during these checks are **screening signals** and **clarification requests**, **never proof of academic misconduct or fabrication**. 
> Image anomalies can frequently result from compression artifacts, formatting errors, file conversion issues, or template mismatches. All comments must be framed as requests for clarification or source file disclosures in a neutral, non-confrontational tone.

---

## 1. Duplicated Panels and Plots
*   **Definition**: The same image panel (e.g., an SEM cross-section of a cathode) representing different samples, different composition ratios, or different test temperatures without clear disclosure.
*   **Audit Procedure**:
    *   Compare panels within the same figure and across different figures in the main text and Supplementary Information (SI).
    *   Look for matching surface features, grain structures, pore distributions, or scratch lines.
    *   *Example comment*: "Figure 3a (MCO-10 cathode) and Figure S5b (MCO-20 cathode) appear to share identical grain boundary distributions. Could the authors clarify if these panels represent the same sample under different magnification levels or if a minor file duplication error occurred?"

## 2. Repeated Regions within a Single Panel
*   **Definition**: Sub-regions within a single image panel that display identical pixel configurations or repeated structures.
*   **Audit Procedure**:
    *   Inspect high-resolution SEM/TEM images for repeated grain clusters, pore arrangements, or background noise patterns.
    *   Use standard image comparison helpers (e.g., color-channel overlays or alignment transformations) to check if separate sub-regions match pixel-for-pixel.
    *   *Example comment*: "In Figure 4c (TEM image), the region marked 'A' and the region marked 'B' appear to show matching atomic spacing and lattice configurations. We would appreciate clarification on whether this arises from a periodic crystal symmetry or a minor imaging/compilation artifact."

## 3. Inconsistent Scale Bars and Magnification
*   **Definition**: Discrepancies between the scale bar value, the written magnification factor in the text/caption, and the actual size of physical features.
*   **Audit Procedure**:
    *   Verify that scale bars are present on all micrographs.
    *   Cross-reference scale bars with the text (e.g., if the text claims "pores of $10\ \mu\text{m}$ diameter" but the $1\ \mu\text{m}$ scale bar is wider than the pore).
    *   Check for changes in scale bar sizes in panels that are claimed to have the same magnification.

## 4. Contrast, Brightness, and Compression Anomalies
*   **Definition**: Discontinuous boundaries or sharp blocks in background noise, contrast, or brightness that may indicate file splicing or insertion.
*   **Audit Procedure**:
    *   Adjust image levels (brightness, contrast, gamma) uniformly to check for hidden boundaries or cropped borders.
    *   Analyze compression artifacts. Heavy JPEG compression can create repeating $8\times8$ pixel blocks; check if these blocks are uniform across the entire image or display sharp discontinuities.
    *   *Example comment*: "Adjusting the contrast of Figure 2d reveals a rectangular boundary around the XRD peak at $2\theta = 32^\circ$. Could the authors clarify the origin of this boundary or provide the raw, uncompressed diffraction data?"

## 5. Unexpected Identical Noise Patterns
*   **Definition**: Identical high-frequency background noise, baseline fluctuations, or signal noise in electrochemical curves (e.g., EIS, CV, or polarization curves) across supposedly independent measurements.
*   **Audit Procedure**:
    *   Verify that experimental noise or baseline ripples in separate measurements (e.g., testing at $500^\circ\text{C}$ and $600^\circ\text{C}$) are not identical. Natural experimental noise is statistically random and cannot be duplicated exactly across different trials.
    *   *Example comment*: "The high-frequency noise ripples in the Nyquist plot in Figure 5a (sample A) and Figure 5b (sample B) appear to be identical. We request clarification on whether these curves were obtained from the same measurement or if the baseline was normalized."
