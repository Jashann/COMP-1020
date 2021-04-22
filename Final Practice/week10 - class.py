class Set:
    def __init__(self, iterable=None):
        self.data = []

        if iterable:
            for item in iterable:
                if item not in self.data:
                    self.data.append(item)
    
    def __str__(self) -> str:
        out = "Set: {}".format(self.data)
        return out
    
    def addItem(self, item):
        if item not in self.data:
            self.data.append(item)
    
    def intersection(self, otherSet):
        newSet = Set()

        for itemThisSet in self.data:
            if itemThisSet in otherSet.data:
                newSet.addItem(itemThisSet)
            
        return newSet
    
    def differenceSet(self, otherSet):
        newSet = Set()

        for itemThisSet in self.data:
            if itemThisSet not in otherSet.data:
                newSet.addItem(itemThisSet)
        
        for itemThisSet in otherSet.data:
            if itemThisSet not in self.data:
                newSet.addItem(itemThisSet)
            
        return newSet
        
set1 = Set()
set1.addItem(1)
set1.addItem(1)
set1.addItem(2)
set1.addItem(4)

set2 = Set([1,2,3,4,4])

print(set1)
print(set2)

interSet = set1.intersection(set2)
print(interSet)

diffSet = set1.differenceSet(set2)
print(diffSet)