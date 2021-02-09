"""
author: Jashanjot Singh Gill
github: https://github.com/Jashann
portfolio: https://jashann.github.io/
email: jashangill3592@gmail.com
message: if you find a bug, please do let me know.
"""


""" <----- Program 1 -----> """
""" APOSPWP Chapter 2 Exercises 2.1 """
def print_Fahrenheit_Celsus_Table():
    for i in range(0, 100, 10):
        fahrenheit = i
        print(fahrenheit, end=" ")

    print("")
        
    for i in range(0, 100, 10):
        fahrenheit = i
        celsus = (fahrenheit - 32) * 5/9
        print("{:.4f}".format(celsus), end=" ")

    print("")
        
    for i in range(0, 100, 10):
        fahrenheit = i
        celsusApprox = (fahrenheit - 30)/2
        print("{:.4f}".format(celsusApprox), end=" ")

# print_Fahrenheit_Celsus_Table()

        
""" <----- Program 2 -----> """
""" APOSPWP Chapter 2 Exercises 2.4 """

def printEvenNumber():
    list = []
    count = 0
    n = int(input("Enter upper bound > "))
    while count < n:
        if(count%2 != 0):
            list.append(count)
        count += 1
    print(list)

# printEvenNumber()


""" <----- Program 3 -----> """
""" Ask for input for a string. Ask for input of a letter. Count the number of that letter in the given string """
def countString():
    str = input("Enter a sentence > ")
    letter = input("Enter a letter to get count of it > ")
    count = 0
    for char in str:
        if char.lower() == letter.lower(): # to convert into lowercase so 'J' 'j' are treated same
            count += 1
    print(count)

# countString()

""" <----- Program - Growing text -----> """
def growingString():
    str = input("Enter a word and see it grow > ")
    iterate = 0

    while iterate < len(str):
        print(str[:iterate+1])  # 0 to iterate + 1. iterate -> 1st loop run = 1, 2nd => 2 and so on.
        iterate += 1

# growingString()

""" <----- Program - Print every second word  -----> """
def printEverySecondWord():
    str = input("Enter a word to get printed with skip every 1st letter > ")
    iterate = 0

    while iterate < len(str):
        if iterate % 2 == 1: # if iterate is odd -> 1,3..., 1 refers to 2nd letter in the string
            print(str[iterate], end="")
        iterate += 1

# printEverySecondWord()


""" <----- Program - Print a word in 3 groups letter having each  -----> """
def printThreeWords():
    str = input("Enter a word having more than 3 letters to get Printed a word in 3 groups letter > ")
    iterate = 0

    length = len(str)

    while iterate < length:  
        substring = str[iterate:iterate+3] 
        if len(substring) == 3:
            print(substring)
        iterate += 1

# printThreeWords()


""" <----- Program 4 -----> """
""" Ask for input, validate the given string. It must begin with http:// and end with .com. Tell the user if the string is valid or not  """
def validateString():
    str = input("Enter a string that begins with http:// and end with .com > ")
    if str.startswith("http://") and str.endswith(".com") :
        print("String is valid")
    else: 
        print("String is not valid")


# validateString()

""" Progarm - Time Delay """
""" Ask for a number of seconds. Print “The other side” after that many seconds """
import time
def waitForNumberOfSeconds():
    seconds = int(input("Please enter time in seconds > "))
    time.sleep(seconds)
    print("The other side")

# waitForNumberOfSeconds()
""" NOTE: THE TIME PROGRAM USES time.sleep though time.time is given as I couldn't find solution with it """    
    


""" <----- Program 5 -----> """
""" Ask for numbers, add them together. Stop when the given number is negative. Print the sum. """

def addNumbers():
    number = 0
    sum = 0
    while number >= 0:
        sum += number
        number = float(input("Enter a number > "))
    print(sum)

# addNumbers()

""" <----- Program 6 -----> """
""" Use a while loop to calculate sigma equation  """

def calculateExpression(n):
    count = 0
    sum = 0
    while count <= n:
        sum += 2 * (count ** 2)
        count += 1
    return sum


# number = int(input("Enter a value for n > "))
# print(calculateExpression(number))



""" <----- Program 7 -----> """
""" Ask the user to enter a potential password. If it does not contain at least eight characters and at least one numerical digit, reject the password and ask again. """



def checkPotentialPassword():

    inputPassed = False

    def ifNumberPresent(str):
        for char in str:
            if char.isdigit():
                return True
        return False

    while not inputPassed:
        password = input("Enter a password of at least 8 characters and containing 1 digit > ")
        if len(password) >= 8 and ifNumberPresent(password):
            print("Your password is passed.")
            inputPassed = True
        
# checkPotentialPassword()

""" Program 8 """
""" Ask the user to enter a positive integer. If the user does not enter a positive integer, ask again. When the user enters a positive integer, n, calculate n!."""

def calculateFactorial():
    inputPassed = False
    factorial = 1

    while not inputPassed:
        number = int(input("Enter a number > "))
        if number >= 0:
            inputPassed = True
    
    # calculating number!
    for i in range(number, 0, -1):
        factorial *= i

    print(factorial)


# calculateFactorial()


""" <----- Program 9 -----> """
""" Ask the user to enter three numbers, a, b, and c. Print out a statement indicating which is smallest and which is largest. """

def showLargestAndSmallestNumber():
    num1 = float(input('Please enter first number > '))
    num2 = float(input('Please enter second number > '))
    num3 = float(input('Please enter third number > '))

    def ifSmaller(a,b):
        return a < b

    if ifSmaller(num1, num2) and ifSmaller(num1, num3):
        print("The smallest number is", num1)
    if ifSmaller(num2, num1) and ifSmaller(num2, num3):
        print("The smallest number is", num2)
    if ifSmaller(num3, num1) and ifSmaller(num3, num2):
        print("The smallest number is", num3)

    if not ifSmaller(num1, num2) and not ifSmaller(num1, num3):
        print("The largest number is", num1)
    if not ifSmaller(num2, num1) and not ifSmaller(num2, num3):
        print("The largest number is", num2)
    if not ifSmaller(num3, num1) and not ifSmaller(num3, num2):
        print("The largest number is", num3)
        

# showLargestAndSmallestNumber()


""" <----- Program 10 -----> """
""" 
    Write a program that displays a multiplication table similar to the following. Include up to 9x9.
         1    2    3
    1    1    2    3
    2    2    4    6
    3    3    6    9
""" 

def printRandomTable():
    for i in range(4):
        for j in range(4):
            if i == 0 and j == 0:
                print("", end="  ")
            else:
                if i * j == 0:
                    print(i+j, end=" ")
                else:
                    print(i*j, end=" ")
        print()


# printRandomTable()

def printRandomTableUsingWhile():

    row = 1000
    column = 1000

    i = 0
    while i < row:
        j = 0
        while j < column:

            spacesLength = len(str(row * column))

            if i == 0 and j == 0:
                print(" "*spacesLength, end="  ")
            else:
                if i * j == 0:
                    print("{:{spaces}d}".format(i+j, spaces=spacesLength), end="  ")
                else:
                    print("{:{spaces}d}".format(i*j, spaces=spacesLength), end="  ")
            j += 1
        i += 1
        print()

# printRandomTableUsingWhile()