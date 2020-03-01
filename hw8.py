"""Homework 8 is the banking file hw8.txt will contain all account numbers and balances
The program will allow the cusotmer to make deposits, withidrawals, set up a new account"""
import csv


#open the file and read it into a dictionary
with open('hw8.txt') as csv_file:
    reader = csv.reader(csv_file)
    accounts = dict(reader)

#bank class
class bank():
    #set up a new account
    def new_acc(self,amount):
        appendix = {self: amount}
        uid = self
        #check to see if the requested user id is already taken
        if uid in accounts.keys():
            print("Sorry, this account id is taken")
        else:
            #f_amount = '${:,.2f}'.format(amount)
            #print welcome message and balance
            print("Welcome to our bank " + uid + ". Your initial balance is $" + amount)
            accounts.update(appendix)
    #account inquiry
    def inquiry(self):
        uid = self.upper()
        #search for the user id, if it is there, print the balance
        if uid in accounts.keys():
             balance = str(accounts.get(uid))
             print("Hello " + str(uid) + ". Your Balance is $" + balance)
        else:
             print("Sorry, we do not have an account under this User ID")
    #depoisit
    def deposit(self):
            ef = 0
            uid = self.upper()
            em = ''
            #get the deposit amount
            deposit = input("Hello " + uid + ". How much would you like to deposit? ")
            try:
               deposit_num = float(deposit)
            except:
                 ef = 1
                 em = ("please enter an amount greater than 0")
            if ef == 0:
               if float(deposit) < 0:
                   ef = 1
                   em = ("please enter an amount greater than 0")
            #add the deposit to the existing balance, print message
            if ef == 0:
                if uid in accounts.keys():
                    balance = str(accounts.get(uid))
                    amount = (float(balance) + deposit_num)
                    msg = ("Thank you " + uid + ". Your old balance was $" + str(balance) + '\n' +
                          "Your new balance is $" + str(amount))
                    print(msg)
                    appendix = {uid: amount}
                    accounts.update(appendix)
                #if a non customer tries to make a deposit
                else:
                    ef = 1
                    em = ("Sorry, you don't appear to have an account with us ")
            if ef == 1:
                print(em)
    #withdrawals
    def wd(self):
        ef = 0
        uid = self.upper()
        #get the amount of withdrawal
        amount = input("Hello " + uid + ". How much would you like to withdraw? $")
        #check if they havean account
        if uid in accounts.keys():
            balance = str(accounts.get(uid))
        else:
            ef = 1
            print("Sorry, it does not appear you have an account at this bank")
        try:
            withdrawal = float(amount)
        except:
            ef = 1
            print("Please enter a withdrawal amount")
        #make sure amount is greater than o
        if ef == 0:
            if withdrawal < 0:
                print("Please specify an amount greater than 0")
                ef = 1
        #compute the new balance after withdrawal, if it is less than 0 print an error message
        if ef == 0:
             new_balance = float(balance) -  withdrawal
             if new_balance < 0:
                 print("Sorry, withdrawal amount exceeds available balance")
                 ef = 1
        #process the withdrawal
        if ef == 0:
            appendix = {uid: str(new_balance)}
            accounts.update(appendix)
            print("Your withdrawal of " + str(withdrawal) + " has been processed." '\n'
                  "Your new balance is " + str(new_balance) )
        if ef == 1:
            print("Please correct the error and try again")

#initial welcome screen
while True:
    try:
        user_input = int(input("What would you like to do?\n"
                               "1. Get Balance\n"
                               "2. Deposit\n"
                               "3. Withdraw\n"
                               "4. Set Up Account\n"
                               "5. Exit\n"))
        if user_input == 1:
           print('Inquiry')
           uid = input("Please enter your User ID: ")
           uid = uid.upper()
           bank.inquiry(uid)
        elif user_input == 2:
           print('Deposit')
           uid = input("Please enter your User ID: ")
           uid = uid.upper()
           bank.deposit(uid)
        elif user_input == 3:
           print("Withdrawal Requested")
           uid = input("Please enter your User ID: ")
           bank.wd(uid)
        elif user_input == 4:
          print("Set up a new account")
          uid = input("Please specify a User ID you would like to use ")
          uid = uid.upper()
          amount = input("How much would you like to deposit? ")
          if uid == '':
              print("Sorry, User ID Not Specified")
          elif uid.count(',') > 0:
              print("UID not allowed")
          else:
              bank.new_acc(uid, amount)
        elif user_input == 5:
            print("Thanks for using our Great Bank!")
            break
        else:
            print("I didn't understand that Hal, try again")
    except ValueError:
        print("Please enter a valid number ERROR")

#once we are done write the accounts to a file for the next time
with open('hw8.txt', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in accounts.items():
       writer.writerow([key, value])