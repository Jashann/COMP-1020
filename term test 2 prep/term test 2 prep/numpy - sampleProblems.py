# IF SQUARE MATRIX, SUM DIAGONALS
import numpy as np


def changeDiagonal(arr):
    shape = arr.shape
    isSquare = shape[0] == shape[1] 

    if isSquare:
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if i == j or i+j == len(arr) - 1:
                    arr[i][j] += 1
    else:
         print("The array is not square")

    





arr = np.zeros((3,5), dtype=np.int64)


for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = i + j

print(arr)
changeDiagonal(arr)
print(arr)