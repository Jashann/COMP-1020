"""
author: Jashanjot Singh Gill
github: https://github.com/Jashann
portfolio: https://jashann.github.io/
email: jashangill3592@gmail.com
message: if you find a bug, please do let me know.
"""




"""
    PROGRAM 1

    OUTPUT:
    *      -> 00
    **     -> 10 11
    ***    -> 20 21

"""

def printTriangle():
    for i in range(3):
        for j in range(3):
            if j <= i:
                print("*", end="")
        print()

# printTriangle()


"""
    PROGRAM 2

    OUTPUT:
    ***      -> 00 01 02
    **       -> 10 11
    *        -> 20

"""

def printTriangleUpsideDown():
    columns = 3
    for i in range(3):
        for j in range(3):
            if j >= columns - 1:
                print("*", end="")
            else:
                print(" ", end="")
            
        columns -= 1
        print()

printTriangleUpsideDown()


"""
    PROGRAM 3

    OUTPUT:
    *    *    ->   00       |       05
    **  **    ->   10 11    |    14 15
    ******    ->   20 21 22 | 23 24 25

    LOGIC
    
    1. divide two parts and use inner for loop for each
    *  |  *  
    ** | **
    ***|***

    2. first part is same is triangle code
    3.    *  -> 00      01      02(P)
         **  -> 10      11(P)   12(P)
        ***  -> 20(P)   21(P)   22(P)


"""

def printM():
    columns = 3
    for i in range(3):

        for j in range(3):
            if j <= i:
                print("*", end="")
            else:
                print(" ", end="")

        for j in range(3):
            if j >= columns - 1:
                print("*", end="")
            else:
                print(" ", end="")

        print()
        columns -= 1

# printM()