import pandas as pd
import matplotlib.pyplot as plt
import csv #has DictWriter

class CSV:
    
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date","amount","category","description"]

    @classmethod
    def initialize_csv(cls): #getting the csv file ready
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE,index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date" : date,
            "amount" : amount,
            "category" : category,
            "description":description
        }

        with open(cls.CSV_FILE,"a",newline="") as csvfile:
            writer = csv.DictWriter(cls.CSV_FILE, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully!")

CSV.initialize_csv()