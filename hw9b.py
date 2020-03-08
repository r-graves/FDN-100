"""Homework 8 is the banking file hw8.txt will contain all account numbers and balances
The program will allow the cusotmer to make deposits, withidrawals, set up a new account"""
import csv


#open the file and read it into a dictionary
def importer():
    with open('sample_superstore.csv') as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)
        return data

data_in = importer()

print(data_in)