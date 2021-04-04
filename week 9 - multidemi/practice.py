# # import numpy as np

# # arr1 = np.arange(0,9)
# # arr = np.ndarray((3,3), dtype=np.int64, buffer= arr1)


# # # print(help(np.ndarray))

# # # print(arr, end="\n\n")

# # # # Even, Conditions
# # # # print(arr[arr%2==0])
# # # # print(arr[arr>4])

# # # # 1st Row and column
# # # # print(arr[0])
# # # # print( arr[ : ,1 ] )

# # # # Odd Columns and Rows
# # # # print(arr[ : , 1: :2])
# # # # print(arr[ 1:  :2  ])


# # # # Assigning using random numbers
# # # # arr4 = np.random.randint(1,10, (3,3))
 
# # # print(arr + 3)


# # # # import matplotlib.pyplot as plt
# # # # import numpy as np
# # # # print(arr4[ : ,0], arr4[ : ,1])
# # # # plt.scatter(arr4[ : ,0], arr4[ : ,1])


# # arr2 = np.ndarray((10,2), dtype=np.int64, buffer=np.array(range(0,20)))
# # pointX = 10
# # pointY = 12
# # distances = np.sqrt(np.square(arr2[ : , 0] - pointX) + np.square(arr2[ : , 1] - pointY))
# # print(distances)
# # print(arr2)
# # print(np.cumsum(arr2, 1))



# import numpy as np
# def smallSlice(arr):
#     new = arr[arr < 50]
#     return new

# def smallLoops(arr):
#     count = 0
#     for it in arr:
#         if it < 50:
#             count += 1

#     new = np.zeros(count)

#     count = 0 
#     for i in range(len(arr)):
#         it = arr[i]
#         if it < 50:
#             new[count] = it
#             count += 1

#     return new 

# arr = np.array([1,341,213,12])

# print(smallLoops(arr))

