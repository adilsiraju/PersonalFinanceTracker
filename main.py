import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_desc

class CSV:
    CSV_FILE = "FinanceData.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    DATEFORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)
    
    @classmethod
    def add_entry(cls, date, amount, category, desc):
        new_entry = {
            "date" : date,
            "amount" : amount,
            "category" : category,
            "description" : desc
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully.")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=CSV.DATEFORMAT)
        start_date = datetime.strptime(start_date, CSV.DATEFORMAT)
        end_date = datetime.strptime(end_date, CSV.DATEFORMAT)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transactions found in the given date range.")
        else:
            print(f"Transactions from {start_date.strftime(CSV.DATEFORMAT)} to {end_date.strftime(CSV.DATEFORMAT)}")
            print(filtered_df.to_string(
                    index=False, formatters={"date": lambda x: x.strftime(CSV.DATEFORMAT)}
                )
            )

            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()

            print("\nSummary:")
            print(f"Total Income: ₹ {total_income:.2f}")
            print(f"Total Expense: ₹ {total_expense:.2f}")

            print(f"Net Savings: ₹ {(total_income-total_expense):.2f}")

            print("-------------------------------------------------")

        return filtered_df


def add():
    CSV.initialize_csv()    
    date = get_date("Enter date of transaction (dd-mm-yyyy) or enter for todays date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    desc = get_desc()

    CSV.add_entry(date, amount, category, desc)

def main():
    while True:
        print('''
              \n1. Add Transaction.
              \n2. View Transaction & summary within a date range.
              \n3. Exit
              ''')
        choice = input("What would you like to do ?: ")
        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter start date in dd-mm-yyyy format: ")
            end_date = get_date("Enter end date in dd-mm-yyyy format: ")
            print("-------------------------------------------------")
            df = CSV.get_transactions(start_date, end_date)
        elif choice == "3":
            print("\nExiting...")
            break
        else:
            print("Invalid Choice.")

if __name__ == "__main__":
    main()