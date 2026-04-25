# Expense Tracker

Expense Tracker is a beginner-friendly command-line Python program that allows users to manage simple expenses.

The program gives the user five options:

1. Display all expenses
2. Add a new expense
3. Remove an expense
4. Display the total cost
5. Save and exit

## How It Works

When the program starts, it loads existing expense data from a JSON file. If no previous data exists, the program starts with an empty list of expenses.

Each expense is stored as a dictionary with two pieces of information:

- the name of the expense
- the amount of the expense

All expenses are stored together in a list, and the list is saved into a JSON file.

Example structure:

```json
[
  {
    "name": "gas",
    "amount": 34.56
  }
]
```
