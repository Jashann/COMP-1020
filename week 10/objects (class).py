class Set():
    def __init__(self): # Constructor 
        self.mySet = []
        
    def add(self, item):
        if item not in self.mySet:
                self.mySet.append(str(item))

    def __str__(self):

        string = ""

        string +="Set: \n"
        string +="{ \n \t"
        for item in self.mySet:
            string += item + "\t"
        
        string += "\n}"

        return string

    def difference(self, otherSet):
        newSet = []
        for item in self.mySet:
            if item not in otherSet.mySet:
                newSet.append(item)
        return newSet
    
    def intersection(self, otherSet):
        newSet = []
        for item in self.mySet:
            if item in otherSet.mySet:
                newSet.append(item)
        return newSet



mySet1 = Set()
mySet1.add(1)
mySet1.add(2)
mySet1.add(3)
mySet1.add(4)
print(mySet1)

mySet2 = Set()
mySet2.add(1)
mySet2.add(2)
mySet2.add(10)
mySet2.add(20)

print(mySet1.difference(mySet2))
print(mySet1.intersection(mySet2))