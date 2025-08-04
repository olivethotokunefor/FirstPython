amount = int(input("Enter the total amount: "))

if amount >= 1000:
    print("You get a 20% discount!")
    discount = amount * 0.20
    print("Discount:", discount)
    print("Final price:", amount - discount)
elif amount >= 500:
    print("You get a 10% discount!")
    discount = amount * 0.10
    print("Discount:", discount)
    print("Final price:", amount - discount)
elif amount >= 100:
    print("You get a 5% discount!")
    discount = amount * 0.05
    print("Discount:", discount)
    print("Final price:", amount - discount)
else:
    print("No discount.")
    print("Final price:", amount)
