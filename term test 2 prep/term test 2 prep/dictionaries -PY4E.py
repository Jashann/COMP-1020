"""
    Resource = https://www.py4e.com/html3/09-dictionaries
"""

"""
    Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
    Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.
"""

def ex1():
    fileName = "words.txt"
    fileHandle = open(fileName)

    wordsDict = {}
    for line in fileHandle:
        words = line.split()

        for word in words:
            if word not in wordsDict:
                wordsDict[word] = 0
            wordsDict[word] += 1

    print(wordsDict)

# ex1()

"""
    Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

    Sample Line:

    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
    Sample Execution:

    python dow.py
    Enter a file name: mbox-short.txt
    {'Fri': 20, 'Thu': 6, 'Sat': 1}

"""

def ex2():
    fileName = "z_mbox-short.txt"
    fileHandle = open(fileName)

    daysDict = {}
    for line in fileHandle:
        if "From" == line[0:4]:
            words = line.split()
            if len(words) > 2:
                day = words[2]
                if day not in daysDict:
                    daysDict[day] = 0
                daysDict[day] += 1
    print(daysDict)
        
# ex2()


"""
    Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.
"""


def ex3():

    def findWhoHasMostAndMinEmails(myDict):
        # (key, value)
        maxKey = None
        minKey = None

        for key in myDict:
            count = myDict[key]
            if not minKey and not maxKey: # if they are empty or None
                maxKey = key
                minKey = key
            else:
                if count > myDict[maxKey]:
                    maxKey = key
                else:
                    minKey = key
        print(f'{maxKey} has the most messages: {myDict[maxKey]}')
        print(f'{minKey} has the least messages: {myDict[minKey]}')


    fileName = "z_mbox-short.txt"
    fileHandle = open(fileName)

    emailsDict = {}
    for line in fileHandle:
        if "From" == line[0:4]:
            words = line.split()
            if len(words) > 1:
                email = words[1]
                if email not in emailsDict:
                    emailsDict[email] = 0
                emailsDict[email] += 1
    # print(emailsDict)

    findWhoHasMostAndMinEmails(emailsDict)


        
ex3()