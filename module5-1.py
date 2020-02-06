#f = open("./land_time_forgot.txt")
# creates a file handle
#f
#<_io.TextIOWrapper name='./land_time_forgot.txt' mode='r' encoding='UTF-8'>


# write a string to file
with open('output.txt', 'w') as f:
    my_string = "stuff"
    f.write(my_string)

# appending a list of lines to a file
out_lines = ["Hello there! This is my first line! \n",
    "This is the second line \n",
    "This is the last time I'm doing this..."]

with open('output.txt', 'a') as f:
    f.writelines(out_lines)