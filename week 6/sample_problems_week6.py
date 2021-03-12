""" Program 1 """

def returnsListStartsWithA(names):
    newList = []
    for name in names:
        if name[0].lower() == "a":
            newList.append(name)
    return newList

# namesList = ["Alice", "Amy", "Annie", "Rob", "Jack", "Katherine"]
# namesStartingA = returnsListStartsWithA(namesList)
# print(namesStartingA)


""" Program 2 """
def getDictionaryOfWords(list1):
    wordsDict = {}
    for string in list1:
        if " " in string:
            firstSpaceIndex = string.index(" ")
            firstWord = string[:firstSpaceIndex]
        else: 
            firstWord = string
        if firstWord not in wordsDict:
            wordsDict[firstWord] = []
        wordsDict[firstWord].append(string)

    return wordsDict
        
sentences = ["Smart work is better.", "Smart people", "Girl", "A Girl", "Hello World"]
myDict = getDictionaryOfWords(sentences)
print(myDict)