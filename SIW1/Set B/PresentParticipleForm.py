def isConsonant(word):
    ''' Takes a string and checks the last
    character. If it is consonant returns a
    True value. '''
    for i in range(len(consonants)):
        #print(i)
        if word[-1:] == consonants[i]:
            return True
            break
    return False

string = input("Type in the words separated by white spaces: ")

words = string.split(" ")
exceptions = ["be", "see", "flee", "knee"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
exc = False

print(words)
#print(isConsonant(words[0]))

for i in range(len(words)):
    exc = False
    #indexE = words[i].rfind("e")
    for j in range(len(exceptions)):
        if words[i] == exceptions[j]:
            exc = True
    if exc == False:
        if words[i][-1:] == "e":
            if words[i][-2:] == "ie":
                words[i] = words[i][:-2]
                words[i] += "ying"
            else:    
                words[i] = words[i][:-1]
                words[i] += "ing"
                #print("its an eeee!!!")
        elif isConsonant(words[i]):
            words[i] += words[i][-1:] + "ing"
        else:
            words[i] += "ing"
    else:
        words[i] += "ing"
        #print("!!exception found!")
    print(words[i])