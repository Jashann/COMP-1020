# import sys

# def calculateCostOfTransportingSoil():

#     volumeOfSoil = 3000
#     volumeOfTruckToTransport = 500

#     truckLoads = int(volumeOfSoil/volumeOfTruckToTransport)

#     totalCost = None

#     perCubicMetreSoilCost = None
#     perLoadCostOfTransport = None

#     if volumeOfSoil < 0 or volumeOfTruckToTransport < 0 :
#         print("Please enter valid input")
#         sys.exit()

#     if volumeOfSoil > 50:
#         perCubicMetreSoilCost = 10
#     elif volumeOfSoil >= 20 and volumeOfSoil <= 50:
#         perCubicMetreSoilCost = 20
#     else:
#         perCubicMetreSoilCost = 30


#     if truckLoads < 10:
#         perLoadCostOfTransport = 100
#     else:
#         perLoadCostOfTransport = 100

#     totalCost = perCubicMetreSoilCost * volumeOfSoil + perLoadCostOfTransport * volumeOfTruckToTransport

#     print("{} truck loads will be needed to transport {} m^3 soil. The cost incurring will be ${}".format(truckLoads, volumeOfSoil, totalCost))

# calculateCostOfTransportingSoil()



# def labSecond():
#     numberOfItems = input("Enter a numberOfItems of items > ")
#     while not (numberOfItems.isnumeric()):
#         numberOfItems = input("Enter a numberOfItems of items > ")

#     numberOfItems = int(numberOfItems)

#     cents = input("Enter a cost in cents > ")
#     while not cents.isnumeric():
#         cents = input("Enter a cost in cents > ")

#     dollars = float(cents) / 100
    # totalCost = None

    # if numberOfItems < 10:
    #     totalCost = numberOfItems * dollars
    # elif numberOfItems >= 10 and numberOfItems <= 19:
    #     totalCost = numberOfItems * dollars * 0.9
    # else:
    #     totalCost = numberOfItems * dollars * 0.8

    # print("The total cost of buying {} items is {:.2f}".format(numberOfItems,totalCost))

# labSecond()


numberOfPizzas = int(input("Enter number of pizzas you wanna order > "))

typeOfOrder = input("You want: delivery or pickup > " )

cost = None

if typeOfOrder == "delivery":
    if numberOfPizzas >= 10:
        cost = 5 * numberOfPizzas 
    elif numberOfPizzas >= 5:
        cost = 8 * numberOfPizzas
    else: 
        cost = 10 * numberOfPizzas
    cost += 5
else:
    if numberOfPizzas >= 5:
        cost = 6 * numberOfPizzas 
    else: 
        cost = 11 * numberOfPizzas

print("The cost of the order is ${}".format(cost))