"""
Jon Whisler

Class: CS 521 - Fall

Date: 9/27/2025

Homework Problem # 4_4

Description: Asks a user for two long input strings. Returns the Jaccard Index for those strings.
"""


def get_long_string_input(prompt):
    while True:
        s = input(prompt)
        if len(s) >= 40:
            return s
        print("The entered string is too short, please try again.")


user_string_a = get_long_string_input(
    "Please enter a string that is at least 40 characters in length: ")
user_string_b = get_long_string_input(
    "Please enter a second string that is at least 40 characters in length:  ")

letters_a = [ch.lower() for ch in user_string_a if ch.isalpha()]
letters_b = [ch.lower() for ch in user_string_b if ch.isalpha()]

set_a = set(letters_a)
set_b = set(letters_b)

union_set = set_a.union(set_b)
intersection_set = set_a.intersection(set_b)

if len(union_set) == 0:
    jaccard_index = 0
else:
    jaccard_index = len(intersection_set) / len(union_set)

print(
    f"The Jaccard Index value for your two strings is {jaccard_index * 100:.2f}%")
