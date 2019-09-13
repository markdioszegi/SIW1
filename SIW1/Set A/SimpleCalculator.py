def calculate(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    else:
        return num1 / num2

number = input("Enter a number (or a letter to exit): ")
if not number.isnumeric():
    exit()
operation = input("Enter an operation: ")
if operation == "+" or operation == "-" or operation == "*" or operation == "/":
    number2 = input("Enter another number: ")
    if not number2.isnumeric():
        exit()
    number = float(number)
    number2 = float(number2)
    result = calculate(number, operation, number2)
    if result.is_integer():
        print("Result: {}".format(int(result)))
    else:
        print("Result: {}".format(result))
else:
    print("Wrong operation!")
    exit()