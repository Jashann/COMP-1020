""" <----- Program 1 - PY4E -----> """

def calculateMin(listOfNumbers):
    smallest = listOfNumbers[0]
    for number in listOfNumbers:
        if smallest > number: # True if a number is smaller finds min
            smallest = number
    return smallest

def calculateMax(listOfNumbers):
    largest = listOfNumbers[0]

    for number in listOfNumbers:
        if largest < number: # True if a number is smaller finds min
            largest = number
    return largest


def findSumCountAvg_OR_MinAndMax(filter):
    done = None
    total = 0
    count = 0
    listOfNumbers = []

    print("The program will keep asking for inputs until \"done\" is typed ")

    while done is None:
        userInput = input("Enter a number > ")
        if userInput == "done":
            done =  True
            if filter == "avg":
                print("Total: {}, Count: {}, Average {}".format(total, count, total/count))
            if filter == "min":
                min = calculateMin(listOfNumbers)
                max = calculateMax(listOfNumbers)
                print("Min: {}, Max: {}".format(min, max))
        else:
            try:
                number = float(userInput)
                
                if filter == "avg":
                    total += number
                    count += 1
                if filter == "min":
                    listOfNumbers.append(number)
            except:
                print("Something went wrong, please enter a number!")


# userInput = input("What do you wanna find: \"avg\" , \"min\" > ")
# findSumCountAvg_OR_MinAndMax(userInput)





import sys

def getInputNumberFloat(inputMessage):
    try: 
        userInput = input(inputMessage) 
        if userInput == "done":
            sys.exit()
        return float(userInput)
    except:
        print("Error, please enter numeric input")
        sys.exit()

""" <----- Program 2 -----> """
""" Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours """

def computePay(hours, payRate):
    pay = hours * payRate
    if hours > 40:
        pay += (hours - 40) * payRate
    return pay



# hours = getInputNumberFloat("Enter numbers of hours worked > ")
# payRate = getInputNumberFloat("Enter pay rate per hour > ")
# print( computePay(hours,payRate) )


""" <----- Program 3 -----> """
""" Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table: """
def calculateGrade():
    while True:
        score = getInputNumberFloat("Enter score between 0.0 and 1.0 > ")
        if(score >= 0.0 and score <= 1.0):
            if score >= 0.9:
                print("A")
            elif score >= 0.8:
                print("B")
            elif score >= 0.7:
                print("C")
            elif score >= 0.6:
                print("D")
            elif score < 0.6:
                print("F")
        else:
            print("Out of range")
print("The program will keep asking for running until done is entered")
calculateGrade()

