def find_maximum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print("The maximum number is:", num1)
    elif num2 >= num1 and num2 >= num3:
        print("The maximum number is:", num2)
    else:
        print("The maximum number is:", num3)

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

find_maximum(n1, n2, n3)
