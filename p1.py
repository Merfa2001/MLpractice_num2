import numpy as np
random_array = np.random.randint(1, 101, 20)
mean = np.mean(random_array)
median = np.median(random_array)
std_dev = np.std(random_array)

print("Random Array:", random_array)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
#done