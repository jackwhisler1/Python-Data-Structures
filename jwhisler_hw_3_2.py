"""
Jon Whisler

Class: CS 521 - Fall 

Date: 9/18/2025

Homework Problem # 3_2

Description: Shifts each alpha letter of a string a set number of characters 
forward in the alphabet. Maintains case.
"""
import string

SHIFT = 6
MESSAGE = "The Quick, brown fox jumped over the lazy dog."
shifted_message = ""

for l in MESSAGE:
    if l in string.ascii_lowercase:
        shifted_index = (string.ascii_lowercase.index(l) + SHIFT) % 26
        shifted_message += string.ascii_lowercase[shifted_index]
    elif l in string.ascii_uppercase:
        shifted_index = (string.ascii_uppercase.index(l) + SHIFT) % 26      
        shifted_message += string.ascii_uppercase[shifted_index]   
    else:
        shifted_message += l
        
print(shifted_message)
