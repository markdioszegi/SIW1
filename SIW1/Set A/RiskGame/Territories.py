#Continents = [["North America"], ["Alaska", "North West Territory", "Greenland", "Alberta", "Contairo", "Quebec", "Western United States", "Eastern United States", "Central America"]]
class Territories():

    terrList = []

    def __init__(self, continentName, countryName, player, army):
        self.continentName = continentName
        self.countryName = countryName
        self.player = player
        self.army = army
        self.terrList.append(self)

    def getArmy(country):
        for i in range(len(Territories.terrList)):
            if Territories.terrList[i].countryName == country:
                return Territories.terrList[i].army
            else:
                return "Didnt find it!"

    def putArmy(self, country, player, size):
        pass

Territories("North America", "Alaska", "", 0)
Territories("North America", "North West Territory", "", 0)
Territories("North America", "Greenland", "", 0)
Territories("North America", "Alberta", "", 0)
Territories("North America", "Contairo", "", 0)
Territories("North America", "Quebec", "", 0)
Territories("North America", "Western United States", "", 0)
Territories("North America", "Eastern United States", "", 0)
Territories("North America", "Central America", "", 0)
Territories("South America", "Venezuela", "", 0)
Territories("South America", "Peru", "", 0)
Territories("South America", "Brazil", "", 0)
Territories("South America", "Argentina", "", 0)
Territories("Europe", "Iceland", "", 0)
Territories("Europe", "Scandinavia", "", 0)
Territories("Europe", "Ukraine", "", 0)
Territories("Europe", "Great Britain", "", 0)
Territories("Europe", "Northern Europe", "", 0)
Territories("Europe", "Western Europe", "", 0)
Territories("Europe", "Southern Europe", "", 0)
Territories("Africa", "North Africa", "", 0)
Territories("Africa", "Egypt", "", 0)
Territories("Africa", "Congo", "", 0)
Territories("Africa", "East Africa", "", 0)
Territories("Africa", "South Africa", "", 0)
Territories("Africa", "Madagascar", "", 0)
Territories("Asia", "Ural", "", 0)
Territories("Asia", "Siberia", "", 0)
Territories("Asia", "Yakutsk", "", 0)
Territories("Asia", "Kamchatka", "", 0)
Territories("Asia", "Irkutsk", "", 0)
Territories("Asia", "Mongolia", "", 0)
Territories("Asia", "Japan", "", 0)
Territories("Asia", "Afghanistan", "", 0)
Territories("Asia", "China", "", 0)
Territories("Asia", "Middle East", "", 0)
Territories("Asia", "India", "", 0)
Territories("Asia", "Siam", "", 0)
Territories("Asia", "Ural", "", 0)
Territories("Australian Archipelago", "Indonesia", "", 0)
Territories("Australian Archipelago", "New Guiena", "", 0)
Territories("Australian Archipelago", "Western Australia", "", 0)
Territories("Australian Archipelago", "Eastern Australia", "", 0)

""" for i in range(5):
    Territories.countries.append((input("Add a country: "))) """
'''for i in range(len(Territories.countries)):
    print()'''

#print(Territories.terrList[0].countryName)
print(Territories.getArmy("Alaska"))