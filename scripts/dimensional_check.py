#!/usr/bin/env python3
"""
Dimensional Check and Physics Consistency Helper.
Checks physical unit strings and audits relationships like P = I * V.
No external dependencies.
"""

import sys

def check_diffusion_unit(unit_str):
    """
    Checks if a reported diffusion coefficient unit is standard.
    Standard units: cm^2/s or m^2/s.
    Returns (is_valid, suggested_unit)
    """
    cleaned = unit_str.replace(" ", "").replace("*", "").replace("-1", "").lower()
    
    # Standard forms in papers: cm2 s-1, cm^2/s, cm2/s, m2 s-1, etc.
    valid_elements = ["cm2s", "cm^2s", "m2s", "m^2s", "cm2/s", "m2/s", "cm^2/s", "m^2/s"]
    
    is_valid = any(elem in cleaned for elem in valid_elements)
    
    # Common mistakes: cm/s (velocity), cm2/s2, etc.
    if is_valid:
        return True, unit_str
    else:
        # Check if they used a velocity unit
        if "cm/s" in cleaned or "m/s" in cleaned and "2" not in cleaned:
            return False, "cm²/s (reported unit lacks the area dimension, resembling velocity)"
        return False, "cm²/s or m²/s"

def check_potential_unit(unit_str):
    """
    Checks if the potential unit is standard.
    Standard: V or mV.
    """
    cleaned = unit_str.strip().lower()
    if cleaned in ["v", "mv", "v (vs. ref)", "v vs. ocv", "v (vs. ocv)", "v vs. rhe"]:
        return True, unit_str
    else:
        return False, "V or mV"

def check_current_density_power_density_relation(current_density, cell_voltage, power_density, tolerance_pct=1.0):
    """
    Verifies if P = I * V holds within a given tolerance.
    Units:
        current_density: A/cm2
        cell_voltage: V
        power_density: W/cm2
    Returns (is_consistent, calculated_power, diff_pct)
    """
    calc_power = current_density * cell_voltage
    if calc_power == 0:
        if power_density == 0:
            return True, 0.0, 0.0
        else:
            return False, 0.0, float('inf')
            
    diff = abs(power_density - calc_power)
    diff_pct = (diff / calc_power) * 100.0
    is_consistent = diff_pct <= tolerance_pct
    return is_consistent, calc_power, diff_pct

import argparse

def run_checks():
    print("--- Running Dimensional & Relation Checks ---")
    
    # Test diffusion units
    units = ["cm2 s-1", "cm/s", "cm^2/s", "m2/s"]
    for u in units:
        ok, sug = check_diffusion_unit(u)
        print(f"Diffusion Unit '{u}': Valid? {ok} | Suggestion: {sug}")
        
    print()
    
    # Test I-V-P relations
    I_val = 1.25 # A/cm2
    V_val = 0.65 # V
    P_reported = 0.8125 # W/cm2
    P_mismatched = 0.95 # W/cm2
    
    ok1, calc1, err1 = check_current_density_power_density_relation(I_val, V_val, P_reported)
    ok2, calc2, err2 = check_current_density_power_density_relation(I_val, V_val, P_mismatched)
    
    print(f"Relation check for I={I_val}, V={V_val}, P_reported={P_reported}:")
    print(f"  Calculated P = {calc1:.4f} | Consistent? {ok1} (Diff: {err1:.2f}%)")
    
    print(f"Relation check for I={I_val}, V={V_val}, P_reported={P_mismatched}:")
    print(f"  Calculated P = {calc2:.4f} | Consistent? {ok2} (Diff: {err2:.2f}%)")

def main():
    parser = argparse.ArgumentParser(description="Check physical units and current-voltage-power consistency.")
    parser.add_argument("--run", action="store_true",
                        help="Run built-in self-test checks")
    parser.add_argument("--diffusion", type=str,
                        help="Check a specific diffusion unit string (e.g. 'cm^2/s')")
    parser.add_argument("--potential", type=str,
                        help="Check a specific potential unit string (e.g. 'mV')")
    parser.add_argument("--ivp", type=str,
                        help="Perform I-V-P check. Format: current,voltage,power (e.g. 1.25,0.65,0.8125)")
    parser.add_argument("-t", "--tolerance", type=float, default=1.0,
                        help="Tolerance percentage for I-V-P check (default: 1.0%%)")
                        
    args = parser.parse_args()
    
    if args.run:
        run_checks()
        return
        
    if not (args.diffusion or args.potential or args.ivp):
        parser.print_help()
        print("\nExamples:")
        print("  python3 dimensional_check.py --diffusion 'cm/s'")
        print("  python3 dimensional_check.py --ivp 1.5,0.63,0.95")
        return
        
    if args.diffusion:
        ok, sug = check_diffusion_unit(args.diffusion)
        print(f"Diffusion Unit '{args.diffusion}': Valid? {ok} | Suggestion/Correct form: {sug}")
        
    if args.potential:
        ok, sug = check_potential_unit(args.potential)
        print(f"Potential Unit '{args.potential}': Valid? {ok} | Suggestion/Correct form: {sug}")
        
    if args.ivp:
        try:
            parts = [float(val.strip()) for val in args.ivp.split(",")]
            if len(parts) != 3:
                raise ValueError("Must contain exactly 3 comma-separated numbers.")
        except ValueError as e:
            print(f"Error parsing --ivp: {e}")
            return
            
        cur, volt, pwr = parts
        ok, calc, err = check_current_density_power_density_relation(cur, volt, pwr, args.tolerance)
        print(f"I-V-P Consistency: Current={cur} A/cm2, Voltage={volt} V, Reported Power={pwr} W/cm2")
        print(f"  Calculated Power = {calc:.5f} W/cm2")
        print(f"  Consistent? {ok} (Difference: {err:.2f}%)")

if __name__ == "__main__":
    main()
