#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prompts user for two whole numbers and prints the product
 as a binary, octal, decimal, and hexadecimal value
 
@author: jnwhisler
"""

num_one = int(input("Please enter an integer: "))
num_two = int(input("Please enter a second integer: "))

product = num_one * num_two
print(f"You entered {num_one} and {num_two}."
      f" The product of these two numbers is {product}.")

print("Here is that product printed in more formats: ")
print(f"Binary: {bin(product)}")
print(f"Octal: {oct(product)}")
print(f"Decimal: {int(product)}")
print(f"Hexadecimal: {hex(product)}")
