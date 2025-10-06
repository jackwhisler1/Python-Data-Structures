"""
Jon Whisler

Class: CS 521 - Fall

Date: 10/5/2025

Homework Problem # 5_2

Description: Takes input for a file, function will count the words in the supplied list that occur exactly the specified number of times.
"""
import re
from collections import Counter


def get_words_from_file():
    """ Takes an input of a filename to convert into a list of formatted strings """
    try:
        file = input("Please enter the name of a file: ")

        with open(file) as f:
            file_contents = f.read()
            file_contents = file_contents.lower()
            file_words = re.findall(r'\b\w+\b', file_contents)
            return file_words

    except Exception as e:
        print(e)
        print('No file of that name could be found. Please try again.')
        get_words_from_file()


def repeated_words(repetitions, words):
    """ Takes in a number of occurrences to look for and a list of words to search. """
    word_counts = Counter(words)
    matching_words = [word for word,
                      count in word_counts.items() if count == repetitions]

    if matching_words:
        print(f"\nWords that appear exactly {repetitions} times:")
        print(sorted(matching_words))
    else:
        print(f"\nNo words found that appear exactly {repetitions} times.")

    return matching_words


if __name__ == '__main__':
    words = get_words_from_file()
    for num in range(2, 6):
        result = repeated_words(num, words)
