# Academic Paper Data Consistency Audit

This project provides a physics-informed technical audit workflow for published materials electrochemistry papers. It helps researchers check whether figures, tables, supplementary information, source data, recalculations, physical dimensions, and mechanistic claims are mutually consistent.

*Inspired by reproducibility and research-integrity workflows, but this project focuses on materials electrochemistry.*

---

## 1. Project Title
**Academic Paper Data Consistency Audit**: A technical audit framework for published articles in materials science, solid-state electrochemistry, solid oxide cells (SOFC/SOEC), and protonic ceramic cells (PCC).

## 2. Short Description
This repository contains a structured methodology, templates, and reference Python scripts designed to perform post-publication technical checks on published research papers. It focuses on identifying core data inconsistencies, verifying calculation reproducibility, evaluating physical and thermodynamic plausibility, and assessing the alignment between qualitative claims and empirical evidence.

## 3. Scope
The scope of this project is strictly limited to checking the internal self-consistency of data presented in published research (or drafts under peer review). It is designed to evaluate solid-state electrochemistry papers, particularly those describing:
*   Electrode kinetics and polarization resistance ($R_p$, $ASR$).
*   Temperature-dependent electrical conductivity ($\sigma$) and Arrhenius fittings.
*   Current-voltage-power ($I\text{--}V\text{--}P$) polarization relationships in fuel cells/electrolyzers.
*   Solid-state ionic diffusion coefficients ($D_{app}$) and electrical properties.

## 4. What this Project Checks
*   **Data Consistency**: Discrepancies between figure points, tables, text assertions, and Supplementary Information (SI) data tables.
*   **Calculational Reproducibility**: Mathematical verification of activation energies ($E_a$), sample standard deviations, and reported performance improvement percentages.
*   **Physics-Informed Boundaries**: Conformance of data to physical constraints such as current-voltage-power relations ($P = I \times V$), charge/mass conservation, and realistic ranges for diffusion coefficients.
*   **Claim-Evidence Alignment**: Evaluation of whether qualitative conclusions or proposed electrochemical mechanisms are supported by direct evidence rather than indirect fitting or simulations alone.

## 5. What this Project Does Not Claim
*   **No Determination of Misconduct**: This project evaluates data consistency and reproducibility. It does not judge the authors' intent or label discrepancies as academic fraud or misconduct.
*   **No Physical Re-experimentation**: The audit is entirely based on the published manuscript and supplementary datasets; it does not involve reproducing the physical synthesis or experimental testing of the materials.
*   **No Peer Review Replacement**: This is a specialized technical check, not a general evaluation of a paper's novelty, scientific significance, or impact.

## 6. Workflow
The technical audit follows a five-step diagnostic pipeline:
```mermaid
graph TD
    A["1. Data Extraction<br>(Text, Tables, Figures, SI)"] --> B["2. Cross-Referencing<br>(Check matching values)")
    B --> C["3. Recalculation<br>(Arrhenius, Stats, Ratios)")
    C --> D["4. Physics Check<br>(P=IV, Diffusion limits)")
    D --> E["5. Reporting<br>(Compile Neutral Memo/Comment)"]
```

## 7. Example Audit Categories
Findings are structured into four objective categories:
*   **Category I (Core Inconsistencies)**: Numerical mismatch between text, tables, and plots.
*   **Category II (Calculation Reproducibility)**: Discrepancies in calculated slope-derived parameters (e.g., $E_a$) or stats.
*   **Category III (Physical Reasonableness)**: Violation of physical laws (e.g., power curve mismatching $I \times V$ product).
*   **Category IV (Claim Mismatch)**: Mechanistic conclusions overshooting the provided experimental resolution.

## 8. Repository Structure
```text
academic-paper-data-consistency-audit/
├── README.md                           # Project homepage and introduction
├── methodology/
│   ├── audit_framework.md              # Four-tier audit category description
│   ├── data_consistency_checks.md      # Category I check guidelines
│   ├── reproducibility_checks.md       # Category II check guidelines
│   ├── physics_consistency_checks.md   # Category III check guidelines
│   └── evidence_claim_alignment.md     # Category IV check guidelines
├── templates/
│   ├── technical_audit_report_template.md  # Template for drafting full audit reports
│   ├── editor_technical_comment_template.md # Neutral email/letter template for journal editors
│   └── issue_log_template.md           # Tabular markdown tracker for identified concerns
├── examples/
│   ├── anonymized_case_study.md        # Reference audit case study using mock data
│   └── example_recalculation_table.csv # Mock performance dataset for testing scripts
├── scripts/
│   ├── arrhenius_fit.py                # Arrhenius regression and Ea calculator
│   ├── statistics_check.py             # Mean and standard deviation verifier
│   ├── performance_ratio_check.py      # Improvement ratio calculator (batch CSV support)
│   └── dimensional_check.py            # Unit validation and I-V-P physical check
├── docs/
│   ├── terminology.md                  # Definition of core project terms
│   ├── writing_style_guide.md          # Linguistic instructions for maintaining neutral tone
│   └── limitations_and_ethics.md       # Ethical boundaries and responsible disclosure rules
├── LICENSE                             # MIT License
└── .gitignore                          # Standard python git exclusions
```

## 9. Ethical and Legal Note
Users of this framework are expected to maintain the highest standards of scientific professionalism. 
*   Always use neutral, objective, and non-accusatory language.
*   Avoid public accusations; contact authors first to resolve questions.
*   Do not redistribute copyrighted or paywalled source PDFs alongside reports.
*   Focus purely on data facts and physical laws, avoiding assumptions regarding author intent.

## 10. License
This project is licensed under the terms of the [MIT License](LICENSE).
