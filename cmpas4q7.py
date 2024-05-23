import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare

score = np.linspace(2, 12, 11)
prob = np.concatenate((np.linspace(1/36, 6/36, 6), np.flip(np.linspace(1/36, 6/36, 6))[1:]))
observed_counts_1 = [4, 10, 10, 13, 20, 18, 18, 11, 13, 14, 13]
n1 = np.sum(observed_counts_1)
observed_counts_2 = [3, 7, 11, 15, 19, 24, 21, 17, 13, 9, 5]
n2 = np.sum(observed_counts_2)

chi2_stat_1, p_val_1 = chisquare(observed_counts_1, f_exp = n1 * prob)
chi2_stat_2, p_val_2 = chisquare(observed_counts_2, f_exp = n2 * prob)

# Function to interpret p-value
def interpret_p_value(p_val):
    if p_val < 0.01:
        return "not sufficiently random"
    elif p_val < 0.05:
        return "suspect"
    elif p_val < 0.1:
        return "almost suspect"
    else:
        return "sufficiently random"

# Interpretation of results
result_1 = interpret_p_value(p_val_1)
result_2 = interpret_p_value(p_val_2)

print(f"Run 1 : χ² statistic = {chi2_stat_1:.2f}, p-value = {p_val_1:.4f}, result = {result_1}")
print(f"Run 2 : χ² statistic = {chi2_stat_2:.2f}, p-value = {p_val_2:.4f}, result = {result_2}")
