def inputNumber():
    accepted = False
    while not accepted:
        num = input("Please type in a number between 0 and 4000: ")
        try:
            num = int(num)
            if num > 0 and num < 4000:
                accepted = True
                return num
        except:
            print("Try again!")
        
def toRomanNumerals(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    romanNum = ""
    i = 0
    while num > 0:
        for k in range(num // values[i]):
            #print("{} // {} = {}".format(num, val[i], num // val[i]))
            romanNum += symbols[i]
            num -= values[i]
        #print("i = {}".format(i))
        i += 1
    return romanNum

number = inputNumber()
print(toRomanNumerals(number))