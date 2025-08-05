def calculate_discount(amount):
    if amount > 500:
        print("You get a 20% discount!")
        discount = amount * 0.20
    elif amount > 100:
        print("You get a 10% discount!")
        discount = amount * 0.10
    else:
        print("No discount.")
        discount = 0

    final_price = amount - discount
    print("Discount:", discount)
    print("Final price:", final_price)

user_amount = int(input("Enter the total amount: "))
calculate_discount(user_amount)
