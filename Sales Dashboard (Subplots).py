import numpy as np
import matplotlib.pyplot as plt

months = np.arange(1, 13)
sales = np.random.randint(2000, 6000, 12)
profit = np.random.randint(500, 3000, 12)
expense = sales - profit
margin = profit / sales

fig, ax = plt.subplots(3, 1, figsize=(10, 10))

ax[0].bar(months, sales)
ax[0].set_title("Monthly sales")

ax[1].plot(months, profit, label='Profit')
ax[1].plot(months, expense, label='Expense')
ax[1].legend()

ax[2].scatter(months, margin)
ax[2].set_title("Profit Margin")

plt.tight_layout()
plt.show()

