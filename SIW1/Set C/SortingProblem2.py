def inputNumbers():
    str = input("Please type in numbers separated by spaces! (1 5 8): ")
    global numbers
    numbers = str.split(" ")
    for i in range(len(numbers)):
        try:
            numbers[i] = int(numbers[i])
        except:
            print("Please follow the example!")
            inputNumbers()

numbers = []
inputNumbers()

print(numbers)
N = len(numbers)

i = 1

while i < N:
    j = 0
    while j <= N - 2:
        if numbers[j] > numbers[j + 1]:
            (numbers[j + 1], numbers[j]) = (numbers[j], numbers[j + 1])
            """ temp = numbers[j + 1]
            numbers[j + 1] = numbers[j]
            numbers[j] = temp """
        j += 1
    i += 1

print(numbers)