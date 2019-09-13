import sys

def findAnagrams():
    found = False
    for i in range(len(anagramsSorted)):
        if anagramsSorted[i] == "".join(sorted(str)):
            print(anagrams[i])
            found = True
    if found == False:
        print("Didn't find any pair!")

#testWords = ["Béla", "Jancsi"]
anagrams = []
anagramsSorted = []

try:
    fileName = sys.argv[1]
except IndexError:
    print("Must have 1 argument! (Anagram.py <pathtofile>)")
    exit()
except FileNotFoundError:
    print("Wrong argument! (Anagram.py <pathtofile>)")
    exit()

str = input("Type in the word: ")

with open(fileName, "r") as f:
    anagrams = f.read().split("\n")

for i in range(len(anagrams)):
    sortedStr = "".join(sorted(anagrams[i]))
    anagramsSorted.append(sortedStr)
#print(anagramsSorted)
findAnagrams()
f.close()