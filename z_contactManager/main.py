import files
import uuid

def addContact(personName, contactNumber, email):
    id = uuid.uuid1()
    isAdded = files.addDataToFile(personName, contactNumber, email, id)
    if isAdded:
        print("Contact is added!")
    else:
        print("Contact is already stored")


addContact("Jashanjot", "981242z", email)