# Physics Consistency Checks (Category III)

This document provides a set of physics-informed checks to verify that reported data in materials electrochemistry papers conform to basic thermodynamic, kinetic, and physical conservation laws.

---

## 1. Dimensional Analysis and Unit Consistency
*   **Audit Procedure**: Perform a dimensional check on all reported variables, constants, and equations used in calculations.
*   **Key Checks**:
    *   Ensure that area-specific resistance ($ASR$ or $R_{p}$) is correctly expressed in $\Omega\ \text{cm}^2$. Note that $ASR = R_{raw} \times A_{active}$ (where $A_{active}$ is the cell active area). A common error is dividing raw resistance by the area instead of multiplying.
    *   Verify that conductivity ($\sigma$) has the unit of $\text{S}\ \text{cm}^{-1}$ (or $\Omega^{-1}\ \text{cm}^{-1}$) and is related to resistivity ($\rho = 1/\sigma$) and geometry via $\sigma = L / (R_{raw} \times A)$, where $L$ is the sample thickness.
    *   Check for consistent scaling factors across unit conversions (e.g., converting $\text{cm}^2$ to $\text{m}^2$).

## 2. Current–Voltage–Power (I–V–P) Consistency
*   **Physical Principle**: The power density ($P$) of an electrochemical cell is directly related to its current density ($I$) and cell voltage ($V$) by:
    $$P (W\ \text{cm}^{-2}) = I (A\ \text{cm}^{-2}) \times V (V)$$
*   **Audit Procedure**:
    1.  Locate the co-plotted current-voltage ($I\text{--}V$) and current-power ($I\text{--}P$) curves (typically shown in the same figure for fuel cells).
    2.  For a given current density, extract the corresponding voltage value from the $I\text{--}V$ curve.
    3.  Calculate the theoretical power density: $P_{calc} = I \times V$.
    4.  Compare $P_{calc}$ with the reported power density on the $I\text{--}P$ curve at that same current density.
    5.  Verify that the peak power density ($P_{max}$) matches the maximum product of $I \times V$ along the entire $I\text{--}V$ polarization curve.

## 3. Mass and Charge Balance (Conservation Laws)
*   **Physical Principle**: Under steady-state conditions, the rate of reactant consumption or product generation must balance the electrical current flowing through the cell (Faraday's Law).
    $$\dot{n} = \frac{I_{total}}{z F} \times \eta_F$$
    where $\dot{n}$ is the molar flow rate ($\text{mol}\ \text{s}^{-1}$), $I_{total}$ is the total current ($\text{A}$), $z$ is the number of electrons transferred per molecule, $F$ is the Faraday constant ($96,485\ \text{C}\ \text{mol}^{-1}$), and $\eta_F$ is the Faraday efficiency.
*   **Audit Procedure**:
    1.  Extract the reported total current, active area, and feed gas flow rates (often reported in $\text{sccm}$ - standard cubic centimeters per minute).
    2.  Calculate the maximum theoretical reactant consumption rate.
    3.  Verify that the reactant consumption rate required to support the reported current does not exceed the feed gas flow rate (which would violate mass conservation, indicating a fuel utilization $>100\%$).
    4.  Check for discrepancies between the reported product generation rate and the current via Faraday's Law.

## 4. Apparent Diffusion Coefficient ($D_{app}$) Magnitude
*   **Physical Principle**: The diffusion coefficient of species in solid-state materials is limited by the lattice structure, temperature, and activation barriers.
*   **Audit Procedure**:
    1.  Extract the reported diffusion coefficients (e.g., $D_{O^{2-}}$, $D_{H^+}$, or apparent chemical diffusion coefficient $D_{chem}$) derived from techniques like GITT (Galvanostatic Intermittent Titration Technique) or EIS.
    2.  Compare the values against established physical limits for the material class at the given temperature:
        *   Proton diffusion in perovskite oxides at $500\text{--}600^\circ\text{C}$ typically falls in the range of $10^{-6}$ to $10^{-8}\ \text{cm}^2\ \text{s}^{-1}$.
        *   Oxygen ion diffusion in perovskite oxides at $600\text{--}800^\circ\text{C}$ typically ranges from $10^{-7}$ to $10^{-10}\ \text{cm}^2\ \text{s}^{-1}$.
    3.  Flag values that are physically implausible (e.g., $D_{app} > 10^{-4}\ \text{cm}^2\ \text{s}^{-1}$ in a solid-state material at moderate temperatures, which approaches liquid-like diffusion rates) for further clarification.

## 5. Electrochemical Impedance Spectroscopy (EIS) Interpretation
*   **Physical Principle**: EIS Nyquist plots must follow physical constraints (e.g., negative imaginary impedance $-Z'' \ge 0$ for capacitive processes; real impedance $Z' \ge 0$).
*   **Audit Procedure**:
    1.  Verify that the high-frequency intercept with the real axis ($Z'$) is positive and represents a reasonable ohmic resistance for the electrolyte thickness and temperature.
    2.  Confirm that the equivalent capacitance of a fitted arc is physically reasonable:
        *   Bulk (dielectric) capacitance: $10^{-12}\ \text{F}\ \text{cm}^{-2}$
        *   Grain boundary capacitance: $10^{-11}\text{--}10^{-9}\ \text{F}\ \text{cm}^{-2}$
        *   Double-layer/electrochemical charge transfer capacitance: $10^{-6}\text{--}10^{-4}\ \text{F}\ \text{cm}^{-2}$
        *   Pseudocapacitance (chemical capacitance of mixed conductors): $10^{-3}\text{--}10^{-1}\ \text{F}\ \text{cm}^{-2}$
    3.  Flag instances where an arc is fitted to a capacitance value that mismatches the proposed physical process by several orders of magnitude.

## 6. Transport-Model Parameter Disclosure
*   **Audit Procedure**: Check whether simulations or macro-homogeneous models (e.g., Butler-Volmer kinetics, dusty-gas models) disclose key transport parameters.
*   **Key Checks**:
    *   Verify that porosity, tortuosity, pore size, and active triple-phase boundary (TPB) length are disclosed if modeling results are compared to experimental data.
    *   Verify that boundary conditions (gas concentrations, operating pressure, temperature) are explicitly defined.
