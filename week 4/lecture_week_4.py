"""
author: Jashanjot Singh Gill
github: https://github.com/Jashann
portfolio: https://jashann.github.io/
email: jashangill3592@gmail.com
message: if you find a bug, please do let me know.
"""

def readFileAndPrintLettersInEachLine():
    file = open("z_sample.txt")
    lineNumber = 0
    for line in file:
        letterInEachLine = 0
        for letter in line:
            if letter.isalnum():
                letterInEachLine += 1
        print("Line {} has these many characters {}".format(lineNumber, letterInEachLine))
        lineNumber += 1

# readFileAndPrintLettersInEachLine()



def quiz04():
    userInput = "z_sample.txt"

    myFile = open(userInput)
    count = 0

    for line in myFile:
        wordsInALine = line.split()
        count += len(wordsInALine)

    print("Total number of words:", count)

# quiz04()


def practice():
    name = "Jashanjot"
    age = 19
    # FORMATTED STRINGS
    print(f"hey {name}, I am {age+2} years old")


practice()