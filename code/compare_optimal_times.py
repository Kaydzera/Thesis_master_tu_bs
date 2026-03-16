import pandas as pd


'''
This script compares the runtime and node counts of the ceiling and MaxLPT bounds for all grid sensitivity instances 
that completed successfully at the root node.
It reads the results from the sensitivity analysis for both methods, merges them on common experimental conditions, and computes statistics on the differences in runtime and node counts.
The output includes average, median, maximal, and minimal differences in runtime, as well as counts of which method was faster and which explored fewer nodes.
The results are printed to the console, providing insights into the practical performance differences between the two bounding methods across the different experimental conditions.

It returns: 
Ceiling vs MaxLPT runtime comparison (only optimal cases, all multipliers)
Average time difference (Ceiling - MaxLPT): -0.428049 seconds
Median time difference: -0.081100 seconds
Maximal time difference: 0.136900 seconds
Minimal time difference: -7.002400 seconds
Average absolute time difference: 0.428851 seconds
Average difference when Ceiling is faster: -0.438035 seconds
Average difference when MaxLPT is faster: 0.022900 seconds
Ceiling faster: 447 times
MaxLPT faster: 8 times
Equal times: 2 times
'''


# File paths for all multipliers
files = [
    'data/sensitivity_grid_1_3.csv',
    'data/sensitivity_grid_2_5.csv',
    'data/sensitivity_grid_5_0.csv'
]

# Read and concatenate all data
all_df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# Filter for cases where both ceiling and maxlpt status are 'optimal'
opt_df = all_df[(all_df['ceiling_status'] == 'optimal') & (all_df['maxlpt_status'] == 'optimal')]

# Compute time differences
opt_df['time_diff'] = opt_df['ceiling_time'] - opt_df['maxlpt_time']
abs_time_diff = opt_df['time_diff'].abs()

# Statistics
avg_diff = opt_df['time_diff'].mean()
median_diff = opt_df['time_diff'].median()
max_diff = opt_df['time_diff'].max()
min_diff = opt_df['time_diff'].min()
mean_abs_diff = abs_time_diff.mean()
avg_ceil_faster = opt_df.loc[opt_df['time_diff'] < 0, 'time_diff'].mean()
avg_maxlpt_faster = opt_df.loc[opt_df['time_diff'] > 0, 'time_diff'].mean()
ceil_faster = (opt_df['time_diff'] < 0).sum()
maxlpt_faster = (opt_df['time_diff'] > 0).sum()
equal = (opt_df['time_diff'] == 0).sum()

# Print results
print('Ceiling vs MaxLPT runtime comparison (only optimal cases, all multipliers)')
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
