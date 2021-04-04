def loadDict(list):
    newList = []
    for str in list:
        words = str.split()
        if len(words) == 3:
            newList.append(str)

    print(newList)





listOfStr = ["hello world", "Jashan jot singh", "hello Jashan", "no at all", "hurrah "]

loadDict(listOfStr)