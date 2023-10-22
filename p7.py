import numpy as np

matrix1 = np.random.rand(2, 3)
matrix2 = np.random.rand(3, 4)

result = np.dot(matrix1, matrix2)

print("Matrix 1 (2x3):")
print(matrix1)
print("\nMatrix 2 (3x4):")
print(matrix2)
print("\nMatrix Multiplication Result (2x4):")
print(result)
#done