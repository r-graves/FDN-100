"""Homework assignment 4 will read in the names and ages of students to a dictionary. The user will get 5 attempts
    at guessing a student name. If they succeed, they will get the user age. If they fail 5 times, they will get an error
    message and kicked out of the loop"""
#bring in the names and ages
names = ["Aliyah", "Bob", "Cathy", "Dan", "Ed", "Frank", "Darnell", "Gary", "Shanice", "Irene", "Jack", "Kelly", "Demetrius"]
ages = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19, 30]
#bring names and ages together in a zip file
age_dir = dict(zip(names, ages))
#age_ty = type(age_dir)
#age_dir type is a dictionary 'dict'

def age_get():
    #x counts the number of attempts
    x = 0
    y = 0
    while x < 5:
        #get the name of the student
        student_name_input = input("What is the student you would like to know the age of? ")
        #if the name is not in the proper format, convert it to Title format
        student_name = student_name_input.title()
        #response for a blank name
        if len(student_name) == 0:
            print("No input received")
            x = x + 1
        #if the student is in the data, return the age
        elif student_name in age_dir.keys():
            #note below the conversion of student age to string
            student_age = str(age_dir.get(student_name))
            #string together the valid response and print
            string_valid = student_name + " is "+ student_age
            print(string_valid)
            #flag for having guessed a student name
            y = 1
            break
        else:
            print("Sorry, the requested name, "+ str(student_name) +  " is not in our database")
            #increment the counter by 1
            x = x + 1
    #too many errors
    #when you have failed at your five attempts, you go here
    if y == 0:
        print("Sorry, it does not appear you know any students")

age_get()
