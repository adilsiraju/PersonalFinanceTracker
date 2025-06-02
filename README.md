# 💰 Personal Finance Tracker

A simple and intuitive command-line application to track your personal finances, built with Python. Keep track of your income and expenses, view transaction history, and get financial summaries within custom date ranges.

## ✨ Features

- 📝 **Add Transactions**: Record income and expense transactions with date, amount, category, and description
- 📅 **Date Flexibility**: Use today's date by default or specify custom dates
- 📊 **Financial Summary**: View total income, expenses, and net savings for any date range
- 💾 **CSV Storage**: All data is stored in a CSV file for easy access and portability
- 🔍 **Transaction History**: View filtered transactions within specific date ranges
- ✅ **Input Validation**: Robust validation for dates, amounts, and categories

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pandas library

### Installation

1. Clone or download this repository
2. Install required dependencies:
   ```bash
   pip install pandas
   ```

### Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Choose from the menu options:
   - **Option 1**: Add a new transaction
   - **Option 2**: View transactions and summary within a date range
   - **Option 3**: Exit the application

## 📖 How to Use

### Adding Transactions

1. Select option `1` from the main menu
2. Enter transaction details:
   - **Date**: Use `dd-mm-yyyy` format or press Enter for today's date
   - **Amount**: Enter a positive number
   - **Category**: Choose `I` for Income or `E` for Expense
   - **Description**: Add an optional description

### Viewing Transactions

1. Select option `2` from the main menu
2. Enter start date and end date in `dd-mm-yyyy` format
3. View:
   - All transactions within the specified date range
   - Total income for the period
   - Total expenses for the period
   - Net savings (income - expenses)

## 📁 File Structure

```
PersonalFinanceTracker/
├── main.py           # Main application logic and CSV operations
├── data_entry.py     # Input validation and user input functions
├── FinanceData.csv   # CSV file storing all transactions (auto-generated)
└── README.md         # Project documentation
```

## 💡 Example Usage

```
1. Add Transaction.
2. View Transaction & summary within a date range.
3. Exit

What would you like to do ?: 1

Enter date of transaction (dd-mm-yyyy) or enter for todays date: 02-06-2025
Enter the amount: 5000
Enter the category
('I': Income,    'E': Expense): I
Enter a description(optional): Salary
Entry added successfully.
```

## 📊 Data Format

The application stores data in CSV format with the following columns:
- `date`: Transaction date (dd-mm-yyyy format)
- `amount`: Transaction amount (positive numbers)
- `category`: Income or Expense
- `description`: Optional transaction description

## 🛠️ Technical Details

### Classes and Methods

- **CSV Class**: Handles all CSV file operations
  - `initialize_csv()`: Creates CSV file if it doesn't exist
  - `add_entry()`: Adds new transactions to the CSV
  - `get_transactions()`: Retrieves and filters transactions by date range

### Input Validation

- **Date validation**: Ensures proper date format and handles default values
- **Amount validation**: Checks for positive numbers only
- **Category validation**: Restricts to Income ('I') or Expense ('E')

## 🔧 Dependencies

- `pandas`: For data manipulation and CSV operations
- `csv`: For writing CSV files
- `datetime`: For date handling and validation

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

## 📝 License

This project is open source and available under the MIT License.

## 🐛 Known Issues

- Currency symbol (₹) may not display properly on all terminals
- Large CSV files may take longer to process

## 🚀 Future Enhancements

- [ ] Add data visualization with charts and graphs
- [ ] Export reports to PDF format
- [ ] Add budget tracking and alerts
- [ ] Support for multiple currencies
- [ ] Web interface using Flask/Django
- [ ] Database integration (SQLite/PostgreSQL)

---

**Happy tracking! 💰**
