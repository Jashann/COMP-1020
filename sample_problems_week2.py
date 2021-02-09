"""
author: Jashanjot Singh Gill
github: https://github.com/Jashann
portfolio: https://jashann.github.io/
email: jashangill3592@gmail.com
message: if you find a bug please do let me know.
"""

import math

""" <----- Program 1 -----> """
def countName(fullname):
    return fullname.count(" ")+1

# print( "Count of names" countName( input("Please enter your fullname ---> ") ) )


""" <----- Program 2 -----> """
def extractThirdWordFromSentence():
    sentence = input("Enter a sentence -> ")
    listOfWords = sentence.split()
    print(listOfWords[2])

# extractThirdWordFromSentence()



""" <----- Program 3 -----> """
def divideNumbers():
    a = float(input("Enter first number -> "))
    b = float(input("Enter second number -> "))
    result = a/b
    print("The result is {:.4f} ".format(result))

# divideNumbers()


""" <----- Program 4 -----> """
def findLengthAndAngle():
    a = input("Enter first coordinates in form (x,y) - (1,3) -> ")
    b = input("Enter second coordinates in form (x,y) - (5,1) -> ")

    [x1, y1] = map(int, a.split(","))
    [x2, y2] = map(int, b.split(","))

    distance = math.sqrt(  (x2-x1)**2 + (y2-y1)**2  )
    print("The length between two coordinates is", distance)

    angle = math.atan2((x2 - x1), (y2 - y1))
    print("The angle between two coordinates is", angle)


# findLengthAndAngle()


""" <----- Program 5 -----> """
def covertWeightIntoKilos():
    a = input("Enter weight in pounds and ounces like 120,20 -> ")
    comma = a.find(",")
    pounds = float(a[:comma])
    ounces = float(a[comma+1:])

    kilos = pounds/2.20462 +  ((ounces/16)/2.20462)

    print("Weight in kilograms {weight:.3f}".format(weight=kilos))


# covertWeightIntoKilos()


""" <----- Program 6 -----> """
def calculateTime():
    distance = float(input("Enter distance in Kilometers -> "))
    speed = float(input("Enter speed in km/h -> "))

    time = distance/speed

    totalMinutes = time * 60
    hours = totalMinutes//60 

    totalMinutes -= hours * 60 # removing minutes stored in hours

    minutes = int(totalMinutes)

    totalMinutes -= minutes
    
    seconds = totalMinutes * 60

    print("It would take {:.0f} hours, {:.0f} minutes, and {:.0f} seconds to travel {distance} km at a speed of {speed} km/h.".format(hours, minutes, seconds, distance = distance, speed=speed))


calculateTime()



# def calculateTimeDifference(startTimeHour,startTimeMinutes, endTimeHours, endTimeMinutes):
#     addedMinutes = startTimeMinutes + endTimeMinutes

def calculateTriangleArea(base, height):
    print("Area of triangle:",base*height/2)

# calculateTriangleArea(12,2) 



base = int(input("Enter base > "))
height = int(input("Enter height > "))

print((base*height)/2)

