import numpy as np
import matplotlib.pyplot as plt

months = np.arange(1, 13)
city1 = np.random.randint(5, 30, 12)
city2 = np.random.randint(8, 33, 12)
city3 = np.random.randint(6, 28, 12)

# --- Averages ---
monthly_avg = (city1 + city2 + city3) / 3   # This gives us monthly average
overall_avg = (city1.mean() + city2.mean() + city3.mean()) / 3  # Overall average temperature

# --- Plot cities ---
plt.figure(figsize=(10, 6))
plt.plot(months, city1, 'b', label='City 1')
plt.plot(months, city2, 'k', label='City 2')
plt.plot(months, city3, 'g', label='City 3')

# --- Plot monthly average ---
plt.plot(months, monthly_avg, 'r--', linewidth=2,
         label='Monthly Avg')

# --- Plot overall average ---
plt.axhline(overall_avg, color='purple', linestyle=':',
         linewidth=2, label=f'Overall Avg ({overall_avg:.1f})')

plt.xlabel('Month')
plt.ylabel('Temperature')
plt.title('Temperatures with monthly and overall averages')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

