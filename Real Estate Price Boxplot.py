import numpy as np
import matplotlib.pyplot as plt

data = [np.random.randint(200000, 500000, 100) for _ in range(4)]
overall_mean = np.mean(np.concatenate(data))    # np.concatenate() combines all 4 arrays into one long array

plt.figure(figsize=(8, 6))

boxes = plt.boxplot(data, patch_artist=True)    # patch_artist=True → allows filling the boxes with color (otherwise boxes are just outlines)

colors = ['#ff9999', '#99ff99', '#9999ff', '#ffcc99']

# Apply colours
for box, color in zip(boxes['boxes'], colors):  # zip() pairs each box with a color
    box.set(facecolor=color)

plt.axhline(overall_mean, color='red', linestyle='--', label=f'Overall Mean: {overall_mean:.0f}')
plt.title("Real Estate Prices by Neighborhood")
plt.xticks([1, 2, 3, 4], ['A', 'B', 'C', 'D'])

plt.legend(loc='upper left')
plt.show()