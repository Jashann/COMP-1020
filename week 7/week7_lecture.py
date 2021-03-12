import random
from typing import Sequence

# headCount = 0
# tailCount = 0
# flips = 100

# while headCount != 50 and tailCount != 50:
#     draw = random.randint(0,1)

#     print(draw)
#     if draw == 1:
#         headCount += 1
#     if draw == 0:
#         tailCount += 1

#     flips = flips - 1

#     if flips == 0:
#         flips = 100
#     print(flips)


# print(headCount, tailCount)


from itertools import count
import random



def giveRandomNumber():
    return random.randint(0,51)
    
def main():
    cardPairs = {}
    count = 100
    while count > 0:
        number = giveRandomNumber()
        mod = number % 13
        if mod not in cardPairs:
            cardPairs[str(mod)] = 0
        cardPairs[str(mod)] += 1 
        count -= 1

    print(cardPairs)

main()