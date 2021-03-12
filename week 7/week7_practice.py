import random

num = random.random()*11 # random number from 0 to 11

list1 = [1,2,3,4,5,6,7,8,9,10]
random.choice(list1) # random choice from a sequence

num2 = random.randrange(2,4,2) # exclusive of the last number i.e -> 4
num3 = random.randint(2,4) # including endpoints

print(num3)