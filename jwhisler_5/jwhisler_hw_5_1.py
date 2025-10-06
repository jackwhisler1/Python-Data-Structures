"""
Jon Whisler

Class: CS 521 - Fall

Date: 10/3/2025

Homework Problem # 5_1

Description: Requests 4 integers to use in calculation and prints results.
"""


def perform_calculation(a, b, c, d):
    """Performs (a+b) * c / d"""
    try:
        result = ((a + b) * c) / d
        print(f"Result of (({a} + {b}) * {c}) / {d} == {result:.2f}")
    except ZeroDivisionError:
        print("Cannot divide by zero.")


def request_integers():
    """Requests 4 integers to use for calculation."""
    nums = input("Please enter 4 non-zero integers separated by /: ")

    try:
        params = nums.split('/')
        params = [int(n) for n in params]
        perform_calculation(params[0], params[1], params[2], params[3])
    except Exception as e:
        print("Error: Please enter integer values.")
        request_integers()


if __name__ == '__main__':
    request_integers()
