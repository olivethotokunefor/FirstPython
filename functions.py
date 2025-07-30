# def addition():
#     a=5
#     b=5
#     result = a+b
#     print(result)

# addition()

# def check_even_odd(num):
#     if(num % 2 ==0):
#         print("It is an even number")
#     else :
#         print("It is an odd number")

# check_even_odd(11)

def check_positive(num):
    # num = input("Enter the number: ")

    if(num < 0):
        print("Number is a negative number")
    else:
        print("Number is a positive number")

check_positive(10)


def double():
    num1 = input("Enter the number: ")
    result= int(num1) * 2
    print(result)

double()
