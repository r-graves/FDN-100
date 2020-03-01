balance = 0
while True:
    try:
        user_input = int(input("What would you like to do?\n"
                               "1. Get Balance\n"
                               "2. Deposit\n"
                               "3. Withdraw\n"
                               "4. Exit\n"))
        if user_input == 1:
            print("Your balance is ", balance)
        elif user_input == 2:
            amount = float(input("How much do you want to deposit?"))
            balance = balance + amount
        elif user_input == 3:
            amount = float(input("How much do you want to withdraw?"))
            balance = balance - amount
        elif user_input == 4:
            print("Thanks for using our Great Bank!")
            break
        else:
            print("I didn't understand that Hal, try again")
    except ValueError:
        print("Please enter a valid number")

