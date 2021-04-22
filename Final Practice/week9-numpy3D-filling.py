"""
Question 3: 
Create a 2D numpy array with 4 rows and 7 columns
Fill the array to create a multiplication table, where each item is the row number * the column number
"""

import numpy as np

arr = np.zeros((4,7), dtype= np.int64)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = i * j 

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end="\t")
    print()

    