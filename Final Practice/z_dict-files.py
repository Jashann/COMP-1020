# def readInFileAndCreateDict(fileName):
    
#     studentsDict = {}
#     fileHandler = open(fileName)

#     for line in fileHandler:
#         columns = line.split(":")
#         studentID = columns[0]
#         studentInfo = columns[1]
#         studentInfo_Parts = studentInfo.split(",")
#         studentName = studentInfo_Parts[0] + studentInfo_Parts[1]
#         print(studentName)


# fileName = "student_info.txt"
# readInFileAndCreateDict(fileName)

def getInput(studentsDict):
    inputIsValid = False

    while not inputIsValid:
        userInput = input("Enter student id > ")
        if userInput.isnumeric():
            parsedInput = int(userInput)
            if parsedInput in studentsDict:
                inputIsValid = True

    return userInput

def calculateStats(studentsDict, studentID):
    student = studentsDict[studentID]
    courses = student[2]
    count = len(courses)
    gradesNum = 0

    for tup in courses:
        grade = tup[1]
        if grade == "A":
            gradesNum += 4
        elif grade == "B":
            gradesNum += 3
        elif grade == "C":
            gradesNum += 2
        else:
            gradesNum += 0
        
    avg = gradesNum/count

    print("{} {}’s GPA is {:.2f}".format(student[0], student[1], avg))

# MAIN
studentsDict = data	= {
    100: ("Mickey",	"Mouse", [("COMP	1010",	'A'), ("COMP	1020",	'B'), ("CHEM	1300", 'C')]),		
	101: ("Minnie",	"Mouse", [("COMP	1012",	'A'), ("COMP	1020",	'A'), ("MATH	1500", 'A')]),		
	102: ("Donald",	"Duck",	 [("COMP	1010",	'B'), ("CHEM	1300",	'C'), ("MATH	1500", 'C')])}


# Input
# studentID = getInput(studentsDict)
studentID = 100
calculateStats(studentsDict, studentID)


