def g(n):
    out = 0

    if n == 1:
        out = 3
    elif n == 2:
        out = 5
    elif n > 2:
        out = 2 * g(n-2) + 7
    else:
        out = -1
    
    return out


# print(g(10))



""" Question 2nd """
def reverseList(list1, out = []):
    length = len(list1)

    if length > 0:
        subList = list1[0: length - 1]
        out.append(list1[-1])
        reverseList(subList, out)

    return out

list2 = [1,2,3,4,5]
# print(reverseList(list2))


""" Question - Prof's style """
def reverseListP(list1):
    length = len(list1)

    if length <= 1:
        result = list1
    else:
        result = reverseListP(list1[1:])
        result.append(list1[0])
    
    return result

# print(reverseListP([1,2,3]))


""" Question 3 """
def sumList(list1):
    length = len(list1)

    if length < 1:
        out = 0
    else:
        out = list1[0] + sumList(list1[1:])
    
    return out

list2 = [1,2,3]
print(sumList(list2))