def fact(n):
    out = 0
    if n == 0:
        out = 1
    else:
        out = n * fact(n-1)
    
    return out

# print(fact(5))

# refer 

def palin(word):
    out = True

    if len(word) > 0:
        if word[0] == word[-1]:
            word = word[1: len(word) - 1]
            palin(word)

        else:
            out = False
        
        return out

# print(palin("refer"))