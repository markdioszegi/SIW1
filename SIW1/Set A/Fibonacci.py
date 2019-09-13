def subtract(num, strt):
    if num >= 0 and num < 9:
        return strt
    elif num >= 9 and num < 99:
        #print("faszom")
        return strt - 1
    elif num >= 99 and num < 999:
        return strt - 2
    elif num >= 999 and num < 9999:
        return strt - 3


numbers = int(input("How many numbers do you want to print out? "))
i = 0
j = 1
k = 0
fib = 0
start = 40
rAlign = 0
while i < numbers:
    rAlign = subtract(i, start)
    print("{}:{:>{}}".format(i + 1, fib, rAlign))
    fib = j + k
    j = k
    k = fib
    i += 1