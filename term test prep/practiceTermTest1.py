"""
    Create a program to calculate points on a parabola. Hard-code a, b, c in your y = ax2 + bx + c. Set a value for x, calculate a value for y, and print the coordinates to three decimal places.
"""

def calculateQuadratic(a,b,c):
    x = 2
    y = a * x**2 + b*c + c
    return y

# print(calculateQuadratic(1,2,3))


""" Given two times (e.g. 2:40 and 7:10), write a program to calculate the number of minutes elapsed. """
def timeElapsed(time1, time2):
    indexColon1 = time1.index(":")
    timehours1 = int(time1[:indexColon1])
    timeMinutes1 = int(time1[indexColon1+1:])

    indexColon2 = time2.index(":")
    timehours2 = int(time2[:indexColon2])
    timeMinutes2 = int(time2[indexColon2+1:])

    hours = abs(timehours1 - timehours2)
    minutes = timeMinutes2 - timeMinutes1     
    total = hours * 60 + minutes

    print(total)


# timeElapsed("2:10", "3:40")


""" Write a program that asks the user for a speed in km/h and a distance in km. Calculate (in hours, minutes and seconds) how long it would take to travel the distance, and print a message similar to “It would take 3 hours, 42 minutes, and 16 seconds to travel 37.03 km at a speed of 10.00 km/h.” """
def calculateTimeToReach(distance, speed):
    originalTime = distance/speed

    hours = originalTime//1
    originalTime = originalTime -hours

    minutes = (originalTime * 60) // 1
    originalTime = originalTime * 60 - minutes
    seconds = originalTime * 60

    print(f"It would take {hours:.0f} hours, {minutes:.0f} minutes, and {seconds:.0f} seconds to travel 37.03 km at a speed of 10.00 km/h")

# calculateTimeToReach(37.03, 10)




def getPassword():
    passwordIsValid = False
    
    while not passwordIsValid:
        password = input("Please enter a password with 8 characters including at least one digit -> ")
        num = 0
        if len(password) >= 8:
            for char in password:
                if char.isnumeric():
                    num =+ 1
            if num > 0:
                passwordIsValid = True

        if not passwordIsValid:
            print("Invalid Password")
# getPassword()

"""
    Write a program that displays a multiplication table similar to the following. Include up to 9x9.
         1    2    3
    1    1    2    3
    2    2    4    6
    3    3    6    9
"""

def printMultiplicationTable(n):
    for i in range(n):
        for j in range(n):

            x = i * j
            if x == 0:
                x = i + j

            spaces = len(str(n*n))
            lenOfNum = len(str(x))

            if lenOfNum < spaces:
                lessLength = spaces - lenOfNum
                spaces = spaces + lessLength

            if i == 0 and j == 0:
                print(" "*(n*n), end="")
            else:
                print(x, " "*spaces ,end="")
        
        print()


# printMultiplicationTable(9)

"""
    hello ->

    Output:
    hel
    ell
    llo
"""
def printGroupsOfThree(word):
    length = len(word)
    currentWord = 0

    while currentWord + 3 <= length:
        print(word[currentWord : currentWord + 3])
        currentWord += 1

printGroupsOfThree("hello")


def sumUpAndAverageGrades():
    studentsDict = {}
    fileName = "students.txt"

    fileHandler = open(fileName)

    # storing in dict
    for line in fileHandler:
        gradeInfo = line.split()

        studentName = gradeInfo[0]
        studentGrade = int(gradeInfo[1])

        if studentName not in studentsDict:
            studentsDict[studentName] = []
        studentsDict[studentName].append(studentGrade)

    #  summing up and average
    for studentName in studentsDict:
        gardes = studentsDict[studentName]
        total = sum(gardes)
        average = total / len(gardes)
        print(studentName)
        print(f"\t Total: {total}, Average: {average:.1f}", end="\n \n")
        
sumUpAndAverageGrades()

# x = 132.5991237423
# print("{:.2f}".format(x))