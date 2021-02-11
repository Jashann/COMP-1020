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
