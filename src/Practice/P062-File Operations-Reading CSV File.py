#File Operations - Reading CSV File

'''
import csv

with open('ExampleCSV.csv') as csvfile:
    reader = csv.reader(csvfile)
    for col in reader:
        print(col[0],col[1],sep="|")
'''

#The same above program can be written in a simplified way
# For this you need to install pandas in Terminal
# Type pip install pandas to install it

import pandas as pd

df = pd.read_csv("ExampleCSV.csv")
print(df)