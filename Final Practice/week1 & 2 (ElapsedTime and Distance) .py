"""
    Given two times (e.g. 2:40 and 7:10), write a program to calculate the number of minutes elapsed.
"""

def elapsedMinutes(startTime, endTime):
    firstColonIndex = startTime.index(":")
    secondColonIndex = endTime.index(":")

    if firstColonIndex == -1 or secondColonIndex == -1:
        print("Invalid Input")
    else:
        startHour = startTime[0: firstColonIndex]
        startMinutes = startTime[firstColonIndex+1 : ]

        endHour = endTime[0: secondColonIndex]
        endMinutes = endTime[secondColonIndex+1 : ]

        if startHour.isnumeric() and endHour.isnumeric() and startMinutes.isnumeric() and endMinutes.isnumeric():

            startHour = int(startHour)
            endHour = int(endHour)
            startMinutes = int(startMinutes)
            endMinutes = int(endMinutes)

            if startHour <= endHour:
                hours = endHour - startHour
                minutes = endMinutes - startMinutes

                totalMinutes = hours * 60 + minutes
                
                print(f"The given time: {startTime} --> {endTime} ")
                print("The elapsed number of minutes: {:.0f} ".format(totalMinutes))
            else:
                print("Start time is greater than end time.")
        else:
            print("The time given is not numeric")

# Main
# elapsedMinutes("8:50", "9:10")




"""
    Write a program that asks the user for a speed in km/h and a distance in km. Calculate (in hours, minutes and seconds) how long it would take to travel the distance, and print a message similar to “It would take 3 hours, 42 minutes, and 16 seconds to travel 37.03 km at a speed of 10.00 km/h.”
"""

def calculateTimeItTakes(distance, speed):
    time = distance/speed
    totalSeconds = int(time * 60 * 60)

    hours = int(totalSeconds // 60 // 60)
    totalSeconds -= hours * 60 * 60

    minutes = int(totalSeconds // 60)
    totalSeconds -= minutes * 60

    seconds = int(totalSeconds)

    print("It would take {h} hours, {m} minutes, and {s} seconds to travel {d:.2f} km at a speed of {speed:.2f} km/h".format(h=hours, m=minutes, s=seconds, d=distance, speed=speed))

# calculateTimeItTakes(37.03, 10)
