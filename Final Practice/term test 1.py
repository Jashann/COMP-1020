import numpy as np
theSum = 0
a = np.array([[1,2,3],[4,5,6],[4,4,4],[10,11,12]])
for i in range(len(a)):
   for j in range(len(a[i])):
       if j == 2:
           theSum += a[i][j]
print(theSum)