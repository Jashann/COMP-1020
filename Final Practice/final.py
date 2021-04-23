def addOdds(fileName):
    fileHandler = open(fileName)
    uniqueOdds = set()

    for line in fileHandler:
        arr = line.split(",")
        for num in arr:
            num = int(num)
            if num % 2 != 0:
                uniqueOdds.add(num)
    
    return sum(uniqueOdds)

fileName = "sample.txt"
# print(addOdds(fileName))

def calculateEq(x):
    result = 0
    for i in range(x):
        result = 10 * i
        for j in range(x+x):
            result *= (i - 10) ** 2
    return result

print(calculateEq(3))