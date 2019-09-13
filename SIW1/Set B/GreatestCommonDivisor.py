#import math

def gcd(x, y):
    temp = 0
    while y != 0:
        #(x, y) = (y, x % y)
        temp = x
        x = y
        y = temp % y
    return x

def gcd2(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


num1 = int(input("Type in the first number: "))
num2 = int(input("Type in the second number: "))

print(gcd(num1, num2))
print(gcd2(num1, num2))