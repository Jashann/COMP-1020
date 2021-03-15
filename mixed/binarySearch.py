def binarySearch(numList, num):
    numFound = False
    index = None

    lowerBound = 0
    upperBound = len(numList)
    
    numIsInList = True


    while not numFound and numIsInList:
        
        midIndex = (upperBound + lowerBound) // 2
        midValue = numList[midIndex]

        if num == midValue:
            numFound = True
            index = midIndex

        elif num < midValue:
            upperBound = midIndex - 1
        
        elif num > midValue:
            lowerBound = midIndex + 1

        if lowerBound > upperBound:
            numIsInList = False

    if numFound:
        print(numList[index] ," is in list at index ", index)       
    else:
        print(num, "is not in list")     

list1 = [1,2,39,53,668,2321]
numToBeSearched = 2

binarySearch(list1, numToBeSearched)