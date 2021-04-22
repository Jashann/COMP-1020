import random

def rollNNumbers(n):
    list1 = list(range(1,6))
    return random.choices(list1, k=n)

def checkIfAllSame(list1):
    same = True
    item1st = list1[0]

    for item in list1:
        if item != item1st:
            same = False

    return same

def howManyTillAllSame():
    """
    Gets a Yahtzee
    """
    gotYahtzee = False
    count = 0

    while not gotYahtzee:
        randomNumbers = rollNNumbers(HOW_MANY_TO_ROLL)
        gotYahtzee = checkIfAllSame(randomNumbers)
        count += 1

    return count


def doManyTrails(n):
    afterHowManyGotYahtzee = []

    for _ in range(n):
        whenGotYahtzee = howManyTillAllSame()
        afterHowManyGotYahtzee.append(whenGotYahtzee)

    return afterHowManyGotYahtzee

def printStats(list1):
    average = sum(list1) / len(list1)
    print(f"The average Yahtzee was after {average:.2f} rolls")

# MAIN
HOW_MANY_TO_ROLL = 5
TRAILS = 1000

afterHowManyGotYahtzee = doManyTrails(TRAILS)
printStats(afterHowManyGotYahtzee)