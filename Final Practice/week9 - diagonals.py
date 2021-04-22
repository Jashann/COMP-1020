import numpy as np




def isSquare(arr):
    shape = arr.shape
    return shape[0] == shape[1]


def addDiagonals(arr):
    rd = 0
    ld = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                ld += arr[i][j]
            if i + j == len(arr) - 1:
                rd += arr[i][j]
    
    return (ld, rd)


# MAIN
arr = np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]]
     )

if isSquare(arr):
    tup = addDiagonals(arr)
    print("Sum is", tup)
else:
    print("Not square")
