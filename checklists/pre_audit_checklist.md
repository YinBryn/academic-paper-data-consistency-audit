# Pre-Audit Checklist

This checklist is used to prepare, inventory, and verify the completeness of a research paper's documentation and files before beginning a detailed data consistency audit.

---

## 1. Article Metadata
- [ ] Record the full article title, author list, journal name, year, and DOI.
- [ ] Check for existing errata, corrections, or comments associated with the DOI.
- [ ] Identify the corresponding author(s) and their email addresses.

## 2. Document Inventory
- [ ] Download the main manuscript PDF.
- [ ] Download the Supplementary Information (SI) PDF/Word files.
- [ ] Download any open-source data tables, spreadsheets, or code repositories provided by the authors or publisher.
- [ ] Extract and convert tables from the main text and SI into editable spreadsheet formats (CSV, Excel) to prevent manual transcription errors.

## 3. Main Figures Check
- [ ] Catalog all figures presenting electrochemical performance (e.g., Nyquist plots, polarization curves, Arrhenius plots).
- [ ] Scan for figure coordinates, axis scales, and legends. Check if they are clearly readable and uncropped.
- [ ] Verify that all figures are explicitly discussed and referenced in the text.

## 4. Main Tables Check
- [ ] Catalog all tables containing experimental parameters, fit results, or statistical summaries.
- [ ] Identify which figures correspond to which tabulated datasets.
- [ ] Note the number of significant digits reported for physical parameters.

## 5. Supplementary Information (SI) Check
- [ ] Check if the SI contains critical data omitted from the main text (e.g., equivalent circuit fitting tables, raw EIS coordinates, or batch statistics).
- [ ] Cross-reference the numbering of supplementary figures/tables with references in the main text.

## 6. Source Data Check
- [ ] Check if the publisher provides an "Associated Data" tab or "Source Data" spreadsheets.
- [ ] Verify if raw electrochemical logs (e.g., raw impedance `.txt` or `.mpt` files) are hosted in an external repository (e.g., Zenodo, Figshare, Dryad).

## 7. Experimental Methods & Conditions Check
- [ ] Extract critical experimental parameters required for physical calculations:
  *   Active cell area ($\text{cm}^2$).
  *   Electrolyte and electrode thicknesses ($\mu\text{m}$ or $\text{mm}$).
  *   Operating temperatures ($^\circ\text{C}$ or $\text{K}$).
  *   Gas flow rates ($\text{sccm}$) and gas compositions (e.g., $3\%\ \text{H}_2\text{O}$).
- [ ] Flag if any of these critical input parameters are missing or undefined.

## 8. Code Availability
- [ ] Check if simulation models, equivalent circuit fitting scripts, or numerical solvers are made available (e.g., via GitHub, GitLab).
- [ ] If code is available, document the programming language, dependencies, and version information.

## 9. Units and Scale Validation
- [ ] Confirm that all physical units are clearly defined on axis labels, legends, and table headers.
- [ ] Check for correct scaling factors (e.g., ensuring polarization resistance is in $\Omega\ \text{cm}^2$ and not just $\Omega$, indicating proper area-normalization).

## 10. Derived Quantities Inventory
- [ ] List all derived physical quantities reported in the paper that require mathematical calculations:
  *   Activation Energy ($E_a$ or $E_{act}$).
  *   Statistical metrics (Means, Standard Deviations, Error Bars).
  *   Conductivity ($\sigma$) and Power Density ($P$).
  *   Apparent Diffusion Coefficients ($D_{app}$ or $D_{chem}$).
- [ ] Note which scripts in the `scripts/` directory will be used to verify each quantity.
