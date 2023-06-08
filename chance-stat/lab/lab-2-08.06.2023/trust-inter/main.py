import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

data = [69, 70, 68, 70, 70, 67, 70, 70, 68, 69, 70, 71, 70, 69, 67, 69, 69, 67, 67, 67, 67, 72, 74, 72, 69, 71, 70,
        71, 73, 66, 68, 69, 69, 72, 70, 72, 68, 71, 69, 70, 71, 69, 69, 69, 65, 68, 73, 69, 69, 67, 65, 67, 68, 66,
        67, 72, 69, 69, 68, 68, 68, 71, 67, 65, 65, 70, 68, 72, 69, 71, 67, 72, 70, 71, 68, 69, 70, 71, 71, 66, 68,
        66, 68, 72, 71, 70, 71, 65, 68, 69, 67, 70, 71, 67, 69, 73, 66, 71, 63, 69, 68, 68, 70, 73]

mean = np.mean(data)
std_dev = np.std(data, ddof=1)

confidence_level = 0.95
z = stats.norm.ppf(1 - (1 - confidence_level) / 2)
margin_of_error = z * (std_dev / np.sqrt(len(data)))
confidence_interval_for_mean = (mean - margin_of_error, mean + margin_of_error)

n = len(data)
alpha = 1 - confidence_level
chi2_lower = stats.chi2.ppf(alpha / 2, df=n - 1)
chi2_upper = stats.chi2.ppf(1 - alpha / 2, df=n - 1)
confidence_interval_for_std = ((n - 1) * std_dev ** 2 / chi2_upper, (n - 1) * std_dev ** 2 / chi2_lower)
confidence_interval_for_std = (np.sqrt(confidence_interval_for_std[0]), np.sqrt(confidence_interval_for_std[1]))
print("Mean: ", mean)
print("Std_dev: ", std_dev)
print("N: ", len(data))
print("Gamma: ", confidence_level)

print(f'95% confidence interval for the mean: {confidence_interval_for_mean}')
print(f'95% confidence interval for the standard deviation: {confidence_interval_for_std}')

confidence_levels = np.linspace(0.1, 0.99, 100)
lower_bounds = []
upper_bounds = []

for confidence_level in confidence_levels:
    z = stats.norm.ppf(1 - (1 - confidence_level) / 2)
    margin_of_error = z * (std_dev / np.sqrt(n))
    confidence_interval = (mean - margin_of_error, mean + margin_of_error)
    lower_bounds.append(confidence_interval[0])
    upper_bounds.append(confidence_interval[1])

plt.figure(figsize=(10, 6))
plt.plot(confidence_levels, lower_bounds, label='Lower bound')
plt.plot(confidence_levels, upper_bounds, label='Upper bound')
plt.title('Confidence Intervals for Different Confidence Levels')
plt.xlabel('Confidence Level')
plt.ylabel('Confidence Interval')
plt.legend()
plt.grid(True)
plt.show()

sample_sizes = range(10, 1001, 10)
lower_bounds = []
upper_bounds = []

for sample_size in sample_sizes:
    z = stats.norm.ppf(1 - (1 - 0.95) / 2)
    margin_of_error = z * (std_dev / np.sqrt(sample_size))
    confidence_interval = (mean - margin_of_error, mean + margin_of_error)
    lower_bounds.append(confidence_interval[0])
    upper_bounds.append(confidence_interval[1])

plt.figure(figsize=(10, 6))
plt.plot(sample_sizes, lower_bounds, label='Lower bound')
plt.plot(sample_sizes, upper_bounds, label='Upper bound')
plt.title('Confidence Intervals for Different Sample Sizes')
plt.xlabel('Sample Size')
plt.ylabel('Confidence Interval')
plt.legend()
plt.grid(True)
plt.show()

lower_bounds = []
upper_bounds = []

for confidence_level in confidence_levels:
    alpha = 1 - confidence_level
    chi2_lower = stats.chi2.ppf(alpha / 2, df=n-1)
    chi2_upper = stats.chi2.ppf(1 - alpha / 2, df=n-1)
    confidence_interval = ((n-1) * std_dev**2 / chi2_upper, (n-1) * std_dev**2 / chi2_lower)
    confidence_interval = (np.sqrt(confidence_interval[0]), np.sqrt(confidence_interval[1]))
    lower_bounds.append(confidence_interval[0])
    upper_bounds.append(confidence_interval[1])

plt.figure(figsize=(10, 6))
plt.plot(confidence_levels, lower_bounds, label='Lower bound')
plt.plot(confidence_levels, upper_bounds, label='Upper bound')
plt.title('Confidence Intervals for Standard Deviation for Different Confidence Levels')
plt.xlabel('Confidence Level')
plt.ylabel('Confidence Interval')
plt.legend()
plt.grid(True)
plt.show()

lower_bounds = []
upper_bounds = []

for sample_size in sample_sizes:
    alpha = 1 - 0.95
    chi2_lower = stats.chi2.ppf(alpha / 2, df=sample_size-1)
    chi2_upper = stats.chi2.ppf(1 - alpha / 2, df=sample_size-1)
    confidence_interval = ((sample_size-1) * std_dev**2 / chi2_upper, (sample_size-1) * std_dev**2 / chi2_lower)
    confidence_interval = (np.sqrt(confidence_interval[0]), np.sqrt(confidence_interval[1]))
    lower_bounds.append(confidence_interval[0])
    upper_bounds.append(confidence_interval[1])

plt.figure(figsize=(10, 6))
plt.plot(sample_sizes, lower_bounds, label='Lower bound')
plt.plot(sample_sizes, upper_bounds, label='Upper bound')
plt.title('Confidence Intervals for Standard Deviation for Different Sample Sizes')
plt.xlabel('Sample Size')
plt.ylabel('Confidence Interval')
plt.legend()
plt.grid(True)
plt.show()
