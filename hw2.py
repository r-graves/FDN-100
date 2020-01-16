"""this isthe homework assignment for week 2. I will create a query that will query purchaser name, address, phone,
car make-model and purchase price

program will then generate taxes, licnese, prep, and generate a total cost as a float as well as a unique id consisting of
the first four charcters of the last name, and their area code seperated by an underscore

"""
def cust_func():
    #query for customer information
    cust_name = input("Customer Name (first and last):  ")
    cust_address = input("Customer Street Address: ")
    cust_city = input("Customer City and State: ")
    cust_zip = input("Customer Zip Code: ")
    cust_phone = input("Customer Phone Number (seperated by '-': ")
    #query for the car information
    purchase_price = input("Purchase Price: ")
    car_make = input("Car Make: ")
    car_model = input("Car Model: ")

    #license and prep fees are constant
    license_fee = 50
    prep_fee = 50


    #if the customer lives in 981 (Seattle) scf compute the sales tax at 10.1%
    #if the customer lives in 606 (Chicago) scf compute the sales tax at 10.25%
    #else 0
    scf = str(str(cust_zip)[:3])
    if scf == "981":
        tax_amt = float(purchase_price) * .101
    elif scf == "606":
        tax_amt = float(purchase_price) * .1025
    else:
        tax_amt = 0
    #compute the total price as a float
    total_price = float(purchase_price) + tax_amt + prep_fee + license_fee

    #customer id is the last four characters of the customers last name plus their area code
    #customer area code
    phone_split = (cust_phone.split("-"))
    area_code = phone_split[0]
    #find the customers last name
    name_split = (cust_name.split(" "))
    last_name = str(name_split[1])
    name_length = len(last_name)
    #if last name le 4 characters put out the whole name. Otherwise, put out the final four characters
    if name_length <= 4:
        uid_name = last_name
    else:
        uid_name = str(last_name[name_length - 4:])
    tran_id = uid_name.upper() + "_" + area_code
    #Generate the final message
    str_out1 = "Hello " + cust_name + "! \n"
    str_out2 = "Thank you for your purchase of a " + car_make + " " + car_model + ". Following is a break down of you total price: \n"
    str_out3 = "Sales Price: $" + purchase_price + "\n"
    str_out4 = "Tax: $" + str(round(tax_amt)) + "\n"
    str_out5 = "License Fee: $" + str(license_fee) + "\n"
    str_out6 = "Dealer Prep Fee: $" + str(prep_fee) + "\n"
    str_out7 = "Total Price : $" + str(round(float(total_price))) + "\n"
    str_out8 = "You have been assigned an ID Number of "+ tran_id + ". Please refer to this ID Number if you have any questions \n"
    #print the final message
    print(str_out1)
    print(str_out2)
    print(str_out3)
    print(str_out4)
    print(str_out5)
    print(str_out6)
    print(str_out7)
    print(str_out8)


cust_func()
