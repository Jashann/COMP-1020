import numpy as np

np.random.seed(1012)
SIZE = 5
MAX_VALUE = 100
data = np.random.randint(0, MAX_VALUE, size=SIZE)

# Linear Sort
def swap(array):
    for i in range(len(array)):
        if i+1 < len(array) - 1:
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
def caller():
    print(data)
    for _ in range(len(data)):
        swap(data)

    print(data)

# caller()


# Bubble sort
def checkIfSorted(array, lastIndex):
    sorted = True
    for i in range(lastIndex):
        if array[i] > array[i+1]:
            sorted = False
            # Swapping
            array[i], array[i+1] = array[i+1], array[i]
    return sorted


def callerForBubbleSort(array):
    finished = False
    lastIndex = len(array) - 1

    while not finished and lastIndex > 0:
        finished = checkIfSorted(array, lastIndex)
        lastIndex -= 1

print(data)                   
callerForBubbleSort(data)
print(data)