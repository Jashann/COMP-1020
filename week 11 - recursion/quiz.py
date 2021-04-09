class House:
    def __init__(self, bedrooms, bathrooms, size):
       self.bedrooms = bedrooms
       self.bathrooms = bathrooms
       self.size = size

    def calculateHousePrice(self, n):
        housePrice = 2*n*self.bedrooms + 1.5*n*self.bathrooms + self.size
        return housePrice


# MAIN
house = House(4,2,1600)

print(house.calculateHousePrice(2))