import random

num_in = random.randint(50, 100)
user_input = int(num_in)
div_3 = user_input % 3
div_5 = user_input % 5


x = div_3 == 0
y = div_5 == 0
if x and y:
    print("FIZZBUZZ")
elif x:
    print("FIZZ")
elif y:
    print("BUZZ")
else:
    print(user_input)

