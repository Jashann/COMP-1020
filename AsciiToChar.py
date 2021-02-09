"""
author: Jashanjot Singh Gill
github: https://github.com/Jashann
portfolio: https://jashann.github.io/
email: jashangill3592@gmail.com
message: if you find a bug please do let me know.
"""


import sys

""" 
    Program - ASSCI values To Characters
"""
def _ASSCIToChar(ascii):
    try:
        return chr(ascii)
    except:
        return "Wrong input!"


# exit = False
# while not exit:
#     userInput = input("Enter a value in \"ASCII\" code or \"exit\" to stop program > ")
#     if userInput == "exit":
#         sys.exit("The program ended")
#     ascii = int(userInput)
#     print(_ASSCIToChar(ascii))





def charToASCII(char):
    try:
        return ord(char)
    except:
        return "Wrong input!"

exit = False

while not exit:
    userInput = input("Enter a \"character\" or \"exit\" to stop program > ")
    if userInput == "exit":
        sys.exit("The program ended")
    print(charToASCII(userInput))