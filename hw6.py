"""homework 6 will develop a multi function program to ask the user for the number of people as well
    as the average number of slices each person will consume to get a total amount of pizza required
    and calculate the cost of said pizza, and divide that cost among the participants"""

import math
# function gets the number of people and average slices
def get_input( ):
    people = int(input("How many people want pizza? "))
    slices = int(input("Average number of slices per person? "))
    #return the nubmer of people and average slices needed
    return{'people':people, 'slices': slices}

#holds the static variables
def static():
    pizza_cost = 15.99
    pie_slices = 8
    tax_rate = .101
    tip_rate = .18
    delivery_fee = 10.99
    #return the static variabes for calculations
    return{'pizza_cost': pizza_cost, "pie_slices": pie_slices, "tax_rate": tax_rate,
           "tip_rate":tip_rate,"delivery_fee": delivery_fee}

#determine how many pizzas we need
def quantity(people,slices, pie_slices):
    #from the number of people and average slices, compute the total number of slices needed
    slices_needed = people * slices
    #from the number of slices needed, round up to get the number of pizzas needed
    pizzas_needed = math.ceil(slices_needed / pie_slices)
    #print the number of pizzas needed
    print('You need ', str(pizzas_needed), ' Pizza Pies')
    #return the number of pizzas needed to compute the costs
    return{'pizzas_needed': pizzas_needed}

#get the total costs with taxes, tip, etc
def costs(pizzas_needed, pizza_cost, tax_rate, tip_rate, delivery_fee):
    #compute the total pizza_cost
    subtotal = pizzas_needed * pizza_cost
    #get the tip and tax amount from the subtotal
    tip_amount = subtotal * tip_rate
    tax_amount = subtotal * tax_rate
    #get the total pizza cost and print it out
    raw_total = subtotal + delivery_fee + tip_amount + tax_amount
    grand_total = '${:,.2f}'.format(raw_total)
    print('Total Pizza cost is ',grand_total)
    #return the unformated total to pass on to cost per person
    return{'raw_total':raw_total}

#get the cost per person
def cost_per_person(people, raw_total):
    raw_per_person = raw_total / people
    cost_per_person = '${:,.2f}'.format(raw_per_person)
    print('Total cost per person is ',cost_per_person)

#main is the control function to call all the other functions, this is the only function executed in main code
def main():
    #contain the user provided variables
    user_input = get_input()
    #contains the static variables
    static_var = static()
    #calculates the amount of pizza we need
    quantity_var = quantity(user_input.get('people'),
                            user_input.get('slices'),
                            static_var.get('pie_slices'))

    #computes the total cost of the pizza with additional charges
    costs_var = costs(quantity_var.get('pizzas_needed'),
                      static_var.get('pizza_cost'),
                      static_var.get('tax_rate'),
                      static_var.get('tip_rate'),
                      static_var.get('delivery_fee')
                     )

    #computes the cost per person
    cost_per_person(user_input.get('people'),
                     costs_var.get('raw_total'))

#call the main function
if __name__ == '__main__':
    main()
