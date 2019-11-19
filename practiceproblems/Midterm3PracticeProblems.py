userArgument = input("input a string: ")

def letterCount(userArgument):
    letterDictionary = {}
    organized = list(userArgument)

    for item in organized:
        if (item in letterDictionary):
            letterDictionary[item] += 1
        else:
            letterDictionary[item] = 1
    
    return letterDictionary

print(letterCount(userArgument))
