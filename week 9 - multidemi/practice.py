import numpy as np

arr = np.ndarray((4,7), dtype=np.int64)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = i*j

print(arr)