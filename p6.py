import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)  # Setting a seed for reproducibility
x = np.random.rand(100)  # 100 random x-coordinates between 0 and 1
y = np.random.rand(100)  # 100 random y-coordinates between 0 and 1

plt.scatter(x, y, color='blue', marker='o', alpha=0.5)  # 'alpha' controls point transparency
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Scatter Plot of Random (x, y) Coordinates')

plt.show()
#done