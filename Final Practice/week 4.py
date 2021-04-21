def printM(n):
    for i in range(n):

        for j in range(n):
            if j <= i:
                print("*", end="")
            else: 
                print(end=" ")

        for j in range(n):
            if i+j >= n-1:
                print("*", end="")
            else: 
                print(end=" ")

        print()

# printM(3)


dict1 = {
    "name": "Jashan",
    "age": 19 
}

for tup in dict1.items():
    print(tup)