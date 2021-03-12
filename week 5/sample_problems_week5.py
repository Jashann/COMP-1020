# from typing import Dict


# def programOne():
#     studentsFile = open("z_students.txt")

#     studentsDict = {}
#     total = 0

#     for student in studentsFile:
#         studentInfo = student.split(" ")
        
#         studentName = studentInfo[0]
#         studentMarks = studentInfo[1]
#         studentMarks = studentMarks.strip()

#         if studentName not in studentsDict:
#             studentsDict[studentName] = []

#         if studentMarks.isnumeric():
#             studentMarks = int(studentMarks)
#             studentsDict[studentName].append(studentMarks)

#     # Finding average
#     # Finding who got what overall grade 
#     gradesCategory = {}

#     for studentName in studentsDict:
#         grades = studentsDict[studentName]
#         countOfGrades = len(grades)
#         total = sum(grades)
#         if countOfGrades != 0:
#             average = total / countOfGrades
#         # print(f"{studentName}: {average:.2f} ")

#         certainGarde = int(average) # 99 or 100
#         if certainGarde not in gradesCategory:
#             gradesCategory[certainGarde] = []
        
#         gradesCategory[certainGarde].append(studentName)

#     gradesListOfTuples = []

#     # # Storing grades in listOfTyple for sorting
#     # for grade in gradesCategory:
#     #     gradeTuple = (grade, gradesCategory[grade])
#     #     gradesListOfTuples.append(gradeTuple)   
    
#     # # Printing sorted gardes
#     # gradesListOfTuples.sort()
#     # for gradeTuple in gradesListOfTuples:
#     #     print(gradeTuple[0], gradeTuple[1])
#     #     print()


#     # Showing sorted gardes without sorting
#     mostCommonGarde = -1
#     for i in range(0,101):
#         if i in gradesCategory:
#             print(i, gradesCategory[i], end="\n \n")

#             # Finding most common
#             studentsHavingGarde = len(gradesCategory[i])
#             if mostCommonGarde < studentsHavingGarde:
#                 mostCommonGarde = studentsHavingGarde

#     print(mostCommonGarde)


# # programOne()


# # Finding who got what gardes on each assignment
# # Grouping stundents by their names' first letter
# def programSecond():
#     fileName = "z_students.txt"
#     fHandle = open(fileName)

#     gradesCategory = {}
#     namesCategory = {}

#     mostCommonGarde = -1
#     for line in fHandle:
#         studentsInfo =  line.split()
#         studentName = studentsInfo[0]
#         studentScores = studentsInfo[1]

#         if studentScores.isnumeric():
#             studentScores = int(studentScores)

#         # Storing grades in the groups
#         if studentScores not in gradesCategory:
#             gradesCategory[studentScores] = set()

#         gradesCategory[studentScores].add(studentName)


#         # Storing names in the dictionary. A: {"Ana",}
#         firstLetter = studentName[0]

#         if firstLetter not in namesCategory:
#             namesCategory[firstLetter] = set()

#         namesCategory[firstLetter].add(studentName)

#     # print(100, gradesCategory[100])
#     print("A", " ------ ", namesCategory["A"])



#     # finding MostCommon Grade
#     for grade in gradesCategory:
#         studentsHavingGarde = len(gradesCategory[grade])
#         if mostCommonGarde < studentsHavingGarde:
#             mostCommonGarde = grade

#     # print(f"Most students had grade of {mostCommonGarde} in all assignments")


    

# programSecond()




# a = 10
# b = 20.0
# c = 2

# print(a/c)
# print(b/c)
# print(a%c)

# numList = [2,4,6]

# total = 0
# for num in numList:
#     total = total  + num ** 2

# total = -total

# print(total)

# str = "alice,bob:eve;alice:alice:bob"
# str2 = str.replace(",",";")
# print(str2.split(";"))


# for i in range(0, 3):
#     for j in range(1, 3):
#         print("{} ** {} = {}".format(i, j, i**j))


# letterset = set("abcdefghijklmnopqrstuvwxyz")
# myDict = {}

# for letter in letterset:
#     myDict[letter] = []

# file = open("z_words.txt")


# for line in file:
#     words = line.split()
#     for word in words:
#         firstLetter = word[0].lower()
#         if firstLetter in letterset:
#             myDict[firstLetter].append(word)

# print(myDict)

