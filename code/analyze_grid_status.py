import pandas as pd

'''
This script analyzes the status counts of the ceiling and maxlpt methods from a given CSV file containing sensitivity analysis results. 
It counts the occurrences of different statuses (e.g., completed, timeout, error) for both methods and prints the counts to the console.
Additionally, it filters the original DataFrame to create two new CSV files: 
one containing only the entries where the ceiling method completed successfully, 
and another for the maxlpt method.
The output CSV files are saved in the data/ directory with names indicating the method and that they contain only completed entries.
This allows for further analysis of the completed cases separately from those that timed out or encountered errors.
'''

def analyze_status_counts(input_csv, OUTPUT_CSV_CEILING='sensitivity_grid_2_5_ceiling_completed.csv', OUTPUT_CSV_MAXLPT='sensitivity_grid_2_5_maxlpt_completed.csv'):
    df = pd.read_csv(input_csv)
    # Count ceiling_status occurrences
    ceiling_counts = df['ceiling_status'].value_counts()
    # Count maxlpt_status occurrences
    maxlpt_counts = df['maxlpt_status'].value_counts()
    print('Ceiling Status Counts:')
    print(ceiling_counts)
    print('\nMaxLPT Status Counts:')
    print(maxlpt_counts)

    # Filter for completed entries
    ceiling_completed = df[df['ceiling_status'] == 'completed']
    maxlpt_completed = df[df['maxlpt_status'] == 'completed']
    ceiling_completed.to_csv(OUTPUT_CSV_CEILING, index=False)
    maxlpt_completed.to_csv(OUTPUT_CSV_MAXLPT, index=False)
    print('\nCSV files written:')
    print(OUTPUT_CSV_CEILING)
    print(OUTPUT_CSV_MAXLPT)

if __name__ == '__main__':
    analyze_status_counts('data/sensitivity_grid_2_5.csv', 'data/sensitivity_grid_2_5_ceiling_completed.csv', 'data/sensitivity_grid_2_5_maxlpt_completed.csv')

    analyze_status_counts('data/sensitivity_grid_1_3.csv', 'data/sensitivity_grid_1_3_ceiling_completed.csv', 'data/sensitivity_grid_1_3_maxlpt_completed.csv')

    analyze_status_counts('data/sensitivity_grid_5_0.csv', 'data/sensitivity_grid_5_0_ceiling_completed.csv', 'data/sensitivity_grid_5_0_maxlpt_completed.csv')