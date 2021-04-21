
"""
    Write a program that asks the user to enter a weight in pounds and ounces, where the input is entered with a comma between the two numbers, as in “14,9”. Convert to a weight in kilograms, and print it to 3 decimal places. (There are 16 ounces in 1 pound, and 1 kilogram = 2.20462 pounds)
"""

def convertToKg(pounds, ounces):
    return pounds / 2.20462 + (ounces  / 16 / 2.20462 ) 


# # main
# userInput = "14,9"

# inputIsValid = False

# while not inputIsValid:
#     userInput = input("Enter pounds and ounces separated by ',' > ")    
#     colonIndex = userInput.find(":")
#     if colonIndex >=0:
#         pounds = userInput[0 : colonIndex]
#         ounces = userInput[colonIndex+1 : ]
#         if pounds.isnumeric() and ounces.isnumeric():
#             pounds = int(pounds)
#             ounces = int(ounces)
#             inputIsValid = True

# kgs = convertToKg(pounds, ounces)
# print(f"{pounds} pounds and {ounces} is: {kgs:.3f} ")



"""
     Use a while loop to calculate Summation of 0 to n of equation { 2n^(2) }
"""
def calculateEquation(n):
    count = 0
    result = 0
    while count <= n:
        result += 2*count**2
        count += 1 
    return result

# print(calculateEquation(2))


"""
    Ask the user to enter a potential password. If it does not contain at least eight characters and at least one numerical digit, reject the password and ask again.
"""
def getValidPassword():
    numeric = 0

    inputIsValid = False

    while not inputIsValid:
        password = input("Enter a password > ")
        if len(password) >= 8:
            for char in password:
                if char.isnumeric():
                    numeric += 1
            if numeric >= 1:
                inputIsValid = True

    print("Your password is passed!") 
    

# getValidPassword()


"""
    Write a program that displays a multiplication table similar to the following. Include up to 9x9.
         1    2    3
    1    1    2    3
    2    2    4    6
    3    3    6    9
"""

def printTable(n):
    for i in range(n):
        for j in range(n):
            if i * j != 0:
                print("{:5d}".format(i*j), end="")
            else:
                print("{:5d}".format(i+j), end="")
        print()

# printTable(9)


# Growing text
def printGrowing(word):
    i = 0

    # while i < len(word):
    #     print(word[0 : i+1])
    #     i += 1

    maximum = 1
    while i < len(word):
        j = 0

        while j < maximum:
            char = word[j]
            print(char, end="")
            j += 1

        print()

        maximum += 1
        i += 1

# printGrowing("Jashan")



def textWindow(word):
    window = 4
    wordLen = len(word)
    i = 0

    while i < wordLen - window + 1:
        print(word[i: i+window])
        i += 1


textWindow("Jashanjot")