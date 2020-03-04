import pandas as pd
import requests
import csv
import matplotlib
import io

# run plots in the notebook
#%matplotlib inline
url = 'http://pbpython.com/extras/sample-salesv2.csv'
x = requests.get(url).content
sales = pd.read_csv(io.StringIO(x.decode('utf-8')))



#print(sales)
#rename the columns
sales.columns = ['account_number', 'name','sku', 'category','quantity','unit_price','ext_price', 'date']
#subset name quantity and unit price
sales2 = sales[['name','category','quantity','unit_price']]
#print(sales2)
#calculate the total shirt sales
shirt_sales = sum(sales['unit_price'])
sales3 = sales[['category','unit_price']]
s3 = sales3.groupby('category').sum()
#print(s3)
#shirt sales 23236.57
#get the shirt sales by company
sales4 = sales[sales['category'] == "Shirt"]
sales5 = sales4[['name','unit_price']]
s4 = sales5.groupby('name').sum()
#s5 = sales4.groupby('name')
#print(s4)
#pull out the top 10 shirt sales


