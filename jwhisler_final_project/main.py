"""
Jon Whisler

Class: CS 521 - Fall

Description:
"""
import os
import csv
from datetime import datetime
import platform
import subprocess
from expense import Expense

CATEGORIES = (
    "Housing", "Transportation", "Food", "Utilities", "Clothing",
    "Medical", "Household items", "Personal",
    "Education", "Entertainment", "Other"
)


def validate_date(date_str):
    """Validates provided date string is proper date format and converts"""
    format = "%m-%d-%Y"
    try:
        datetime.strptime(date_str, format)
        return date_str
    except:
        raise ValueError("Date must be formatted as MM-DD-YYYY.")


def load_expenses(file_name):
    """Load expense sheet from CSV file if it exists"""
    if not os.path.exists(file_name):
        print(
            f"File '{file_name}' not found. Starting with empty expense list.")
        return []
    expenses = []
    try:
        with open(file_name, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(Expense(
                    expense_id=int(row["id"]),
                    date=row["date"],
                    category=row["category"],
                    description=row["description"],
                    amount=float(row["amount"])
                ))
    except Exception as e:
        print(f"Error loading file: {e}")
        return []
    return expenses


def save_expenses(file_name, expenses):
    """Save expenses to CSV"""
    if not file_name.lower().endswith('.csv'):
        file_name += '.csv'
    try:
        with open(file_name, "w", newline="") as file:
            fieldnames = ["id", "date", "category", "description", "amount"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for e in expenses:
                writer.writerow(e.to_dict())
        print(f"\nData saved to {file_name}")
        return file_name
    except Exception as e:
        print(f"Error saving file: {e}")
        return None


def open_file(file_name):
    """Open CSV file in default application"""
    try:
        system = platform.system()
        if system == "Windows":
            os.startfile(file_name)
        elif system == "Darwin":  # macOS
            subprocess.call(["open", file_name])
        else:  # Linux
            subprocess.call(["xdg-open", file_name])
        print(f"Opening {file_name} in default CSV viewer...")
    except Exception as e:
        print(f"Could not open file automatically: {e}")
        print(f"Please open {file_name} manually.")


def summarize_expenses(expenses):
    """Show summary statistics and top expense per category"""
    if not expenses:
        print("\nNo expenses to summarize.")
        return

    print("\n" + "="*60)
    print("EXPENSE SUMMARY")
    print("="*60)

    # Dictionary to store category summaries
    summary = {}

    # Set of unique categories
    unique_categories = {e.category for e in expenses}

    # Calculate totals per category
    category_totals = {}
    for cat in unique_categories:
        cat_expenses = [e for e in expenses if e.category == cat]
        category_totals[cat] = sum(e.amount for e in cat_expenses)
        summary[cat] = max(cat_expenses, key=lambda x: x.amount)

    # Overall statistics
    total_amount = sum(e.amount for e in expenses)
    print(f"\nTotal Expenses: ${total_amount:.2f}")
    print(f"Number of Expenses: {len(expenses)}")
    print(f"Average Expense: ${total_amount/len(expenses):.2f}")

    # Category breakdown
    print("\n" + "-"*60)
    print("SPENDING BY CATEGORY")
    print("-"*60)
    for cat in sorted(category_totals.keys()):
        print(f"{cat:.<25} ${category_totals[cat]:>10.2f}")

    # Highest expense per category
    print("\n" + "-"*60)
    print("HIGHEST EXPENSE PER CATEGORY")
    print("-"*60)
    for cat in sorted(summary.keys()):
        exp = summary[cat]
        print(f"{cat}: {exp.description} - ${exp.amount:.2f} ({exp.date})")

    print("="*60 + "\n")


def add_expense(expenses):
    """Prompt user for expense details and add to list

    Args:
        expenses (list): List of Expense objects to add to
    """
    while True:  # While iteration for adding multiple expenses
        print("\n" + "="*60)
        print("ADD NEW EXPENSE")
        print("="*60)
        print("Categories:")
        for i, c in enumerate(CATEGORIES):  # For iteration with tuple
            print(f"  {i + 1:2d}. {c}")
        print("\nType 'done' when finished adding expenses.")
        print("-"*60)

        # Get category with validation loop
        while True:
            category_num = input("Enter category number (1-11): ").strip()
            if category_num.lower() == "done":
                return  # Exit the entire function

            try:
                category_index = int(category_num) - 1
                if category_index not in range(len(CATEGORIES)):  # Conditional
                    print("❌ Invalid category number. Please enter 1-11.")
                    continue
                category = CATEGORIES[category_index]
                break  # Valid category, exit this loop
            except ValueError:
                print("❌ Please enter a valid number.")
                continue

        # Get and validate date with loop
        while True:
            date = input("Enter date (MM-DD-YYYY): ").strip()
            try:
                date = validate_date(date)
                break  # Valid date, exit this loop
            except ValueError as e:
                print(f"❌ {e}")
                continue

        # Get description with validation loop
        while True:
            desc = input("Enter description: ").strip()
            if not desc:  # Conditional
                print("❌ Description cannot be empty.")
                continue
            break  # Valid description, exit this loop

        # Get and validate amount with loop
        while True:
            amount = input("Enter amount: $").strip()
            try:
                amount = float(amount)
                if amount <= 0:  # Conditional
                    print("❌ Amount must be positive.")
                    continue
                break  # Valid amount, exit this loop
            except ValueError:
                print("❌ Amount must be a valid number.")
                continue

        # Create new expense with next available ID
        new_id = max([e.get_id() for e in expenses], default=0) + 1
        new_expense = Expense(new_id, date, category, desc, amount)
        expenses.append(new_expense)
        print(f"✓ Expense added successfully! (ID: {new_id})")
        print("\nAdd another expense or type 'done' at category prompt.")


def main():
    """Main program function"""
    print("\n" + "="*60)
    print("WELCOME TO EXPENSE TRACKER")
    print("="*60)

    # Loop until valid choice or quit
    while True:
        print("\nSelect an option:")
        print("  1. Add expenses to existing sheet")
        print("  2. Create new expense sheet")
        print("  3. View existing expenses only")
        print("  Type 'quit' to exit")
        print("-"*60)

        choice = input("Enter choice (1-3) or 'quit': ").strip().lower()

        # Check if user wants to quit
        if choice == 'quit' or choice == 'q':
            print("\nExiting Expense Tracker. Goodbye!")
            return

        # Validate menu choice
        if choice in ("1", "2", "3"):
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 'quit'.")

    filename = input("Enter expense file name: ").strip()

    # Ensure .csv extension
    if not filename.lower().endswith('.csv'):
        filename += '.csv'

    # Load or create expense list based on choice
    if choice == "1" or choice == "3":
        expenses = load_expenses(filename)
    else:
        expenses = []
        print("Starting new expense sheet.")

    # Add expenses if user chose options 1 or 2
    if choice in ("1", "2"):
        add_expense(expenses)

        # Save expenses
        saved_file = save_expenses(filename, expenses)

        # Show summary
        if expenses:
            summarize_expenses(expenses)

        # Open file if successfully saved
        if saved_file:
            open_choice = input(
                "\nWould you like to open the CSV file? (y/n): ").strip().lower()
            if open_choice == 'y':
                open_file(saved_file)

    elif choice == "3":  # View only
        summarize_expenses(expenses)

    print("\nThank you for using Expense Tracker!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
    else:
        print("Program completed successfully.")
