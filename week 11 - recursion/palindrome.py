def palin(word):

    if len(word) == 0 or len(word) == 1:
        return True
    else:
        if word[0] == word[-1]:
            return palin(word[1:-1])
        else:
            return False

def checkPalin(word):
    if palin(word):
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")