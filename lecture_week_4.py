"""
author: Jashanjot Singh Gill
github: https://github.com/Jashann
portfolio: https://jashann.github.io/
email: jashangill3592@gmail.com
message: if you find a bug please do let me know.
"""

def readFileAndPrintLettersInEachLine():
    lineNumber = 0
    for line in file:
        letterInEachLine = 0
        for letter in line:
            if letter.isalnum():
                letterInEachLine += 1
        print("Line {} has these many characters {}".format(lineNumber, letterInEachLine))
        lineNumber += 1

readFileAndPrintLettersInEachLine()