import time
import random

def doLottery():
    list1 = list(range(1, 50))
    winningTickets = random.choices(list1, k=NUM)
    ourTickets = random.choices(list1, k=NUM)

    return checkIfSame(winningTickets, ourTickets)

def checkIfSame(list1, list2):
    return sorted(list1) == sorted(list2)

def toWinLottery():
    count = 0
    won = False

    while not won:
       won = doLottery()
       count += 1

    return count

# MAIN
NUM = 6

startTime = time.time()

counts = toWinLottery()
print(f"It took {counts} tries to win")

print("Time took:", time.time() - startTime)
