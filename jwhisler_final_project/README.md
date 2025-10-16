# Budget and Expense Tracker

**Author:** Jon Whisler  
**Course:** CS-521

## Overview

The Budget and Expense Tracker is a Python command-line application that helps users manage personal finances by recording, storing, and analyzing expenses. Users can track expenses across multiple categories, generate detailed summaries, and maintain persistent records through CSV files.

This project demonstrates practical application of Python programming concepts including object-oriented design, file I/O operations, data validation, error handling, and data structure manipulation.

## Features

- **Flexible Data Management**: Create new expense sheets or add to existing ones
- **Expense Categorization**: Track spending across 11 predefined categories
- **Data Persistence**: Save and load expense data from CSV files
- **Comprehensive Summaries**: View spending statistics, category breakdowns, and top expenses
- **Input Validation**: Robust validation for dates, amounts, and categories
- **Cross-Platform File Opening**: Automatically open CSV files in default applications
- **View-Only Mode**: Review existing expenses without making changes

## Categories

The application supports the following expense categories:

- Housing
- Transportation
- Food
- Utilities
- Clothing
- Medical
- Household items
- Personal
- Education
- Entertainment
- Other

## Requirements

- Python 3.x
- Standard library modules: `os`, `csv`, `datetime`, `platform`, `subprocess`

## File Structure

```
expense-tracker/
├── main.py    # Main application file
├── expense.py           # Expense class definition
└── *.csv               # Generated expense data files
```

## Installation

1. Clone or download the project files
2. Ensure both `main.py` and `expense.py` are in the same directory
3. No additional package installation required

## Usage

### Running the Application

```bash
python main.py
```

### Main Menu Options

1. **Add expenses to existing sheet**: Load a CSV file and append new expenses
2. **Create new expense sheet**: Start fresh with a new expense file
3. **View existing expenses only**: Display summary statistics without modification

### Adding an Expense

When adding expenses, you'll be prompted for:

- **Category**: Select from numbered list (1-11)
- **Date**: Enter in MM-DD-YYYY format
- **Description**: Brief text description
- **Amount**: Dollar amount (positive numbers only)

Type `done` at the category prompt when finished adding expenses.

### Example Session

```
WELCOME TO EXPENSE TRACKER
============================================================

Select an option:
  1. Add expenses to existing sheet
  2. Create new expense sheet
  3. View existing expenses only
  Type 'quit' to exit
------------------------------------------------------------
Enter choice (1-3) or 'quit': 2

Enter expense file name: monthly_expenses

Starting new expense sheet.

============================================================
ADD NEW EXPENSE
============================================================
Categories:
   1. Housing
   2. Transportation
   3. Food
   ...

Enter category number (1-11): 3
Enter date (MM-DD-YYYY): 10-15-2025
Enter description: Grocery shopping
Enter amount: $127.45
✓ Expense added successfully! (ID: 1)
```

## Expense Class

The `Expense` class provides a robust object-oriented representation of individual expenses with the following features:

### Attributes

- `expense_id` (private): Unique identifier
- `date`: Transaction date (MM-DD-YYYY)
- `category`: Expense category
- `description`: Transaction description
- `amount`: Dollar amount (validated)

### Methods

- `to_dict()`: Convert expense to dictionary format for CSV export
- `update_amount(new_amount)`: Update and validate expense amount
- `get_id()`: Access the private expense ID
- Magic methods: `__str__`, `__repr__`, `__lt__`, `__eq__` for enhanced functionality

### Key Features

- Private attribute encapsulation for ID protection
- Amount validation (positive numbers only)
- Rich comparison operators for sorting
- Dictionary conversion for data persistence

## Summary Report

After adding expenses, the application generates a comprehensive summary including:

- **Overall Statistics**: Total expenses, count, and average
- **Category Breakdown**: Total spending per category
- **Highest Expenses**: Largest expense in each category with details

Example output:

```
============================================================
EXPENSE SUMMARY
============================================================

Total Expenses: $1,247.89
Number of Expenses: 8
Average Expense: $155.99

------------------------------------------------------------
SPENDING BY CATEGORY
------------------------------------------------------------
Food.................... $    347.23
Housing................. $    650.00
Transportation.......... $    250.66

------------------------------------------------------------
HIGHEST EXPENSE PER CATEGORY
------------------------------------------------------------
Food: Grocery shopping - $127.45 (10-15-2025)
Housing: Monthly rent - $650.00 (10-01-2025)
Transportation: Gas - $89.50 (10-12-2025)
============================================================
```

## Error Handling

The application includes comprehensive error handling for:

- Invalid file operations
- Malformed date inputs
- Non-numeric or negative amounts
- Empty descriptions
- Out-of-range category selections
- Keyboard interrupts (Ctrl+C)

## Data Format

Expenses are stored in CSV format with the following structure:

```csv
id,date,category,description,amount
1,10-15-2025,Food,Grocery shopping,127.45
2,10-01-2025,Housing,Monthly rent,650.00
```

## Programming Concepts Demonstrated

- **Object-Oriented Programming**: Encapsulation, private attributes, magic methods
- **File I/O**: CSV reading/writing with error handling
- **Data Structures**: Lists, tuples, dictionaries, sets
- **Control Flow**: Loops (for, while), conditionals, exception handling
- **Validation**: Input sanitization and type checking
- **Date Processing**: String parsing and validation
- **Cross-Platform Compatibility**: OS-specific file opening

## Future Enhancements

Potential improvements for future versions:

- Budget setting and alerts
- Date range filtering
- Expense editing and deletion
- Data visualization (charts/graphs)
- Multiple file management
- Export to different formats
- Recurring expense tracking

## License

This project is created for educational purposes as part of CS-521 coursework.
