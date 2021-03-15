"""
author: Jashanjot Singh Gill
github: https://github.com/Jashann
portfolio: https://jashann.github.io/
email: jashangill3592@gmail.com
message: if you find a bug, please do let me know.
"""

import sys

""" Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file. """

""" 'sample.txt' -> CONTENT:
    Hello World
    I am Jashanjot Singh Gill
    I am just 
    Working with files
"""


""" FILE.READ() -> str [WHOLE TEXT]"""
# file = open("sample.txt", "r")
# print(file.read())
# print(file.read(5)) # reading first 5 characters


""" FILE.READLINE() -> str """
# file = open("sample.txt", "r")
# print(file.readline())
# print(file.readline())

""" FILE.READLINE() -> List """
# file = open("sample.txt", "r")
# listLines = file.readlines()

# for line in listLines:
#     print(line)



""" FILE HANDLE OBJECT --- READING WHOLE FILE """

# fhandle = open("sample.txt")

# for line in fhandle:
#     print(line)

# print()


""" FILE HANDLE OBJECT --- After iterating for first time fileHandle gets all cleared """
# fhandle2 = open("sample.txt")
    
# for line in fhandle2:
#     print(repr(line))


# fhandle = open("sample_users.txt")

""" FILE HANDLE OBJECT --- READING FILE USING  AND ITERATE OVER LINES PRINT ONLY NAMES """
# for line in fhandle: 
#     index = line.find("name:") # if line does not have name then it returns -1
#     if index != -1:
#         indexBeforeName = line.find(": ")
#         name = line[indexBeforeName+1:]
#         print("I am",line)


""" 
    EXERCISE 1 
    Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will look as follows:
    file download link: www.py4e.com/code3/mbox-short.txt
"""

def readFileAndUpperCaseText():
    try:
        fileHandler = open("mbox-short.txt")
    except:
        print("Something went wrong, maybe File does not exist in current directory")
        sys.exit()
        # NOTE: sys has to be imported above to use this
    
    for line in fileHandler:
        print(line.upper())

# readFileAndUpperCaseText()

"""
    Exercise 2
    When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.

    Output:
        Enter the file name: mbox.txt
        Average spam confidence: 0.894128046745

        Enter the file name: mbox-short.txt
        Average spam confidence: 0.750718518519
        Test your file on the mbox.txt and mbox-short.txt files.
"""
def readFileAndFindingSpamAverave(fileName):
    try:
        fileHandler = open(fileName)
    except:
        print("Something went wrong, maybe File does not exist in current directory")
        sys.exit()
        # NOTE: sys has to be imported above to use this
    
    totalSpam = 0
    count = 0
    for line in fileHandler:
        if line.find("X-DSPAM-Confidence:") == 0:
            """ line = X-DSPAM-Confidence: 0.7606 """
            index = line.find(": ")
            totalSpam = totalSpam + float(line[index+2:])
            count += 1
    averageSpam = totalSpam / count
    print("Average spam confidence:", averageSpam )

# fileName = input("Enter a file name located in current directory > ")
# readFileAndFindingSpamAverave(fileName)


"""
    Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program. Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name “na na boo boo”. The program should behave normally for all other files which exist and don’t exist. Here is a sample execution of the program:

    Output:
        python egg.py
        Enter the file name: mbox.txt
        There were 1797 subject lines in mbox.txt

        python egg.py
        Enter the file name: missing.tyxt
        File cannot be opened: missing.tyxt

        python egg.py
        Enter the file name: na na boo boo
        NA NA BOO BOO TO YOU - You have been punk'd!
"""



def easterEgg(fileName):
    try:
        fileHandler = open(fileName)
    except:
        if fileName == "na na boo boo":
            print("NA NA BOO BOO TO YOU - You have been punk'd!")
        else:
            print("File cannot be opened:", fileName)
        sys.exit()
        # NOTE: sys has to be imported above to use this
    

    countLines = 0
    for line in fileHandler:
        countLines += 1
    
    print("There were {} subject lines in mbox.txt".format(countLines))

fileName = input("Enter a file name located in current directory > ")
easterEgg(fileName)