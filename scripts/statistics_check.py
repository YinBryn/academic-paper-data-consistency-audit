#!/usr/bin/env python3
"""
Statistics Verification Script.
Computes mean, sample standard deviation, and population standard deviation of datasets.
Includes a comparison function to verify reported values within a certain tolerance.
No external dependencies.
"""

import math
import sys

def calculate_mean(values):
    """Calculate the arithmetic mean of a list of numbers."""
    if not values:
        raise ValueError("Dataset is empty.")
    return sum(values) / len(values)

def calculate_sample_std(values, mean=None):
    """
    Calculate the sample standard deviation (denominator n-1).
    Used for general experimental replicate samples.
    """
    n = len(values)
    if n < 2:
        raise ValueError("Sample standard deviation requires at least 2 data points.")
    if mean is None:
        mean = calculate_mean(values)
    variance = sum((x - mean) ** 2 for x in values) / (n - 1)
    return math.sqrt(variance)

def calculate_population_std(values, mean=None):
    """
    Calculate the population standard deviation (denominator n).
    Used when the dataset represents the entire population.
    """
    n = len(values)
    if n < 1:
        raise ValueError("Population standard deviation requires at least 1 data point.")
    if mean is None:
        mean = calculate_mean(values)
    variance = sum((x - mean) ** 2 for x in values) / n
    return math.sqrt(variance)

def compare_reported_value(reported_val, calculated_val, tolerance_pct=1.0):
    """
    Compares a reported value in a paper with an independently calculated value.
    Returns (is_consistent, relative_difference_pct).
    """
    if calculated_val == 0:
        if reported_val == 0:
            return True, 0.0
        else:
            return False, float('inf')
            
    diff = abs(reported_val - calculated_val)
    diff_pct = (diff / abs(calculated_val)) * 100.0
    is_consistent = diff_pct <= tolerance_pct
    return is_consistent, diff_pct

import argparse

def run_test():
    # Simple self-test to verify correctness
    test_data = [0.24, 0.26, 0.25, 0.27, 0.23]
    print("--- Running Statistics Check Self-Test ---")
    print(f"Test Dataset: {test_data}")
    
    mean = calculate_mean(test_data)
    sample_std = calculate_sample_std(test_data, mean)
    pop_std = calculate_population_std(test_data, mean)
    
    print(f"Calculated Mean: {mean:.4f}")
    print(f"Calculated Sample Std Dev (n-1): {sample_std:.5f}")
    print(f"Calculated Population Std Dev (n): {pop_std:.5f}")
    
    # Comparison examples
    reported_mean_1 = 0.25
    reported_mean_2 = 0.28
    
    ok1, err1 = compare_reported_value(reported_mean_1, mean)
    ok2, err2 = compare_reported_value(reported_mean_2, mean)
    
    print(f"Reported Mean {reported_mean_1} vs Calculated {mean:.4f}: Consistent? {ok1} (Diff: {err1:.2f}%)")
    print(f"Reported Mean {reported_mean_2} vs Calculated {mean:.4f}: Consistent? {ok2} (Diff: {err2:.2f}%)")

def main():
    parser = argparse.ArgumentParser(description="Verify statistical mean and standard deviation.")
    parser.add_argument("-d", "--data", type=str,
                        help="Comma-separated list of numbers (e.g., 0.24,0.26,0.25)")
    parser.add_argument("-r", "--reported", type=float,
                        help="Optional reported mean value to check against")
    parser.add_argument("-t", "--tolerance", type=float, default=1.0,
                        help="Tolerance percentage for comparison (default: 1.0%%)")
    parser.add_argument("--test", action="store_true",
                        help="Run built-in self-test")
    
    args = parser.parse_args()
    
    if args.test:
        run_test()
        return
        
    if not args.data:
        parser.print_help()
        print("\nExample:")
        print("  python3 statistics_check.py -d 0.24,0.26,0.25,0.27,0.23 -r 0.25")
        return
        
    try:
        values = [float(val.strip()) for val in args.data.split(",")]
    except ValueError:
        print("Error: Data must be a comma-separated list of numbers.")
        return
        
    mean = calculate_mean(values)
    print(f"Dataset size: {len(values)}")
    print(f"Calculated Mean: {mean:.5f}")
    
    try:
        sample_std = calculate_sample_std(values, mean)
        print(f"Calculated Sample Std Dev (n-1): {sample_std:.5f}")
    except ValueError as e:
        print(f"Sample Std Dev: {e}")
        
    pop_std = calculate_population_std(values, mean)
    print(f"Calculated Population Std Dev (n): {pop_std:.5f}")
    
    if args.reported is not None:
        ok, err = compare_reported_value(args.reported, mean, args.tolerance)
        print(f"Comparison: Reported={args.reported} vs Calculated={mean:.5f} | Consistent? {ok} (Diff: {err:.2f}%)")

if __name__ == "__main__":
    main()
