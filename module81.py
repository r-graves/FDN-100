class Critter():
    total = 0

    def __init__(self, name):
        # name is an attribute of the Critter class
        # every Critter will have a name, but the name does not have to be the same
        self.name = name
        print("A new critter, {}, has been born!".format(self.name))
        Critter.total += 1

    # define a method, using the self parameter
    def talk(self):
        print("Hi. I'm {}".format(self.name))

    # using python's __str__ method
    def __str__(self):
        rep = "Critter object\n "
        rep += "name: {} \n".format(self.name)
        return rep



crit = Critter("Hopper")




#continuaiton of examples from class
#official solution to module 1

# define class Calculate
class Calculate:

    # init object and set its name to the name input or "default" if no value given
    def __init__(self, name="default"):
        self.name = name
        self.uses = 0

    # add input a and b and increment object uses
    def add(self, a, b):
        self.uses += 1
        return a + b

    # subtract input a and b and increment object uses
    def subtract(self, a, b):
        self.uses += 1
        return a - b

    # multiply input a and b and increment object uses
    def multiply(self, a, b):
        self.uses += 1
        return a * b

    # divide input a and b and increment object uses
    def divide(self, a, b):
        self.uses += 1
        return a / b

# create object calc of class Calculate
calc = Calculate("firstCalc")

# run and print calculations
print("Running calculations using calc object named {}".format(calc.name))
print(calc.add(4,2))
print(calc.subtract(4,2))
print(calc.multiply(4,2))
print(calc.divide(4,2))

# print number of times the current calc object has been used
print("calc object '{}' has performed {} calculations".format(calc.name, calc.uses))

