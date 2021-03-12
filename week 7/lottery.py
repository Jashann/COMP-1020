import random 
import time

SELECT_NUMS = 6
RANGE_NUMS = 70

def getRandomNumbers(list, selectNum):
    return random.choices(list, k= selectNum)

def ifSame(list1,list2):
    """
    Checks if two lists are the same
    Returns -> Boolean
    """

    list1.sort()
    list2.sort()
    return list1 == list2

def doLottery():
    numbers = list(range(1,RANGE_NUMS))
    winning = getRandomNumbers(numbers, SELECT_NUMS)
    gotLottery = getRandomNumbers(numbers, SELECT_NUMS)

    return ifSame(winning, gotLottery)
    
def lotteryWinWhatTime():
    startTime = time.time()

    win = False
    count = 0
    while not win:
        count += 1
        win = doLottery()
    
    finalTime = time.time() - startTime
    
    print(f'Lottery after {count} tries. Time taken in seconds: {finalTime}')


# print(lotteryWinWhatTime())
list1 = [1,3,2,1]
list2 = [1,1,2,3]
print(ifSame(list1, list2))