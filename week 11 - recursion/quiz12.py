def function(dictionary): # c
    theSum = 0 # c
    for k in dictionary:
        if len(dictionary[k]) > 0: # c
                theSum += dictionary[k][0] # c
    return theSum

# line 1 dictionary is to be passed as a param
eter
# function(dictionary)
# line 2 theSum is to be defined to add to it
# theSum = 0
# line 4 we need to fetch value of list so we use dictionary[k]
# dictionary[k]
# line 5 we need to get dictionary value using key then add index 0 element
# dictionary[k][0]

dictionary = {"a": [1,2] , "c": [1,2], "d": []}
            
print(function(dictionary))
