# import random

# def roll5Numbers():

#     howManyToChoose = 5

#     rolls = list(range(1,7))
#     result = random.choices(rolls, k=howManyToChoose)
#     return result

# def rollToWin():
#     won = False
#     count = 0
#     while not won:
#         count += 1

#         won = True 
#         result = roll5Numbers()

#         for i in range(len(result)):
#             if result[0] != result[i]:
#                 won = False
    
#     return count


# def doTrails(howManyTrails):
#     data = []
#     for _ in range(howManyTrails):
#         howManyCountBeforeWin = rollToWin()
#         data.append(howManyCountBeforeWin)

#     return data

# def calculateAverage(data):
#     avg = sum(data)/len(data)
#     print("Average rolls needed to get yachtsee", avg)


# # MAIN
# TRAILS = 1000

# random.seed(1500)

# data = doTrails(TRAILS)
# calculateAverage(data)

