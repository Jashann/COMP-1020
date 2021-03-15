import random

TRAILS = 1000
YAHTZEE = 5

random.seed(1500)

def makeADiceRoll():
    """
    make dices roll, returns 1 to 6
    """
    return random.randint(1,6)

def makeDiceRoll_ReturnResult():
    results = []
    for i in range(YAHTZEE):
        results.append( makeADiceRoll() )
    return results

def ifAllSame(results):
    """
        returns True or False  
    """
    ifAllSame = True

    for result in results:
        if result != results[0]:
            ifAllSame = False

    return ifAllSame

def findStats():
    
    ifSame = False
    count = 0
    while not ifSame:
        results = makeDiceRoll_ReturnResult()
        ifSame = ifAllSame(results)
        count += 1

    return count

def findProbability():
    """
    returns average of trails
    """
    trailsCount = []
    for i in range(TRAILS):
        trailsCount.append(findStats())

    avg = sum(trailsCount)/len(trailsCount)

    return avg

print(findProbability())