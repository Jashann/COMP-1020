fHandle = open("marks.csv")

assignmentScores = []
testScores = []

for line in fHandle:
    if line[0] != "i":
        indexFirstComma = line.index(",") + 1 
        # indexFirstComma = index of assign1
        indexSecondComma = line.index(",",indexFirstComma)
        # indexFirstComma = index of test

        assignmentScore = int(line[indexFirstComma:indexSecondComma])
        assignmentScores.append(assignmentScore)

        testScore = int(line[indexSecondComma+1:].strip())
        testScores.append(testScore)

# code for finding average, minimum and maximum

total = 0
min = 99999
max = -99999
for score in assignmentScores:
    total += score
    if min > score:
        min = score
    if max < score:
        max = score

average =  total/len(assignmentScores)

print("Average of assignment scores:", average)
print("Minimum value of assignment scores:", min)
print("Maximum value of assignment scores:", max)