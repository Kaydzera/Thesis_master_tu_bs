# Script to compute the upper bound on the number of feasible selections and the estimated runtime
import math

n = 10
B = 100
prices = [5 + i for i in range(n)]  # p_i in [5, 15]

# Compute the max number of copies for each item
def max_copies(B, prices):
    return [B // p for p in prices]

max_copies_list = max_copies(B, prices)

# Compute the upper bound on the number of combinations
upper_bound = 1
for m in max_copies_list:
    upper_bound *= (m + 1)

# Estimate runtime (in seconds, days, years) for 1 ms per combination
time_per_comb_ms = 1
seconds = upper_bound * time_per_comb_ms / 1000
minutes = seconds / 60
hours = minutes / 60

days = hours / 24
years = days / 365.25

print(f"n = {n}, B = {B}, prices = {prices}")
print(f"Max copies per item: {max_copies_list}")
print(f"Upper bound on number of combinations: {upper_bound:.2e}")
print(f"Estimated runtime at 1 ms per combination:")
print(f"  Seconds: {seconds:.2e}")
print(f"  Days:    {days:.2f}")
print(f"  Years:   {years:.2f}")
