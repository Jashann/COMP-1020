import numpy as np
from numpy.core.fromnumeric import size

np.random.seed(100)

numbers = np.random.random(size= 100)


below05 = 0

for num in numbers:
    if num < 0.5:
        below05 += 1

below05Arr = numbers[numbers < 0.5]

print(len(below05Arr)/len(numbers))
print(below05/len(numbers))