import random

def monthAverage(dictionary, integer):
    
    total = 0
    count = 0

    for key in dictionary:
        nums = dictionary[key] 
        total += sum(nums)
        count += len(nums) 

    avg = total/count
    dictionary[integer] = avg
    
    return dictionary[integer]


randomNum = random.randint(0, 11)


averageTemps = {
    "list1": [10,10,20],
    "list2": [10,10,20]
}
returned = monthAverage(averageTemps, randomNum)
print("The average of that list is {:.2f} ".format(returned))
