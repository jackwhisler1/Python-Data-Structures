"""
Jon Whisler

Class: CS 521 - Fall

Date: 10/3/2025

Homework Problem # 5_5

Description: Returns GCD from provided integers
"""


def greatest_common_divisor(a, b):
    """Returns greatest common divisor for given input of integers"""
    if a % b == 0:
        return b
    else:
        return greatest_common_divisor(b, (a % b))


def get_non_zero_integer(prompt):
    """Requests a non-zero integer from user"""
    while True:
        value = input(prompt)
        try:
            value = int(value)
            if value == 0:
                print("You may not use zero in this calculation.")
            else:
                return value
        except ValueError:
            print("That is not an integer value.")


if __name__ == '__main__':
    a = get_non_zero_integer("Enter first non-zero integer value: ")
    b = get_non_zero_integer("Enter second non-zero integer value: ")
    result = greatest_common_divisor(a, b)
    print(f"The GCD of {a} and {b} is {result}")
