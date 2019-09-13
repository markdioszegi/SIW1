c = 0
for i in range(100, 1000):
    if c < 25:
        if (i % 7 == 0) or (i % 9 == 0):
            print("{}.: {}".format(c + 1, i))
            c += 1