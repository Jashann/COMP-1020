def groupByGrades(fileName):
    fileHandler = open(fileName)
    studentsDict = {}

    for line in fileHandler:
        columns = line.strip().split()
        studentName = columns[0]
        studentGrade = int(columns[1])

        if studentName not in studentsDict:
            studentsDict[studentName] = 0

        studentsDict[studentName] += studentGrade

    print(studentsDict)



fileName = "students.txt"
# groupByGrades(fileName)




def averageGrades(fileName):
    fileHandler = open(fileName)
    studentsDict = {}
    averageDict = {}

    # Grouping
    for line in fileHandler:
        columns = line.strip().split()
        studentName = columns[0]
        studentGrade = int(columns[1])

        if studentName not in studentsDict:
            studentsDict[studentName] = []

        studentsDict[studentName].append(studentGrade)
        
    # Getting average
    for tup in studentsDict.items():
        studentName = tup[0]
        studentGrades = tup[1]
        averageDict[studentName] = sum(studentGrades)//len(studentGrades)
    
    print(averageDict)


fileName = "students.txt"
# averageGrades(fileName)


def whoGotWhatGrade(fileName, GRADE):
    fileHandler = open(fileName)
    studentsDict = {}
    averageDict = {}
    gradesDict = {}

    for line in fileHandler:
        columns = line.strip().split()
        studentName = columns[0]
        studentGrade = int(columns[1])

        if studentName not in studentsDict:
            studentsDict[studentName] = []

        studentsDict[studentName].append(studentGrade)

    # Getting average and Grouping by Grade
    for tup in studentsDict.items():
        studentName = tup[0]
        studentGrades = tup[1]
        studentAverage = sum(studentGrades)//len(studentGrades)
        averageDict[studentName] = studentAverage
        
        if studentAverage not in gradesDict:
            gradesDict[studentAverage] = []
        gradesDict[studentAverage].append(studentName)
        

    print(gradesDict[GRADE])



fileName = "students.txt"
grade = 100
whoGotWhatGrade(fileName, grade)

