"""
Jon Whisler

Class: CS 521 - Fall

Date: 10/3/2025

Homework Problem # 5_3

Description: Calculates and prints straight line depreciation schedule
"""


def calc_depreciation(term, initial_val, salvage_val):
    """Calculate annual depreciation and return float"""
    return (initial_val - salvage_val) / term


def depreciation_generator(initial_val, salvage_val, annual_depreciation):
    """Yields teh yearly depcreciated value of asset"""
    current_val = initial_val
    for _ in range(term + 1):
        yield current_val
        current_val -= annual_depreciation


def format_int(value_str):
    """Converts string to integer"""
    if value_str.isdigit() or (value_str.startswith('-') and value_str[1].isdigit()):
        return int(value_str)
    raise ValueError


def get_valid_int(prompt):
    """Ask user for input until valid integer"""
    while True:
        value = input(prompt)
        try:
            return format_int(value)
        except ValueError:
            print("That's not an integer.")


if __name__ == '__main__':
    initial_value = get_valid_int(
        "Enter the initial integer value of the item: ")
    term = get_valid_int("Enter the term in years as an integer: ")
    salvage_value = get_valid_int(
        "Enter the integer salvage value of the item: ")

    annual_depreciation = calc_depreciation(term, initial_value, salvage_value)

    print(f"Depreciation schedule for ${initial_value} over {term} years:")

    for year, value in enumerate(depreciation_generator(initial_value, salvage_value, annual_depreciation)):
        print(f"Year {year}: | {value:.2f}|")
