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