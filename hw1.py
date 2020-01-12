"""This is a program I created for the first week homwork assignment"""
# validate the user has entered a value for name
def name_validation(nv):
    #did user put in a name?
    if len(user_name) == 0:
        print("USER ERROR 213488898: ENTER A VALID NAME")
        nv = False
    else:
        nv = True
    #return true falue if name in proper format
    return bool(nv)

#validate the user has put in a value for location
def location_validation(lv):
    #did user put in a location?
    if len(user_loc) == 0:
        print("USER ERROR 394879 ENTER A VALID LOCATION")
        lv = False
    else:
        lv = True
    #return true value if locaiton in proper format
    return bool(lv)

#validate the number selected
def num_validation(nbr):
    nbr = True
    #make sure number is numeric
    try:
        int(num_in)
    except:
        print("USER ERROR 9737789789: ENTER A NUMBER")
        nbr = False
    #if numeric make sure the number is between 1 and 10
    if nbr is True:
        if 1 < float(num_in) > 10:
            nbr = False
            print("USER ERROR 8978769867: NUMBER OUTSIDE VALID RANGE")
    #return true value if number in proper foramat
    return bool(nbr)

#query for user name location and a number between 1 and 10
user_name = input("What is your name? ")
user_loc = input("what is your location? ")
num_in = input("Enter a Number between 1 and 10: ")
#make sure number name and location are valid
if name_validation(nv=True) and location_validation(lv=True) and num_validation(nbr=True):
    j = 1
    k = int(num_in)
    #loop through message however many times the user selected
    while j <= k:
        print(user_name, "is at", user_loc, "for the", j, "out of", k, "times.")
        j = j + 1
#if name location or number in are not valid, print a final error message
else:
    print("CORRECT YOU ERROR AND TRY AGAIN")
