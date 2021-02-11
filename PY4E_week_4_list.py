"""
    Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
"""

def chop(listOfItems):
    listOfItems.pop(0)
    length = len(listOfItems) - 1
    listOfItems.pop(length)
    return None

def middle(listOfItems):
    length = len(listOfItems)  - 1
    return listOfItems[1:length]

listOfNumbers = [1,2,3,4]
# chop(listOfNumbers)
# print(listOfNumbers)
print(middle(listOfNumbers))



