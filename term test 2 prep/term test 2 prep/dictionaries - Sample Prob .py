def groupByGrades():

    def getAverageDictionary(myDict):
        averagesDict = {}
        for key in myDict:
            studentGradesList =  myDict[key]
            average = sum(studentGradesList) / len(studentGradesList)

            averagesDict[key] = round(average, 2)
        
        return averagesDict

    
    def whoGotWhatGrades(studentsDict, whatGrade):
        gradesDict = {}
        
        for studentName in studentsDict:
            studentGrade = int(studentsDict[studentName])
            if studentGrade not in gradesDict:
                gradesDict[studentGrade] = []
            gradesDict[studentGrade].append(studentName)

        if whatGrade in gradesDict:
            print(f'These students: {gradesDict[whatGrade]} got {whatGrade}' )
        else:
            print("No student got",whatGrade)  



    fileName = "z_students.txt"

    fileHandle = open(fileName)
    studentsDict = {}

    for line in fileHandle:

        words = line.split()
        studentName = words[0]
        studentGrade = int(words[1])

        if studentName not in studentsDict:
            studentsDict[studentName] = []
        studentsDict[studentName].append(studentGrade)

    # getAverageDictionary(studentsDict)
    averagesDict = getAverageDictionary(studentsDict)
    whoGotWhatGrades(averagesDict, 100)

groupByGrades()