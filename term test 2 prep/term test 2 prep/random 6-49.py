import random
import time
def chooseRandomNums():
    N = 5
    randomNumsSet = set()
    rangeToChooseFrom = list(range(1,50))

    while len(randomNumsSet) != N:
        randomNumsSet = set(random.choices(rangeToChooseFrom, k=N)) # 1 - 49

    return randomNumsSet

def ifTwoSetsSame(set1, set2):
    return set1 == set2


def doLottery():
    count = 0
    won = False

    while not won: 
        buyer = chooseRandomNums()
        winner = chooseRandomNums()
        won = ifTwoSetsSame(buyer, winner)
        count += 1
        
    print("Tries to win,", count)

startTime = time.time()
doLottery()
seconds = (time.time() - startTime)
print("Took", seconds)
