import time
import random

class Player:

    playerList = []

    def __init__(self, name, armySize, diceValue):
        self.name = name
        self.armySize = armySize
        self.diceValue = diceValue
        self.playerList.append(self)

def rollTheDice():
    wait()
    max = 0
    index = 0
    for i in range(len(Player.playerList)):
        rand = random.randrange(1, 6)
        Player.playerList[i].diceValue = rand
        if Player.playerList[i].diceValue > max:
            max = rand
            index = i
        else:
            pass
        print(Player.playerList[i].name + " rolled a {}!".format(rand))
    print("{} rolled the highest!".format(Player.playerList[index].name))
    
def wait():
    time.sleep(0)

def choosePlayerNames(a):   #also create it
    i = 0
    while i < a:
        name = input("Player {} name: ".format(i + 1))
        Player(name, 0, 0)
        i += 1
        wait()

def assignTroops():
    size = 0
    if len(Player.playerList) == 2:
        size = 40
    elif len(Player.playerList) == 3:
        size = 35
    elif len(Player.playerList) == 4:
        size = 30
    elif len(Player.playerList) == 5:
        size = 25
    elif len(Player.playerList) == 6:
        size = 20
    for i in range(len(Player.playerList)):
        Player.playerList[i].armySize = size

def placeTroops():
    print("It's time to place your armies! Rolling the dice who starts first...")
    rollTheDice()
    """ for i in range(len(Territories.terrList)):
        pass """

print("***Unofficial modified game of Risk***")

numberOfPlayers = int(input("Type in the number of players (2-6): "))
while numberOfPlayers < 2 or numberOfPlayers > 6:
    print("Try again!")
    numberOfPlayers = int(input())
wait()
choosePlayerNames(numberOfPlayers)
assignTroops()
placeTroops()

#print(Player.playerList[0].name)