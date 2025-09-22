#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prompts user for length and height as decimals. Returns 
areas of square, rectangle, and triangle using those dimensions.

@author: jnwhisler
"""

length = float(input("Please enter the length as a"
                     " decimal (e.g., 4.0): "))
height = float(input("Please enter the height as a"
                     " decimal (e.g., 4.0): "))
print(f"You entered a length of {length} and a height of {height}.")
print("Here are your shapes:") 

square = round(length * 2, 2)                  
triangle = round(length * height * .5, 2)
rectangle = round(length * height, 2)
print(f"Square: {square}, Triangle: {triangle}, Rectangle: {rectangle}")


# Please enter the length as a decimal (e.g., 4.0): 4.0 
# Please enter the height as a decimal (e.g., 4.0): 2.0 
# You entered a length of 4.0 and a height of 2.0. 
# Here are your shapes:
# Square: 16.00 Rectangle: 8.00 Triangle: 4.00