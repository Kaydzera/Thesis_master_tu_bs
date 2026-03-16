
import csv
import numpy as np


'''

This script reads the test_big_results_20260311_235529.csv file, which contains detailed results of the verification process for different patterns.
It groups the results by pattern, counts the number of timeouts, calculates mean enumeration times, and computes mean and maximum runtimes for both the ceiling and maxlpt methods.
The results are then written to a summary CSV file (summary_table.csv) and printed in a LaTeX table format that can be included in a research paper or report.
The summary table includes the pattern name, the number of timeouts out of total instances, mean enumeration time, mean and maximum runtimes for both methods, providing a clear overview of the verification performance across different patterns.
The created summary CSV file is saved in the data/test_big_results_by_pattern/ directory, and the LaTeX table is printed to the console for easy copying into a LaTeX document.
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

csv_path = "data/test_big_results_20260311_235529.csv"

# Read all rows and group by pattern
pattern_rows = {p: [] for p in patterns}
with open(csv_path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["scheme"] in pattern_rows:
            pattern_rows[row["scheme"]].append(row)

summary = []
for pattern in patterns:
    rows = pattern_rows[pattern]
    n = len(rows)
    timeout = sum(1 for row in rows if row["verification_status"] == "TIMEOUT")
    enum_times = [float(row["enumeration_runtime"]) if row["verification_status"] != "TIMEOUT" else 3600.0 for row in rows]
    mean_enum_time = np.mean(enum_times) if enum_times else float('nan')
    ceiling_runtimes = [float(row["bnb_ceiling_runtime"]) for row in rows]
    maxlpt_runtimes = [float(row["bnb_maxlpt_runtime"]) for row in rows]
    summary.append([
        pattern,
        timeout,
        n,
        mean_enum_time,
        np.mean(ceiling_runtimes) if ceiling_runtimes else float('nan'),
        np.mean(maxlpt_runtimes) if maxlpt_runtimes else float('nan'),
        np.max(ceiling_runtimes) if ceiling_runtimes else float('nan'),
        np.max(maxlpt_runtimes) if maxlpt_runtimes else float('nan'),
    ])

# Write summary CSV
header = [
    "Pattern", "Timeouts", "Total", "Mean_enum_time",
    "Mean Ceil", "Mean LPT", "Max Ceil", "Max LPT"
]
with open("data/test_big_results_by_pattern/summary_table.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in summary:
        writer.writerow(row)

# Print LaTeX table in correct format
print("\\begin{table}[htbp]")
print("\\centering")
print("\\caption{Verification and runtime summary by pattern}")
print("\\label{tab:pattern-verification-summary}")
print("\\begin{tabular}{lrrrrrrr}")
print("\\toprule")
print("Pattern & Timeouts & Mean\\_enum\\_time & Mean Ceil & Mean LPT & Max Ceil & Max LPT \\\\")
print("\\midrule")
for row in summary:
    # row: pattern, timeout, n, mean_enum_time, mean_ceil, mean_lpt, max_ceil, max_lpt
    timeouts_str = f"{row[1]}/{row[2]}"
    print(f"{row[0].replace('_', ' ').title()} & {timeouts_str} & {row[3]:.2f} & {row[4]:.4f} & {row[5]:.4f} & {row[6]:.4f} & {row[7]:.4f} \\")
print("\\bottomrule")
print("\\end{tabular}")
print("\\end{table}")