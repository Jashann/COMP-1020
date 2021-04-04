# IF SQUARE SUM DIAGONALS
import numpy as np

def ifSquare(arr):
    shape = arr.shape
    return shape[0] == shape[1] 

def sumDiagonal(arr):
    rd = 0
    ld = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                rd += arr[i][j]
            if i+j == len(arr) - 1:
                ld += arr[i][j]
    return (rd, ld)

arr = np.zeros((3,3), dtype=np.int64)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = i + j

print(arr)
if ifSquare(arr):
    print("The sum is:", sumDiagonal(arr))
else:
    print("Not square matrix")