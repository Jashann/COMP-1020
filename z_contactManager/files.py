import csv
FILES = "data.csv"

def addDataToFile(name, contactNo, email, id):
    filehandler = open(FILES, mode="a")

    response = checkIfNameNotInFile(name, contactNo)
    if response:
        filehandler.write(f'{name},{contactNo},{id} \n ')

    return response

def checkIfNameNotInFile(name, contactNo):
    alreadyStored = False

    return not alreadyStored


def readAFile(callback):
    with open(FILES) as csvFile:
        csvReader = csv.reader(csvFile, delimiter='\t')
        lineCount = 0

        for row in csvReader:
            if lineCount == 0:
                print(row)
            else:
                # print(row)
                callback(row)
            lineCount += 1