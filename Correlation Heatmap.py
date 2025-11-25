import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import figure

# Generate sample data
np.random.seed(42)  # for reproducibility
data = pd.DataFrame({
    'Height': np.random.randint(150, 200, 50),
    'Weight': np.random.randint(50, 100, 50),
    'Age': np.random.randint(18, 65, 50),
    'Income': np.random.randint(20000, 100000, 50),
    'Score1': np.random.randint(0, 100, 50),
    'Score2': np.random.randint(0, 100, 50)
})

# Computer correlation
corr_matrix = data.corr()   # corr() - computes the pairwise correlation between all columns

# Plot heatmap
fig, ax = plt.subplots(figsize=(8,6))
cax = ax.imshow(corr_matrix, cmap='coolwarm', vmin=-1, vmax=1)

# Add value labels
for i in range(corr_matrix.shape[0]):
    for j in range(corr_matrix.shape[1]):
        text = ax.text(j, i, f"{corr_matrix.iloc[i, j]:.2f}",
                       ha="center", va="center", color="black")

ax.set_xticks(np.arange(len(corr_matrix.columns)))
ax.set_yticks(np.arange(len(corr_matrix.columns)))
ax.set_xticklabels(corr_matrix.columns)
ax.set_yticklabels(corr_matrix.columns)
plt.xticks(rotation=45)

# Add colorbar
cbar = fig.colorbar(cax, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('Correlation coefficient')

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
