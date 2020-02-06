# open file
with open("./land_time_forgot.txt", "r") as f:
    # read lines into a list
    flines = f.readlines()

    # calculate beginning of the middle third of the file
    onethird = len(flines) // 3
    # calculate beginning and of the middle third of the file
    twothirds = len(flines) * 2 // 3

    # place to store the middle third of the file
    mthirdlines = flines[onethird:twothirds]

    print("\nThe number of lines in the file:", len(flines))
    print("\nThe number of lines in the middle third of the file:", len(mthirdlines))

    print("\nThe line that is 1/3 of the way through file:")
    print(flines[onethird].strip())
    print("\nThe line that is 2/3 of the way through file:")
    print(flines[twothirds].strip())



