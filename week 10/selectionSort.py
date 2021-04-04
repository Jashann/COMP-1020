import numpy as np
import random

def locateLargest(arr, indexUpto):
    largestIndex = 0
    for i in range(indexUpto):
        if arr[i] > arr[largestIndex]:
            largestIndex = i
    
    temp = arr[largestIndex]
    arr[largestIndex] = arr[indexUpto - 1]
    arr[indexUpto - 1] = temp

def caller(arr):
    for i in range(len(arr)):
        locateLargest(arr, len(arr) - i)

list1 = list(range(1, 100))
# arr = random.choices(list1, k=5)
arr = np.random.randint(1, 100, size=10)

print(arr)
caller(arr)
print(arr)
