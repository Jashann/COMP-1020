""" --------------- DICTIONARIES ---------------- """

# file = open("C:/Users/University/Documents/University/COMP 1012/mycode/z_words.txt")
"""
Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt

Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.
"""
def programFirst():
    file = open("z_words.txt")

    wordsDict = {}
    for line in file:
        for word in line.split():
            wordsDict[word] = 1

    print(wordsDict)

# programFirst()

"""
Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

Sample Line:

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Sample Execution:

python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
"""

def programSecond():
    file = open("z_mbox-short.txt")
    
    weekDaysFrequency = {}
    for line in file:
        if "From " in line:
            day = line.split()[2]
            if day not in weekDaysFrequency:
                weekDaysFrequency[day] = 1
            else:
                weekDaysFrequency[day] += 1
    print(weekDaysFrequency)

# programSecond()


"""
Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.
"""
def programThird():

    # find maximum
    def findMaximumAndReturn(dictionary):
        maxDict = { "keyID": None, "value": -999999999999 }
        minDict = { "keyID": None, "value":  999999999999}
        for key, value in dictionary.items():
            if maxDict["value"] < value:
                maxDict["keyID"] = key
                maxDict["value"] = value
            if minDict["value"] > value:
                minDict["keyID"] = key
                minDict["value"] = value

        print(maxDict)
        print(minDict)
            

    file = open("z_mbox-short.txt")
    emailsFrequency = {}
    for line in file:
        if "From:" in line:
            index = line.find(" ")
            email = line[index+1:].strip()
            if email not in emailsFrequency:
                emailsFrequency[email] = 1
            else:
                emailsFrequency[email] += 1
    print(emailsFrequency)
    findMaximumAndReturn(emailsFrequency)

# programThird()





"""
    Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

    python schoolcount.py
    Enter a file name: mbox-short.txt
    {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
    'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

"""

def programFourth():

    domainAddressesDict = {}

    fileName = "z_mbox-short.txt"
    # fileName = input("Enter a file name: ")

    fileHandler = open(fileName)

    for line in fileHandler:
        if "From:" in line:
            # finding index of @
            index = line.index("@")
            domainAddress = line[index:].strip()

            if domainAddress in domainAddressesDict:
                domainAddressesDict[domainAddress] += 1
            else:
                domainAddressesDict[domainAddress] = 1

    print(domainAddressesDict)

# programFourth()






""" ----------------- PRACTICE ------------------- """
# counts = {"name": "Jashan", "age": 19, "gender": "Male"}
# lst = list()
# for tup in counts.items():
#     (key, value) = tup
#     print(key, value)


""" ------------------  TUPLE ----------------- """

def programPullAddresses():

    personsCount = {}
    file = open("z_mbox-short.txt")

    for line in file:
        # Could be easily done with in operator, trying something differnent
        if line.split(" ")[0]  == "From":

            index = line.index(" ")
            secondIndex = line.index(" ",index+1)
            email = line[index:secondIndex]

            if email not in personsCount:
                personsCount[email] = 1
            else:
                 personsCount[email] += 1
    print(personsCount)            


programPullAddresses()