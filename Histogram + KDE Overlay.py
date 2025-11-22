import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

data = np.random.normal(50, 10, 1000)  # Generate values with mean = 50, std = 10 and size of 1000
kde = gaussian_kde(data)    # Creates KDE object trained on the data

xs = np.linspace(min(data), max(data), 300) # Evenly spaced values from data, so program can draw KDE line

plt.figure(figsize=(8, 5))
plt.hist(data, bins=100, density=True, alpha=0.5) # density=True is used to represent probability density function
plt.plot(xs, kde(xs))   # kde is callable

mean = data.mean()
std = data.std()
plt.axvline(mean, color='red', linestyle='--')
plt.axvline(mean+std, color='green', linestyle='--')
plt.axvline(mean-std, color='green', linestyle='--')

plt.title("Histogram + KDE")
plt.tight_layout()
plt.show()

