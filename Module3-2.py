"""Ask user for a number between 1 and 10, give them 3 attempst using a wille loop"""
import random

# pick the number
num_in = random.randint(1, 10)
response = "The number is " + str(num_in)
print(response)
print("Welcome to random number thingie. Please guess a number between 1 and 10. For your convienience, the correct response is above")


def chose_here():
    #x is the sentry variable
    x = 0
    z = 0
    #user gets three chances
    while x < 3:
        #increment the sentry variable
        x = x + 1
        #query user input
        user_input = input("What is your guess? ")
        #if correct
        if user_input == num_in:
            print("congratulations")
            z = 1
            break
        #if incorrect
        else:
            if user_input < num_in:
                var_out = "Sorry, " + str(user_input) +  " is less than " + str(num_in)
                print(var_out)
            if user_input > num_in:
                var_out = "Sorry, "+ str(user_input) + " is greater than " + str(num_in)
                print(var_out)
    #print if they are out of choices
    if z == 0:
        print("GAME OVER")

chose_here()



