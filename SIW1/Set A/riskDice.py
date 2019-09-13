import random

attackerRolls = []
defenderRolls = []
defLost = 0
atkLost = 0

def printStatus():
    print("Dice:")
    print("  Attacker: ", end="")
    for i in range(len(attackerRolls)):
        if i == len(attackerRolls) - 1:
            print("{}".format(attackerRolls[i]))
        else:
            print("{}-".format(attackerRolls[i]), end="")
    print("  Defender: ", end="")
    for i in range(len(defenderRolls)):
        if i == len(defenderRolls) - 1:
            print("{}".format(defenderRolls[i]))
        else:
            print("{}-".format(defenderRolls[i]), end="")

def printOutcome():
    print("Outcome:")
    print("  Attacker: lost {} units".format(atkLost))
    print("  Defender: lost {} units".format(defLost))

def battle():
    global defLost, atkLost
    min = len(attackerRolls)
    if len(attackerRolls) > len(defenderRolls):
        min = len(defenderRolls)
    for i in range(min):
        if attackerRolls[i] > defenderRolls[i]:
            defLost += 1
        else:
            atkLost += 1

def setup():
    attackers = input("How many units attack: ")
    defenders = input("How many units defend: ")
    while not(attackers.isnumeric()) or not(defenders.isnumeric()):
        attackers = input("How many units attack: ")
        defenders = input("How many units defend: ")
    attackers = int(attackers)
    defenders = int(defenders)

    while (attackers > 3 or attackers < 1) or (defenders > 2 or defenders < 1):
        print("Retry please!")
        attackers = int(input("How many units attack: "))
        defenders = int(input("How many units defend: "))
    
    for i in range(attackers):
        attackerRolls.append(random.randrange(1,7))
    for i in range(defenders):
        defenderRolls.append(random.randrange(1,7))

setup()
printStatus()
battle()
printOutcome()