import sys

"""
    Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
"""

def chop(listOfItems):
    listOfItems.pop(0)
    length = len(listOfItems) - 1
    listOfItems.pop(length)
    return None

def middle(listOfItems):
    length = len(listOfItems)  - 1
    return listOfItems[1:length]

listOfNumbers = [1,2,3,4]
# chop(listOfNumbers)
# print(listOfNumbers)
# print(middle(listOfNumbers))



"""
    Exercise 4: Download a copy of the file www.py4e.com/code3/romeo.txt. Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function. For each word, check to see if the word is already in a list. If the word is not in the list, add it to the list. When the program completes, sort and print the resulting words in alphabetical order.
"""
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


"""
    Exercise 5: Write a program to read through the mail box data and when you find line that starts with “From”, you will split the line into words using the split function. We are interested in who sent the message, which is the second word on the From line.
    From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
"""

def readFileAndFindSender():
    file = open("z_mbox-short.txt")
    count = 0
    for line in file:
        if line[0:4] == "From":
            print(line.split()[1])
            count += 1
    print("There were {} lines in the file with From as the first word".format(count))

# readFileAndFindSender()


"""
    Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.
"""

def findMixAndMax():
    exit = False
    numbers = []
    while not exit:
        userInput = input("Enter a number: ")
        if userInput == "done":
            exit = True
        elif userInput.isnumeric():
            number = int(userInput)
            numbers.append(number)
        else:
            print("Invalid Input, Enter a number") 

    print("Maximum: ",max(numbers))
    print("Minimum: ",min(numbers)) 
            
findMixAndMax()