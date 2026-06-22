#!/usr/bin/env python3
"""
Arrhenius Fitting Script for Electrochemical Area Specific Resistance (ASR) / Polarization Resistance (Rp).
This script performs a linear fitting of:
1. ln(1/R) vs 1000/T  (standard kinetic activation energy)
2. ln(1/(R*T)) vs 1000/T (transport-informed activation energy)

It outputs the fitted values, activation energy (Ea) in eV, and the correlation coefficient R^2.
No external dependencies (uses standard library only).
"""

import argparse
import math

# Boltzmann constant in eV/K
KB = 8.617333262e-5

def linear_regression(x, y):
    """
    Performs simple linear regression y = m * x + c.
    Returns (m, c, R_squared)
    """
    n = len(x)
    if n < 2:
        raise ValueError("At least 2 data points are required for fitting.")
        
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xx = sum(val * val for val in x)
    sum_yy = sum(val * val for val in y)
    sum_xy = sum(x[i] * y[i] for i in range(n))
    
    # Calculate slope (m) and intercept (c)
    denom = (n * sum_xx - sum_x * sum_x)
    if denom == 0:
        raise ValueError("Vertical line detected; cannot fit.")
        
    m = (n * sum_xy - sum_x * sum_y) / denom
    c = (sum_y - m * sum_x) / n
    
    # Calculate R-squared (coefficient of determination)
    y_mean = sum_y / n
    ss_tot = sum((val - y_mean) ** 2 for val in y)
    if ss_tot == 0:
        r_sq = 1.0  # Perfect fit for flat line
    else:
        ss_res = sum((y[i] - (m * x[i] + c)) ** 2 for i in range(n))
        r_sq = 1.0 - (ss_res / ss_tot)
        
    return m, c, r_sq

def main():
    parser = argparse.ArgumentParser(description="Perform Arrhenius fitting for electrochemistry resistance data.")
    parser.add_argument("-t", "--temperatures", type=str, required=True,
                        help="Comma-separated temperatures in Celsius (e.g. 500,550,600,650)")
    parser.add_argument("-r", "--resistances", type=str, required=True,
                        help="Comma-separated resistance/ASR values in ohm-cm2 (e.g. 1.2,0.65,0.32,0.15)")
    parser.add_argument("--mode", choices=["kinetic", "transport"], default="kinetic",
                        help="kinetic: ln(1/R) vs 1000/T; transport: ln(1/(R*T)) vs 1000/T (default: kinetic)")
    
    args = parser.parse_args()
    
    try:
        temp_c = [float(val.strip()) for val in args.temperatures.split(",")]
        res_val = [float(val.strip()) for val in args.resistances.split(",")]
    except ValueError:
        print("Error: Temperatures and resistances must be comma-separated numeric lists.")
        return

    if len(temp_c) != len(res_val):
        print(f"Error: Number of temperatures ({len(temp_c)}) does not match resistances ({len(res_val)}).")
        return

    # Process lists
    n = len(temp_c)
    temp_k = [c + 273.15 for c in temp_c]
    inv_t = [1000.0 / tk for tk in temp_k] # 1000/T
    
    ln_y = []
    y_label = ""
    if args.mode == "kinetic":
        ln_y = [math.log(1.0 / r) for r in res_val]
        y_label = "ln(1/R)"
    else:
        # transport mode: ln(1 / (R * T))
        ln_y = [math.log(1.0 / (r * tk)) for r, tk in zip(res_val, temp_k)]
        y_label = "ln(1/(R*T))"
        
    # Print raw values
    print("--- Arrhenius Pre-Processed Data ---")
    print(f"{'T (C)':<8} {'T (K)':<8} {'1000/T (K-1)':<15} {'R (ohm-cm2)':<15} {y_label:<15}")
    for i in range(n):
        print(f"{temp_c[i]:<8.2f} {temp_k[i]:<8.2f} {inv_t[i]:<15.5f} {res_val[i]:<15.4f} {ln_y[i]:<15.5f}")
    print()
    
    # Fit
    try:
        m, c, r_sq = linear_regression(inv_t, ln_y)
    except ValueError as e:
        print(f"Fitting Error: {e}")
        return
        
    # Calculate activation energy (Ea) in eV
    # ln(y) = -Ea / (kB * T) + ln(A)
    # y-axis is ln(y), x-axis is 1000/T
    # So ln(y) = m * (1000/T) + c => slope m = -Ea / (1000 * kB)
    # Therefore: Ea = -m * 1000 * kB
    ea = -m * 1000.0 * KB
    
    print("--- Fitting Results ---")
    print(f"Fitting Mode: {args.mode}")
    print(f"Slope (m): {m:.5f}")
    print(f"Intercept (c): {c:.5f}")
    print(f"R^2 Coefficient: {r_sq:.6f}")
    print(f"Calculated Activation Energy (Ea): {ea:.4f} eV")
    print("-----------------------")

if __name__ == "__main__":
    main()
