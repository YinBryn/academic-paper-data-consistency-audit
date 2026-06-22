# Issue Log Template

This table is used to compile, organize, and track technical concerns identified during the paper audit.

| Issue ID | Category | Priority | Location | Concern | Evidence | Recalculation | Requested Clarification | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **IT-001** | Category I: Data Inconsistency | High / Medium / Low | Main text Page 3, Column 2; Fig. 2a vs Table 1 | Ohmic resistance value discrepancy | Fig. 2a shows $R_o = 0.15\ \Omega\ \text{cm}^2$, but Table 1 lists $R_o = 0.25\ \Omega\ \text{cm}^2$. | Mismatch is $66.7\%$. | Please clarify the correct ohmic resistance value at $600^\circ\text{C}$. | Open / Pending / Resolved |
| **IT-002** | Category II: Calculation Reproducibility | Medium | Fig. 5 Arrhenius plot | Activation energy value mismatch | Fig. 5 shows $E_a = 1.10\ \text{eV}$ for LSCF cathode. | Recalculation using Table S2 values gives $E_a = 0.92\ \text{eV}$ ($R^2 = 0.992$). | Please provide the raw fitting data or explain the fitting method. | Open |
| **IT-003** | Category III: Physical Consistency | High | Fig. 4b $I\text{--}V\text{--}P$ curves | Power density calculation mismatch | At $1.5\ \text{A}\ \text{cm}^{-2}$, $V = 0.60\ \text{V}$ (giving $P = 0.90\ \text{W}\ \text{cm}^{-2}$), but power curve plots $1.15\ \text{W}\ \text{cm}^{-2}$. | Calculated product $I \times V = 0.90$, plotted $P = 1.15$ (discrepancy of $27.8\%$). | Please clarify if the active area normalization factor was identical. | Open |
| **IT-004** | Category IV: Evidence-Claim Alignment | Low | Abstract, lines 5-7 | Overgeneralized stability claim | Text claims "excellent stability over 1000 h of testing". | Fig. 8 only presents stability data up to 100 hours. | Please provide the extended stability dataset or amend the claim. | Open |
