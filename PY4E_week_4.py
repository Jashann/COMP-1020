"""
author: Jashanjot Singh Gill
github: https://github.com/Jashann
portfolio: https://jashann.github.io/
email: jashangill3592@gmail.com
message: if you find a bug, please do let me know.
"""

""" Lesson - 6 (String) 
Program 1 - Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards. 
"""

def reverse():
    word = input("Enter a word > ")
    itreate = len(word) - 1
    while itreate >= 0:
        print(word[itreate])
        itreate -= 1

# reverse()

# word = "jashan"
# print(word[::])


""" Lesson - 6 (String)
Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments. 
"""

def count(sentence, letterToBeCounted):
    count = 0
    for char in sentence:
        if char.lower() == letterToBeCounted.lower():
            count += 1
    print("'{}' is present in the sentense: \"{}\", {} times ".format(letterToBeCounted, sentence, count))

# count('I am Jashanjot', 'J')


""" Lesson - 6 (String) 
Exercise 5: Take the following Python code that stores a string:

str = 'X-DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.
"""

def extractSubsring():
    str = 'X-DSPAM-Confidence:0.8475'
    index = str.find(":")
    numberString = str[index+1:].strip()
    number = float(numberString)
    print(number)

# extractSubsring()


# str = "jashan.com"
# print(str.strip(".com")) # returns jashan

# str = "jashan"
# print(str.replace("a", "#", 1)) 

"""
str.replace(old, new[, count])
Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.
"""



# format Operator
# print('%d' % 123)