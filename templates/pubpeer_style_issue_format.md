# PubPeer-Style Technical Comment Format

This template is designed to draft single, objective, and self-contained technical comments suitable for posting on post-publication peer-review platforms (such as PubPeer) or submitting to journal editor portals. The tone must remain strictly technical, neutral, and focused on data clarity.

---

### [Issue Title]
*Provide a descriptive, objective title summarizing the physical parameter or figure in question (e.g., "Ohmic resistance discrepancy in Figure 2" or "Activation energy calculation consistency"). Do not use qualitative or accusatory words.*

**Location**: [Identify the exact page, column, figure, table, equation, or line number (e.g., Page 4, Figure 3b, or Supplementary Table S1)].

**Observation**:  
[Provide a clear, factual description of the observed data point, trend, or discrepancy. State the exact numbers as they appear in the paper.]
*   *Example*: "In Figure 3b, the polarization resistance ($R_p$) of the composite cathode at $600^\circ\text{C}$ is plotted as approximately $0.15\ \Omega\ \text{cm}^2$. However, Table 1 lists the $R_p$ value under the same conditions as $0.25\ \Omega\ \text{cm}^2$."

**Check / Recalculation**:  
[Describe the step-by-step verification, equations, or calculations performed to verify the observation. Present the math transparently so it can be replicated.]
*   *Example*: "Using the data points listed in Supplementary Table S2, we recalculated the activation energy using the Arrhenius relation: $\ln(1/ASR) \propto -E_a / (k_B T)$. The linear regression slope yields an activation energy ($E_a$) of $1.01\ \text{eV}$ ($R^2 = 0.999$), which differs from the reported value of $0.85\ \text{eV}$ in the text."

**Why It Matters**:  
[Explain the scientific or technical consequence of the discrepancy in a neutral manner. Focus on how it impacts model parameters, reproduction of results, or baseline comparisons.]
*   *Example*: "Since the polarization resistance is a key input parameter for electrode transport modeling, a $66.7\%$ discrepancy in $R_p$ limits the accuracy of secondary model simulations and makes independent performance replication difficult."

**Clarification Requested**:  
[State the exact technical questions that would resolve the observation, addressed to the authors.]
*   *Example*: "Could the authors clarify the correct value of the polarization resistance at $600^\circ\text{C}$? If the difference arises from different sample batches or specific fitting bounds, providing those details would be highly beneficial."
