# fhandle = open("sample.txt")

# for line in fhandle:
#     print(line)

# print()


# fhandle2 = open("sample.txt")
    
# for line in fhandle2:
#     print(repr(line))


# fhandle = open("sample_users.txt")

# for line in fhandle: 
#     index = line.find("name:") # if line does not have name then it returns -1
#     if index != -1:
#         indexBeforeName = line.find(": ")
#         name = line[indexBeforeName+1:]
#         print("I am",line)


file = open("sample.txt")

lineNumber = 0
for line in file:
    letterInEachLine = 0
    for letter in line:
        if letter.isalnum():
            letterInEachLine += 1
    print("Line {} has these many characters {}".format(lineNumber, letterInEachLine))
    lineNumber += 1
