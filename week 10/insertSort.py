import numpy as np
import random

def insertionSort(arr, indexItem):
    # indexItem -> itemToBeChanged
    correctIndex = 0
    foundLarger = False

    i = 0
    while i < indexItem and not foundLarger:
        if arr[i] > arr[correctIndex]:
            correctIndex = i
            foundLarger = True
        i+=1
        
    temp = arr[correctIndex]
    arr[correctIndex] = arr[indexItem]
    arr[indexItem] = temp

def caller(arr):
    for i in range(1, len(arr)):
        insertionSort(arr, i)

list1 = list(range(1, 100))
arr = random.choices(list1, k=5)
arr = np.random.randint(1, 100, size=10)

print(arr)
caller(arr)
print(arr)
