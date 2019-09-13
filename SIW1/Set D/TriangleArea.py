import math

def inputSides():
    vertices = []
    temp = []
    j = 0
    for i in range(3):
        #print("Lefut {}".format(i))
        while j < 2:
            j += 1
            vertex = input("{}. coordinate {}. vertex: ".format(i + 1, j))
            try:
                vertex = int(vertex)
                if vertex > 100 or vertex < -100:
                    print("Too high/low number!")
                    j -= 1
                else:
                    temp.append(vertex)
            except:
                print("Try again!")
                j -= 1
        vertices.append(temp)
        temp = []
        j = 0
    #print(vertices)
    return vertices

def calcSides(coords):
    tmp = []
    a = math.sqrt(pow(coords[0][0] - coords[1][0], 2) + pow(coords[0][1] - coords[1][1], 2))
    b = math.sqrt(pow(coords[1][0] - coords[2][0], 2) + pow(coords[1][1] - coords[2][1], 2))
    c = math.sqrt(pow(coords[0][0] - coords[2][0], 2) + pow(coords[0][1] - coords[2][1], 2))
    tmp.extend((a, b, c))
    return tmp

def calcArea(sides):
    s = (sides[0] + sides[1] + sides[2]) / 2
    area = math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))
    print(s)
    #area = 
    result = round(area, 1)
    if result.is_integer():
        return int(result)
    else:
        return result

coordinates = inputSides()
sides = calcSides(coordinates)
area = calcArea(sides)

#print(coordinates)
#print(sides)
print(area)