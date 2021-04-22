import numpy as np
from numpy.core.records import array

arr = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)

print(arr)
print()

# Column 1st
print(arr[ : , 0])
print()

# row 2nd
print(arr[1 , : ], "\n")

# row 2 to 3 & column 1 to 2
print(arr[1:3, 0:2], "\n")


# Conditionals
print(arr[arr > 5], "\n")