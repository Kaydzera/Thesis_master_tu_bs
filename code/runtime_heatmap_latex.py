import pandas as pd
import numpy as np

# File paths for all multipliers
files = [
    'data/sensitivity_grid_1_3.csv',
    'data/sensitivity_grid_2_5.csv',
    'data/sensitivity_grid_5_0.csv'
]

all_df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# Filter: omit root-optimal instances (where both bounds are optimal and nodes == 0)
mask = ~((all_df['ceiling_status'] == 'optimal') & (all_df['maxlpt_status'] == 'optimal') & (all_df['ceiling_nodes'] == 0) & (all_df['maxlpt_nodes'] == 0))
filtered_df = all_df[mask]

# Mark timeouts and leaf_timeouts for each bound
for bound, col, status_col in [
    ('Ceiling', 'ceiling_time', 'ceiling_status'),
    ('MaxLPT', 'maxlpt_time', 'maxlpt_status')
]:
    df = filtered_df.copy()
    timeout_mask = df[status_col].isin(['timeout', 'leaf_timeout'])
    df.loc[timeout_mask, col] = 4000.0
    valid_mask = df[status_col].isin(['completed', 'timeout', 'leaf_timeout'])
    df = df[valid_mask]
    # Normal scale plot
    print(f'% Scatter plot for {bound} bound (normal scale, color = machines)')
    print(r'\begin{tikzpicture}')
    print(r'  \begin{axis}[')
    print(r'    xlabel={Number of Job Types},')
    print(r'    ylabel={Runtime (s)},')
    print(r'    colorbar,')
    print(r'    colormap/viridis,')
    print(r'    scatter,')
    print(r'    only marks,')
    print(r'    point meta=explicit symbolic,')
    print(f'    title={{Runtime vs. Job Types, {bound} Bound, Normal Scale}},')
    print(r'  ]')
    print(r'    \addplot+[scatter, scatter src=explicit, mark=*,] coordinates {')
    # Single log-scale scatter plot with explicit point meta for machines
    print(f'% PGFPlots scatter plot for {bound} bound (log scale, color = machines)')
    print(r'\begin{tikzpicture}')
    print(r'  \begin{axis}[')
    print(r'    xlabel={Number of Job Types},')
    print(r'    ylabel={Runtime (s)},')
    print(r'    ymode=log,')
    print(r'    log basis y=10,')
    print(r'    scatter,')
    print(r'    only marks,')
    print(r'    colorbar,')
    print(r'    colormap/viridis,')
    print(r'    point meta=explicit,')
    print(r'    point meta min=2,')
    print(r'    point meta max=12,')
    print(r'    colorbar style={title=Machines},')
    print(r'  ]')
    print(r'    \addplot+[scatter, scatter src=explicit, mark=*] coordinates {')
    for _, row in df.iterrows():
        print(f'      ({row["n_jobs"]}, {row[col]}) [{row["m_machines"]}]')
    print(r'    };')
    print(r'  \end{axis}')
    print(r'\end{tikzpicture}')
    print(r'  \end{axis}')
