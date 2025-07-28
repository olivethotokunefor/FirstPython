print("Welcome to my calculator")


num1 =input("Enter the first number: ")
num2 = input("Enter the second number: ")
opr = input("Enter the operator(+,-,/,*): ")

if opr=="+":
    print(int(num1) + int(num2))
elif opr=="-":
     print(int(num1) - int(num2))
elif opr=="/":
      print(int(num1) / int(num2))
elif opr=="*":
      print(int(num1) * int(num2))
else :
     print("Invalid operator")