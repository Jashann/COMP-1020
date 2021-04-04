import numpy as np
theSum = 0
a = np.array([[1,2,3],[4,5,6],[4,4,4],[10,11,12]])
for i in range(len(a)):
    for j in range(len(a[i])):
        if i == 2:
            theSum += a[i][j]
print(theSum)


# # # # x = {'a': 23, 'b': 18, 'c': 39, 'd': 24, 'e': 42, 'f':5}

# # # # def findEvenCounts(x):
# # # #     theList = []
# # # #     for k in x:
# # # #         if x[k] % 2 == 0:
# # # #             theList.append(x[k])
# # # #     return theList


# # # # print(findEvenCounts(x))


# # # studentGrades = {123: [10,10], 456: [10, 10], 789: [72, 84, 77, 81, 92]}

# # # def grades(mydict, stuID1, stuID2):
# # #     if stuID1 in mydict and stuID2 in mydict:
# # #         stu1Grades = mydict[stuID1]
# # #         stu2Grades = mydict[stuID2]

# # #         average1 = sum(stu1Grades)/len(stu1Grades)
# # #         average2 = sum(stu2Grades)/len(stu2Grades)

# # #         if average1 == average2:
# # #             return 0
# # #         if average1 > average2:
# # #             return stuID1
# # #         else:
# # #             return stuID2
# # #     else:
# # #         return -1

# # # print(grades(studentGrades, 123, 456))


# # import numpy as np

# # def getNCards(n):
# #     return np.random.randint(1,53,n)

# # def checkCards(arr):
# #     cards = {}
# #     for num in arr:
# #         if num not in cards:
# #             cards[num] = 0
# #         cards[num] += 1

# #     freq = arr[0]
# #     for key in cards:
# #         repeatedTimes = cards[num]
# #         if repeatedTimes > cards[freq]:
# #             freq = key

# #     return freq
        

# # cardsDrawn = getNCards(10)
# # print(cardsDrawn)
# # print(checkCards(cardsDrawn))



# counts = np.array([3,0,34,2,21,43])

# def timeToSpray(counts):
#     trapCountMoreThan5 = 0
#     average = 0
#     total = 0

#     for count in counts:
#         if count > 5:
#             trapCountMoreThan5 += 1
#         total += count
    
#     average = total / len(counts)

#     if trapCountMoreThan5 > 5 and average > 10:
#         return True
#     return False


# import numpy as np
# counts = np.array([10,10,00,0,5,5])
# print(timeToSpray(counts))


# def timeToSpray(counts):
    
#     average = 0

#     trapCountMoreThan5 = counts[counts > 5]
#     total = np.sum(trapCountMoreThan5)
    
#     average = total / len(counts)

#     if len(trapCountMoreThan5) > 5 and average > 10:
#         return True
#     return False

# print(timeToSpray(counts))
