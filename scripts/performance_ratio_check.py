#!/usr/bin/env python3
"""
Performance Improvement Ratio Check.
Provides function to calculate percentage improvements or reductions,
and batch compares values from a CSV file.
No external dependencies.
"""

import argparse
import csv
import sys

def improvement_ratio(new_val, baseline_val):
    """
    Calculates the relative improvement ratio: (new - baseline) / baseline.
    Returns the percentage value.
    """
    if baseline_val == 0:
        raise ZeroDivisionError("Baseline value cannot be zero.")
    return ((new_val - baseline_val) / baseline_val) * 100.0

def reduction_ratio(new_val, baseline_val):
    """
    Calculates the relative reduction ratio: (baseline - new) / baseline.
    Commonly used for resistance reduction audits.
    """
    if baseline_val == 0:
        raise ZeroDivisionError("Baseline value cannot be zero.")
    return ((baseline_val - new_val) / baseline_val) * 100.0

def batch_process_csv(csv_path, new_sample_name, baseline_sample_name, target_col):
    """
    Reads a CSV and computes the improvement of new_sample_name over baseline_sample_name
    grouped by temperature or other experimental conditions.
    """
    data = []
    try:
        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: CSV file not found at '{csv_path}'.")
        return
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    # Group by Temperature_C or similar
    # We look for a temperature or condition column
    temp_col = None
    for col in ['temperature_C', 'temperature', 'temp', 'T (C)']:
        if col in data[0]:
            temp_col = col
            break

    if not temp_col:
        print("Warning: No temperature/condition column identified. Comparing all rows individually.")
        
    print(f"--- Batch Performance Comparison (Target: {target_col}) ---")
    print(f"New Sample: {new_sample_name} | Baseline Sample: {baseline_sample_name}\n")

    # Match pairs by temperature
    conditions = {}
    for row in data:
        cond = row[temp_col] if temp_col else "All"
        sample = row.get('sample', '').strip()
        try:
            val = float(row[target_col])
        except (ValueError, TypeError):
            continue
            
        if cond not in conditions:
            conditions[cond] = {}
        conditions[cond][sample] = val

    print(f"{'Condition':<15} {baseline_sample_name:<18} {new_sample_name:<18} {'Change %':<15}")
    print("-" * 70)

    for cond, samples in sorted(conditions.items()):
        new_val = samples.get(new_sample_name)
        base_val = samples.get(baseline_sample_name)
        
        if new_val is not None and base_val is not None:
            try:
                # Decide if it's resistance (reduction preferred) or power/current/conductivity (increase preferred)
                is_resistance = any(term in target_col.lower() for term in ['resistance', 'rp', 'asr', 'r_p'])
                if is_resistance:
                    ratio = reduction_ratio(new_val, base_val)
                    direction = "reduction"
                else:
                    ratio = improvement_ratio(new_val, base_val)
                    direction = "increase"
                    
                print(f"{cond:<15} {base_val:<18.4f} {new_val:<18.4f} {ratio:<+14.2f}% ({direction})")
            except ZeroDivisionError:
                print(f"{cond:<15} {base_val:<18.4f} {new_val:<18.4f} {'Zero Baseline':<15}")
        else:
            missing = []
            if base_val is None: missing.append(baseline_sample_name)
            if new_val is None: missing.append(new_sample_name)
            print(f"{cond:<15} {'Missing ' + ', '.join(missing):<50}")

def main():
    parser = argparse.ArgumentParser(description="Calculate performance improvement ratios and parse CSV files.")
    parser.add_argument("--csv", type=str, help="Path to CSV file for batch processing")
    parser.add_argument("--new", type=str, help="Name of the improved/new sample")
    parser.add_argument("--base", type=str, help="Name of the baseline/control sample")
    parser.add_argument("--column", type=str, help="Column name to compare (e.g. Rp_ohm_cm2 or Pmax_W_cm2)")
    
    args = parser.parse_args()
    
    if args.csv:
        if not (args.new and args.base and args.column):
            print("Error: When using --csv, you must specify --new, --base, and --column.")
            sys.exit(1)
        batch_process_csv(args.csv, args.new, args.base, args.column)
    else:
        # Prompt user on standard usage
        print("Standard calculation example:")
        base_p = 0.50 # W/cm2
        new_p = 1.25  # W/cm2
        pct = improvement_ratio(new_p, base_p)
        print(f"Improvement from {base_p} to {new_p} W/cm2 is {pct:+.2f}%")
        
        base_r = 0.85 # ohm-cm2
        new_r = 0.17 # ohm-cm2
        red = reduction_ratio(new_r, base_r)
        print(f"Resistance reduction from {base_r} to {new_r} ohm-cm2 is {red:.2f}%")
        print("\nTo run a batch audit, use:")
        print("  python3 performance_ratio_check.py --csv <file.csv> --new <new_sample> --base <baseline> --column <column_name>")

if __name__ == "__main__":
    main()
