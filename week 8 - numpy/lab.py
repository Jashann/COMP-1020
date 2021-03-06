# import random

# def isPrime(num):
#     count = 1 # as every is divisible by 1

#     for i in range(2, num):
#         divisible = isDivisible(num, i)
#         if divisible:
#             count += 1

#     prime = count == 1
#     return prime 

# def isDivisible(x, y):
#     divisible = False
#     if x%y == 0:
#         divisible = True
    
#     return divisible


# num = random.randint(1, 100)
# if isPrime(num):
#     print(num, "is prime")
# else:
#     print(num, "is not prime")



import random

def isPerfect(num):
    sum = 1
    for i in range(2, num):
        divisible = isDivisible(num, i)
        if divisible:
            sum += i
    
    return sum == num

def isDivisible(x, y):
    return x%y == 0

num = random.randint(1, 100)
if isPerfect(num):
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")