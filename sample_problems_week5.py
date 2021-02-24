studentsFile = open("z_students.txt")

studentsDict = {}
total = 0

for student in studentsFile:
    studentInfo = student.split(" ")
    
    studentName = studentInfo[0]
    studentMarks = studentInfo[1]
    studentMarks = studentMarks.strip()

    if studentName not in studentsDict:
        studentsDict[studentName] = 0

    if studentMarks.isnumeric():
        studentsDict[studentName] = int(studentMarks)

print(studentsDict)