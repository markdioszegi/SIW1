import sys
from io import *

fileName = "SI W1\Set A\IdeaBank.txt"

def writeIntoFile(idea):
    try:
        f = open(fileName, "a")
        f.writelines(idea + "\n")
    finally:
        f.close()

def printIdeaBank():
    try:
        f = open(fileName, "r")
        ideas = f.readlines()
    finally:
        f.close()
    print("Your idea bank:")
    for i in range(len(ideas)):
        print("{}. {}".format(i + 1, ideas[i]), end="")

def deleteLine(lineToDelete):
    try:
        f = open(fileName, "r")
        lines = f.readlines()
    finally:
        f.close()
    try:
        f = open(fileName, "w")
        for pos, line in enumerate(lines):
            if pos != lineToDelete - 1:
                f.write(line)
    finally:
        f.close()

if len(sys.argv) == 1:
    idea = input("What is your new idea? :) ")
    writeIntoFile(idea)
    printIdeaBank()
elif sys.argv[1] == "--list":
    printIdeaBank()
elif sys.argv[1] == "--remove":
    deleteLine(int(sys.argv[2]))
    printIdeaBank()