# # def g(n):

# #     if n == 1:
# #         out = 2
# #     else:
# #         out = 3 * g(n-1) + 4
    
# #     return out

# # print(g(5))


# def exponent(num, m):
#     if num < 0 or m < 0:
#         result = -1
#     else:
#         if m == 1:
#             result = num
#         else:
#             result = num * exponent(num, m- 1)

#     return result

# print(exponent(3, 3))


def printReverse(list1):
    length = len(list1)

    if length > 0:
        print(list1[-1], end=", ")
        printReverse(list1[0 : length-1])


list1 = [1,2,3,4,5]

printReverse(list1)

# ma'am, could I get your LinkedIn username or email, so we could stay connected. I enjoyed my course with you. :) 

# Skyla#1505

# skyla.docx