#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prompt user for two integers and return the quotient in 
multiple formats.

@author: jnwhisler
"""
num_one = int(input("Please enter an integer: "))
num_two = int(input("Please enter another integer: "))

print(f"The result of {num_one} divided by {num_two} is:")
print(f"{round(num_one / num_two, 2)} as a floating point value")
print(f"{num_one // num_two} remainder {num_one % num_two}")

