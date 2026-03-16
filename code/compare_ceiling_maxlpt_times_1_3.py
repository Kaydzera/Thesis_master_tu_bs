import pandas as pd
import numpy as np

'''
Comparison of Ceiling vs MaxLPT bounds for runtime and node count across different budget multipliers. 
This script reads the results from the sensitivity analysis for both methods, merges them on common experimental conditions, and computes statistics on the differences in runtime and node counts.
The output includes average, median, maximal, and minimal differences in runtime, as well as counts of which method was faster and which explored fewer nodes.

Output:
Ceiling vs MaxLPT runtime and node count comparison (all multipliers)
Average time difference (Ceiling - MaxLPT): 71.383366 seconds
Median time difference: 0.392900 seconds
Maximal time difference: 1057.312000 seconds
Minimal time difference: -0.425900 seconds
Average absolute time difference: 71.423638 seconds
Average difference when Ceiling is faster: -0.061415 seconds
Average difference when MaxLPT is faster: 106.234478 seconds
Ceiling faster: 20 times
MaxLPT faster: 41 times
Equal times: 0 times

Average node count difference (Ceiling - MaxLPT): 4782454.00
Median node count difference: 68985.00
Maximal node count difference: 54531975
Minimal node count difference: 22
Ceiling explored fewer nodes: 0 times
MaxLPT explored fewer nodes: 61 times
Equal node counts: 0 times
'''


# File paths for all multipliers (relative to workspace root)
ceiling_files = [
    'data/sensitivity_grid_1_3_ceiling_completed.csv',
    'data/sensitivity_grid_2_5_ceiling_completed.csv',
    'data/sensitivity_grid_5_0_ceiling_completed.csv'
]
maxlpt_files = [
    'data/sensitivity_grid_1_3_maxlpt_completed.csv',
    'data/sensitivity_grid_2_5_maxlpt_completed.csv',
    'data/sensitivity_grid_5_0_maxlpt_completed.csv'
]

# Concatenate all ceiling and maxlpt data
df_ceil = pd.concat([pd.read_csv(f) for f in ceiling_files], ignore_index=True)
df_maxlpt = pd.concat([pd.read_csv(f) for f in maxlpt_files], ignore_index=True)

# Merge on common columns (machines, jobs, budget, repetition, seed)
merge_cols = ['m_machines', 'n_jobs', 'budget_multiplier', 'budget', 'repetition', 'seed']
df = pd.merge(df_ceil, df_maxlpt, on=merge_cols, suffixes=('_ceil', '_maxlpt'))

# Compute time differences
# Positive: Ceiling slower; Negative: MaxLPT slower
df['time_diff'] = df['ceiling_time_ceil'] - df['maxlpt_time_maxlpt']

# Compute absolute time difference
abs_time_diff = df['time_diff'].abs()
mean_abs_diff = abs_time_diff.mean()

# Average difference when ceiling is faster (negative time_diff)
avg_ceil_faster = df.loc[df['time_diff'] < 0, 'time_diff'].mean()
# Average difference when maxlpt is faster (positive time_diff)
avg_maxlpt_faster = df.loc[df['time_diff'] > 0, 'time_diff'].mean()

# Compute node count differences
# Positive: Ceiling explored more nodes; Negative: MaxLPT explored more nodes
df['node_diff'] = df['ceiling_nodes_ceil'] - df['maxlpt_nodes_maxlpt']

# Time statistics
avg_diff = df['time_diff'].mean()
median_diff = df['time_diff'].median()
max_diff = df['time_diff'].max()
min_diff = df['time_diff'].min()

# Node statistics
avg_node_diff = df['node_diff'].mean()
median_node_diff = df['node_diff'].median()
max_node_diff = df['node_diff'].max()
min_node_diff = df['node_diff'].min()

# Count which is faster
ceil_faster = (df['time_diff'] < 0).sum()
maxlpt_faster = (df['time_diff'] > 0).sum()
equal = (df['time_diff'] == 0).sum()

# Count which explored fewer nodes
ceil_nodes_fewer = (df['node_diff'] < 0).sum()
maxlpt_nodes_fewer = (df['node_diff'] > 0).sum()
equal_nodes = (df['node_diff'] == 0).sum()

# Print results
print('Ceiling vs MaxLPT runtime and node count comparison (all multipliers)')
print(f'Average time difference (Ceiling - MaxLPT): {avg_diff:.6f} seconds')
print(f'Median time difference: {median_diff:.6f} seconds')
print(f'Maximal time difference: {max_diff:.6f} seconds')
print(f'Minimal time difference: {min_diff:.6f} seconds')
print(f'Average absolute time difference: {mean_abs_diff:.6f} seconds')
print(f'Average difference when Ceiling is faster: {avg_ceil_faster:.6f} seconds')
print(f'Average difference when MaxLPT is faster: {avg_maxlpt_faster:.6f} seconds')
print(f'Ceiling faster: {ceil_faster} times')
print(f'MaxLPT faster: {maxlpt_faster} times')
print(f'Equal times: {equal} times')
print()
print(f'Average node count difference (Ceiling - MaxLPT): {avg_node_diff:.2f}')
print(f'Median node count difference: {median_node_diff:.2f}')
print(f'Maximal node count difference: {max_node_diff}')
print(f'Minimal node count difference: {min_node_diff}')
print(f'Ceiling explored fewer nodes: {ceil_nodes_fewer} times')
print(f'MaxLPT explored fewer nodes: {maxlpt_nodes_fewer} times')
print(f'Equal node counts: {equal_nodes} times')

# --- Additional suggestions ---
# 1. Grouped statistics by budget multiplier (df.groupby('budget_multiplier'))
# 2. Proportion of cases where one method is both faster and explores fewer nodes
# 3. Outlier analysis: print rows with largest time/node differences
# 4. Correlation between node_diff and time_diff
# 5. Distribution plots (histograms) for differences (optional, if matplotlib available)
