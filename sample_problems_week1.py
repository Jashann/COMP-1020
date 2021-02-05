""" <----- Program 1 -----> """
def convertCelsusToFrenheit(celsus):
    return celsus * 1.8 + 32

# celsus = int(input("Enter temperature in celsus! \n"))
# print("Temperature in frahrenheit is :", convertCelsusToFrenheit(celsus))


""" <----- Program 2 -----> """
def calculateParabola(x):
    a, b, c = 1, 2, 3
    print("{:.3f}".format(a*x**2+b*x+c))

# calculateParabola(12.4128912)


""" <----- Program 3 -----> """
def timeElapsed():
    startTime = input("Enter the starting time like this  3:20 > ")
    endTime = input("Enter the ending time like this  22:20 > ")

    startTimeColon = startTime.find(":")
    endTimeColon = endTime.find(":")

    startTimeHoursInt = int(startTime[:startTimeColon])
    startTimeMinutesInt = int(startTime[startTimeColon+1:])

    endTimeHoursInt = int(endTime[:endTimeColon])
    endTimeMinutesInt = int(endTime[endTimeColon+1:])

    totalHours = abs(endTimeHoursInt - startTimeHoursInt)
    totalMinutes = abs(endTimeMinutesInt - startTimeMinutesInt) + totalHours * 60

    print("The numbers of minutes elapsed ----> ", totalMinutes )


# timeElapsed()



""" <----- Program 4 -----> """
def calculateLaps():
    # measurements in meter
    marthonDistance = 42.195 * 1000 # Multiplying by 1000 To convert Kms into meters 
    circularRaceTrackDistance = 200
    laps = marthonDistance/circularRaceTrackDistance
    print("Number of laps", laps)

# calculateLaps()


""" <----- Program 5 -----> """
def calculateBoardsNeededForBuildingFence():
    # measurements in inches
    fenceToBeBuilt = 60 * 12 # Multiplying by 12 To convert foot into inches
    board = 6 
    gap = 0.5
    boardsNeeded = fenceToBeBuilt / (board + gap)
    print(boardsNeeded)

calculateBoardsNeededForBuildingFence()