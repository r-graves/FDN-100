"""Homework assignment 3
IN this program I will be asking the user for an input number >= 1, then a subsequent number at least 5 more than their
initial number. I then generate a range from the starting number to the ending number and print out the number and index
from each member of the list that is even. THen SUm all the odd numbers in the list using a for loop. Print the sum of
all numbers"""


def error_check(ef):
    #set the error check to true
    ef = 1
    #check the length of the inputs
    if len(str(user_input1_ch)) == 0\
            or len(str(user_input2_ch)) == 0:
        ef = 0
        print("Sorry, no input detected")
    #confirm they are numeric
    try:
        input_num = int(user_input1_ch)
        input_num2 = int(user_input2_ch)
        #was unclear if second number has to be 5 more than the first, or 5 times the first
        input_num5 = input_num *5
    except:
        ef = 0
        print("Sorry, invalid input detected")
    if ef == 1 and (input_num < 1 or input_num2 < 1):
        ef = 0
        print("Sorry, Input is less than 0")
    if ef == 1 and input_num2 < input_num5:
        ef = 0
        print("Sorry, second number is less than 5 times more than the first " + str(input_num5))
    return bool(ef)

#main_prog generates the ranges from the start to the end
def main_prog():
    input_num1 = int(user_input1_ch)
    input_num2 = int(user_input2_ch)
    ranger = range(input_num1, input_num2)
    odd_balls = []
    #total number of elements in the list
    for index, ranger in enumerate(ranger):
        x = ranger % 2
        if x == 0:
            print(str(ranger)+" is at the "+str(index)+"th index.")
        if x == 1:
            odd_balls.append(ranger)
    print("The total sum of odd numbers is "+str(sum(odd_balls)))




#execution is below. Ask the user for two numbers greater than 0 and 5 or more apart
while True:
    user_input1_ch = input("Please Select a starting number greater than 0: ")
    user_input2_ch = input("Please select an ending number at least times 5 more than the starting number: ")
    if error_check(ef=True):
        main_prog()
        break


