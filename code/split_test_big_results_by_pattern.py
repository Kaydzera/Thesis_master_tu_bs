import csv

'''
This script reads the test_big_results_20260311_131045.csv file, which contains results for various patterns, and splits it into separate CSV files for each pattern.
The patterns considered are: uniform_ratios, high_variance, increasing, random_realistic, extreme, strong_correlation, and subset_sum.
For each pattern, a new CSV file is created in the data/test_big_results_by_pattern/ directory, containing only the rows corresponding to that pattern.
The output files are named test_big_results_{pattern}.csv, where {pattern} is replaced by the respective pattern name. 
This allows for easier analysis of results by pattern in subsequent steps.
'''




patterns = [
    "uniform_ratios",
    "high_variance",
    "increasing",
    "random_realistic",
    "extreme",
    "strong_correlation",
    "subset_sum",
]

input_csv = "data/test_big_results_20260311_131045.csv"
output_dir = "data/test_big_results_by_pattern/"

with open(input_csv, newline="", encoding="utf-8") as infile:
    reader = list(csv.reader(infile))
    header = reader[0]
    rows = reader[1:]

for pattern in patterns:
    filtered = [row for row in rows if row[2] == pattern]
    with open(f"{output_dir}test_big_results_{pattern}.csv", "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(filtered)
