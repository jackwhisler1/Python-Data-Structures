#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prints numbers 1 through 30 and 'two' if multiple of two, 'three' if 
multiple of three, 'five' if multiple of five.

@author: jnwhisler
"""

MAXVAL = 30
i = 1

while i <= MAXVAL:
  is_mult_two = "two" if i % 2 == 0 else ""
  is_mult_three = "three" if i % 3 == 0 else ""
  is_mult_five = "five" if i % 5 == 0 else ""
  print(f"{i}. {is_mult_two}{is_mult_three}{is_mult_five}")
  i += 1

print("----------------------------")