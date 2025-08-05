def check_leap_year(year):
    if year % 4 != 0:
        print(year, "is not a leap year.")
    elif year % 100 != 0:
        print(year, "is a leap year.")
    elif year % 400 == 0:
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

input_year = int(input("Enter a year: "))
check_leap_year(input_year)
