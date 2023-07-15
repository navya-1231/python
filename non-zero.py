import numpy as np

# Create the original array
arr = np.array([[0, 10, 20], [20, 30, 40]])

print("Original array:")
print(arr)

# Count the number of non-zero elements
count = np.count_nonzero(arr)

print("Number of non-zero elements in the above array:", count)
