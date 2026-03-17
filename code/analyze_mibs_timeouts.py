import pandas as pd
import glob
import os

# --- Adapted for comparison with BnB (Ceiling/MaxLPT) ---

# File paths for MIBS results
mibs_files = [
    r'C:\Users\oleda\.vscode\Thesis_Bilevel_TUBS\data\mibs results\grid_mibs_results_1_3.csv',
    r'C:\Users\oleda\.vscode\Thesis_Bilevel_TUBS\data\mibs results\grid_mibs_results_2_5.csv',
    r'C:\Users\oleda\.vscode\Thesis_Bilevel_TUBS\data\mibs results\grid_mibs_results_5_0.csv',
]

# File paths for BnB (Ceiling/MaxLPT) results
bnb_files = [
    r'C:\Users\oleda\.vscode\Thesis_Bilevel_TUBS\data\sensitivity_grid_1_3.csv',
    r'C:\Users\oleda\.vscode\Thesis_Bilevel_TUBS\data\sensitivity_grid_2_5.csv',
    r'C:\Users\oleda\.vscode\Thesis_Bilevel_TUBS\data\sensitivity_grid_5_0.csv',
]

# Load and concatenate all MIBS results
mibs_df = pd.concat([pd.read_csv(f) for f in mibs_files], ignore_index=True)
# Load and concatenate all BnB results
bnb_df = pd.concat([pd.read_csv(f) for f in bnb_files], ignore_index=True)

# Build keys for matching: (m_machines, n_jobs, budget_multiplier, repetition, seed)
def mibs_key(row):
    return (
        int(row['m_machines']),
        int(row['n_jobs']),
        float(row['budget_multiplier']),
        int(row['repetition']),
        int(row['seed'])
    )

def bnb_key(row):
    return (
        int(row['m_machines']),
        int(row['n_jobs']),
        float(row['budget_multiplier']),
        int(row['repetition']),
        int(row['seed'])
    )

# Index BnB results by key
bnb_dict = {bnb_key(row): row for _, row in bnb_df.iterrows()}

ceiling_faster = []
maxlpt_faster = []
ceiling_timeouts = 0
maxlpt_timeouts = 0
total_matched = 0

for _, mibs_row in mibs_df.iterrows():
    key = mibs_key(mibs_row)
    if key not in bnb_dict:
        print(f"Warning: No matching BnB result for MIBS instance with key {key}")
        continue
    bnb_row = bnb_dict[key]
    total_matched += 1

    # Get MIBS time (timeout = 3600)
    mibs_time = float(mibs_row['mibs_wall_time_seconds']) if mibs_row['mibs_status'] != 'timeout' else 3600.0
    # Get BnB times (timeout = 3600)
    ceiling_time = float(bnb_row['ceiling_time']) if bnb_row['ceiling_status'] != 'timeout' else 3600.0
    maxlpt_time = float(bnb_row['maxlpt_time']) if bnb_row['maxlpt_status'] != 'timeout' else 3600.0

    # Record timeouts
    if bnb_row['ceiling_status'] == 'timeout':
        ceiling_timeouts += 1
    if bnb_row['maxlpt_status'] == 'timeout':
        maxlpt_timeouts += 1

    # Compute speedups (positive = BnB faster)
    ceiling_faster.append(mibs_time - ceiling_time)
    maxlpt_faster.append(mibs_time - maxlpt_time)

import numpy as np

def stats(arr):
    arr = np.array(arr)
    return {
        'mean': np.mean(arr),
        'median': np.median(arr),
        'min': np.min(arr),
        'max': np.max(arr),
        'std': np.std(arr),
    }

print(f"Total matched instances: {total_matched}")
print(f"Ceiling timeouts: {ceiling_timeouts}")
print(f"MaxLPT timeouts: {maxlpt_timeouts}")
print("\nCeiling speedup (MIBS - Ceiling, seconds):", stats(ceiling_faster))
print("MaxLPT speedup (MIBS - MaxLPT, seconds):", stats(maxlpt_faster))
