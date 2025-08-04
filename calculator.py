def calculator():
    num1 = input("Enter the first number: ")
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = input("Enter the second number: ")

    num1 = int(num1)
    num2 = int(num2)

    if operator == '+':
        print("Result:", num1 + num2)
    elif operator == '-':
        print("Result:", num1 - num2)
    elif operator == '*':
        print("Result:", num1 * num2)
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print("Result:", num1 / num2)
    elif operator != '+' and operator != '-' and operator != '*' and operator != '/':
        print("Error: Unsupported operator.")


calculator()
