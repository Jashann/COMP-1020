import numpy as np

arr = np.zeros((4,4), dtype=np.int64)

# Filling
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = i + j

print(arr)
print()

# Accessing 3rd column
print(   arr[ : ,2]  )
print()

# Accessing 2rd row
print(   arr[1]  )
print()

# Accessing from 2nd row and from 3rd column 
print(   arr[ 1: , 2:  ]   )
print()

# Printing more than 4
print(    arr[ arr > 4 ]    )
print()