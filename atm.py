def atm_operations(balance):
    print("Welcome to the ATM")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")

    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        print("Your current balance is:", balance)

    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print("Deposit successful!")
            print("New balance is:", balance)
        else:
            print("Invalid deposit amount.")

    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            balance -= amount
            print("Withdrawal successful!")
            print("New balance is:", balance)

    else:
        print("Invalid option.")

    return balance

user_balance = float(input("Enter your starting balance: "))
user_balance = atm_operations(user_balance)
