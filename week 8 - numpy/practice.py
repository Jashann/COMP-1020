"""
    https://numpy.org/devdocs/user/absolute_beginners.html#basic-array-operations
"""

import numpy as np

# Creating or initailing Numpy array
arr = np.zeros((2,3), dtype="int")
arr2 = np.ones((3,3,), "int8")
arr3 = np.full((2,2), 10, dtype="int16") 
arr4 = np.array([ [1,2,3,5], [5,6,7,8] ])
arr5 = np.empty((2,3,2), "int32")
arr6 = np.arange(2,10,2)
arr7 = np.linspace(0,10, num=3)
# print(arr7)
# print(arr7.size)



# Sorting, adding, removing
arr = np.array([5,3,1])
arr2 = np.arange(10,1, -1)

# arr.sort()
arr3 = np.concatenate((arr, arr2), axis=0) 
# print(arr3)



# shape and size of an array
arr2 = np.empty((2,4,4))
# print(arr2)
# print(arr2.ndim)
# print(arr2.size, arr2.shape)



# Indexing and slicing
arr = np.arange(1, 10, 1)
# print(arr[1:])

# Conditions
# print(arr<5)
# print(arr[arr<=5])

divisible_by_2 = arr[arr%2==0]
# print(divisible_by_2)

c = arr[(arr > 2) & (arr < 5)]
# print(c)





# Basic array operations
arr = np.arange(1, 50, 10)
arr2 = np.arange(1, 6, 1)

# print(arr)
# print(arr2)
# print(arr + arr2)
# print(arr - arr2)
# print(arr / arr2)
# print(arr * arr2)

# print(arr.max(), arr.sum())




# Random numbers
arr = np.random.random(5)
# print(arr)


rng = np.random.default_rng()
arr = rng.integers(low=0, high=10, size=3)
# print(arr)


# Reshaping
arr = np.full((3,3), 10)
# print(arr)

arr.resize((5,2))
# print(arr)


# How to reverse an array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
arr = np.flip(arr)
# print(arr)
# print(help(np.flip))




## Saving
#a = np.array([1, 2, 3, 4, 5, 6])
#
## You can save it as “filename.npy” with:
#np.savetxt('new_file.csv', a)
## np.save('filename', a)
#
#b = np.load('filename.npy')
## print(b)


import matplotlib.pyplot as plt
import numpy as np
np.random.seed(444)

plt.scatter(1,2)






