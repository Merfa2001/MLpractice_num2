import numpy as np

arr1 = np.random.randint(1, 101, (5, 5))
arr2 = np.random.randint(1, 101, (5, 5))

addition_result = arr1 + arr2

subtraction_result = arr1 - arr2

multiplication_result = arr1 * arr2

division_result = np.divide(arr1, arr2, out=np.zeros_like(arr1), where=arr2 != 0)

print("Array 1:")
print(arr1)
print("\nArray 2:")
print(arr2)
print("\nElement-wise Addition:")
print(addition_result)
print("\nElement-wise Subtraction:")
print(subtraction_result)
print("\nElement-wise Multiplication:")
print(multiplication_result)
print("\nElement-wise Division:")
print(division_result)
#done
