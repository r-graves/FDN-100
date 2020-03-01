import click
#try to open a file that does not exist
def file_read():
    #try to open the file
    infile = click.prompt('Please enter a file name: ')

    try:
       fin = open(infile,'r')
       print("Reading from file:")
       for x in fin:
           print(x)
    #what if the file can't be opened
    except:

        print('Unable to open specified file')


if __name__ == '__main__':
    file_read()
