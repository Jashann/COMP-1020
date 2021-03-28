import files
import uuid

runAgain = True

while runAgain:
    def addContact(personName, contactNumber, email):
        id = uuid.uuid1()
        isAdded = files.addDataToFile(personName, contactNumber, email, id)
        if isAdded:
            print("Contact info is added!")
        else:
            print("Contact info is already stored")

    addContact("Jashanjot", "981242z", "jashangill3592@gmail.com")

