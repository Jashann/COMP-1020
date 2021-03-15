def readFileAndSplit():
    fileHandle = open("tempfile.txt")

    # create list
    wordsList = []

    for line in fileHandle: # for loop runs for 4 times
        lineWordsList = line.split()
        for lineWord in lineWordsList:
            if not lineWord in wordsList:
                wordsList.append(lineWord)

    wordsList.sort()
    print(wordsList)

def random():
    data = [1,65,2,24,3]

    total = 0

    for number in data:
            if number % 2 == 0:
                    total += number

    print(total)



    for i in range(0, len(data), 3 ):
            print(data[i]) 

