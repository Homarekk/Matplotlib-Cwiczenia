import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

months = np.arange(1, 13)
city1 = np.random.randint(5, 30, 12)
city2 = np.random.randint(8, 33, 12)
city3 = np.random.randint(6, 28, 12)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# --- Main Plot (Top) ---
ax1.plot(months, city1, 'b', label='City 1')
ax1.plot(months, city2, 'k', label='City 2')
ax1.plot(months, city3, 'g', label='City 3')

ax1.set_ylabel('Temperature')
ax1.set_xlabel('Month')
ax1.set_title("City Temperature Comparison")
ax1.legend()
ax1.grid(True, alpha=0.3)

# --- Zoomed Plot (Bottom) ---
ax2.plot(months, city1, 'b')
ax2.plot(months, city2, 'k')
ax2.plot(months, city3, 'g')

ax2.set_xlim(6, 8)
ax2.set_xlabel("Month")
ax2.set_ylabel("Temperature (Zoom)")
ax2.set_title("Zoomed-In View")
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

