import pandas as pd
import csv

class Test_CRUD():

    def test_update_1(self):
        with open('src/Practice/userdata.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row[0], row[1])

    def test_update_2(self):
        df = pd.read_csv('src/Practice/userdata.csv')
        print(df)