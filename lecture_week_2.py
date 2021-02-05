st = "Jashan Singh Gill"
space = st.find(" ")
sSpace = st.find(" ", space, len(st))



print(st[sSpace:])


# message = "In the land of submarines"
# # new = message.replace("land","sea")
# # print(new)

# index = message.find("yellow")
# subIndex = message.find('submarine',index)
# print(message[subIndex])


galleons = float(input("Enter amount of money in Galleons >"))
sickles = float(input("Enter amount of money in Sickles >"))

cad = galleons * 8.43 + sickles * 0.50

print("Sum total value of money $ {sum:.2f} ".format(sum=cad))