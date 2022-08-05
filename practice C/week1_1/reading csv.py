import csv

f=open('customers.csv','r')

x_reader=csv.reader(f)
print(x_reader)
print(type(x_reader))

