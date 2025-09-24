"""
Jon Whisler

Class: CS 521 - Fall 

Date: 9/18/2025

Homework Problem # 3_4

Description: Returns longest word in given text file.
"""
import sys, string
FILENAME = 'cs521_assign_3_4.txt'
try:
  with open(FILENAME, 'r') as file:
    text = file.read()
    words = text.split()
    # Strips each word of punctuation
    clean_words = [word.strip(string.punctuation).lower() for word in words]
    # Removes words that contain non alpha characters 
    alpha_words = [word for word in clean_words if word.isalpha()]

    if alpha_words:
      max_len = max(len(word) for word in alpha_words)
      # Return all words with max length
      longest_words = list({word for word in alpha_words if len(word) == max_len})
except Exception as e:
  print(f'Failure to find file, {e}')

if len(longest_words) == 1:
  print(f"The longest word in {FILENAME} is {longest_words[0]} at {max_len} letters.")
elif len(longest_words) > 1:
  print(f"The longest words in {FILENAME} are {', '.join(longest_words)} at {max_len} letters.")
