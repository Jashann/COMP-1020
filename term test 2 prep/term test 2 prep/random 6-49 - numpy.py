import numpy as np
import time

def giveNNumbers():
    N = 5
    arr1 = np.arange(1,50)
    sample = np.random.choice(arr1, (N))
    return sample


def ifSameNumbers(arr1, arr2):
    arr1.sort()
    arr2.sort()
    originalLen = len(arr1)
    checked = arr1[ arr1== arr2]
    checkedLen = len(checked)

    return originalLen == checkedLen

def doLottery():
    count = 0
    won = False

    while not won: 
        buyer = giveNNumbers()
        winner = giveNNumbers()
        won = ifSameNumbers(buyer, winner)
        count += 1
        
    print("Tries to win,", count)

startTime = time.time()
doLottery()
seconds = (time.time() - startTime)
print(f"Took {seconds:.0f} seconds")