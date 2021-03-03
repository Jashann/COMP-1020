
# days = {1:"Sunday", 2:"Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thursday", 6:"Friday", 7:"Saturday" }

# months = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July",
#             8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}

# monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]

# def getMonth():
#     inputIsValid = False
#     while not inputIsValid:
#         monthInput = input("Enter a month in number >> 1 to 12 << : ")
#         if monthInput.isnumeric():
#             month = int(monthInput)
#             if month >= 1 and month <= 12:
#                 inputIsValid = True
#     return month

# def getDayOfMonth(month):
#     inputIsValid = False
#     while not inputIsValid:
#         dayInput = input("Enter a day in number >> 1 to 31 << : ")
#         if dayInput.isnumeric():
#             day = int(dayInput)
#             if day >= 1 and day <= monthDays[month - 1]: # as index starts at 0
#                 inputIsValid = True
#     return day

# def getWeekDay():
#     inputIsValid = False
#     while not inputIsValid:
#         dayInput = input("Enter a day in number >> 1 to 7<< : ")
#         if dayInput.isnumeric():
#             day = int(dayInput)
#             if day >= 1 and day <=7: # as index starts at 0
#                 inputIsValid = True
#     return day

# def getYear():
#     inputIsValid = False
#     while not inputIsValid:
#         yearInput = input("Enter a year: ")
#         if yearInput.isnumeric():
#             year = int(yearInput)
#             if year >= 1900 and year <= 2100:
#                 inputIsValid = True
#     return year


# monthInput = getMonth()
# weekDayInput = getWeekDay()
# dayOfMonth = getDayOfMonth(monthInput)
# year = getYear()


# weekDay = days[int(weekDayInput)]
# month = months[int(monthInput)]

# "Sunday, 2 October 2020"
# print(f"{weekDay}, {dayOfMonth} {month} {year}")




def sumList(numList):
    sum = 0
    for num in numList:
        sum += num
    return sum


def max(num1, num2):
    if num1 > num2:
        return num1
    return num2

def getFibonacciNum(num):
    first = 0
    second = 1

    count = 1 

    if num == 0:
        return 0
    
    while count < num:
        third = first + second
        first = second
        second = third
        count += 1

    return second
