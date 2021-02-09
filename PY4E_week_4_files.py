"""
author: Jashanjot Singh Gill
github: https://github.com/Jashann
portfolio: https://jashann.github.io/
email: jashangill3592@gmail.com
message: if you find a bug please do let me know.
"""


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
