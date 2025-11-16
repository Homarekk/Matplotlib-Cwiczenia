import numpy as np
import matplotlib.pyplot as plt

days = np.arange(1, 31) # np.arange(start, stop, step) returns an arr with values
temps = np.random.randint(10, 32, size=30)
avg = temps.mean()  # mean() calculates average of a set of numbers

plt.figure(figsize=(10, 5)) # plt.figure() creates new figure 10 inches wide and 5 inches tall
plt.plot(days, temps, marker='o', label='Daily Temp')   # days on the x-axis and temps on the y-axis
plt.axhline(avg, color='red', linestyle='--', label=f'Avg Temp ({avg:.1f})')    # axhline() - axis horizontal line
plt.fill_between(days, temps, avg, where=temps>avg, alpha=0.3)

plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Daily temperature trend")
plt.legend()
plt.tight_layout()
plt.show()