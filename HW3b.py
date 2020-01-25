"""Fizzbuzz 2.0 Stretch assignment for week 3:
In addition to the original program, this program selects a second random number between 0 and 50 and generates a range
Once again if the number is divisible by 3 I print FIZZ, divisible by 5 I print BUZZ, and if it is divisible by both I
print FIZZBUZZ"""
import random
#generate two random numbers between 50 and 100
num_in = random.randint(50, 100)
num_in2 = random.randint(50,100)

#convert the first number to integer
user_input = int(num_in)
#add the random number and the second random number to get our range
user_input2 = user_input + int(num_in2)
#create the range
ranger = range(user_input, user_input2)
print("START IS " + str(user_input)+"\n"+"END IS "+str(user_input2))
#go through each number in the list created above
for index, ranger in enumerate(ranger):
    #divide the number in the list by 3 or 5
    div_3 = ranger % 3
    div_5 = ranger % 5
    x = div_3 == 0
    y = div_5 == 0
    #with this version, I am creating empty fizz and buzz variables, I will populate them if the number is divisible by 3 or 5
    fizz = ''
    buzz = ''
    #populate fizz or buzz if x or y is true
    if x:
        fizz = "FIZZ"
    if y:
        buzz = "BUZZ"
    #print the results
    print(str(ranger)+" "+fizz+buzz)