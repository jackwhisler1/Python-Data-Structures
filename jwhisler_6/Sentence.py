"""
Jon Whisler

Class: CS 521 - Fall

Date: 10/8/2025

Homework Problem # 6

Description: Class library for Sentence that evaluates and manipulates an English sentence.
"""
import string
import random


class Sentence:
    """Represents an English sentence for basic evaluation and manipulation."""

    def __init__(self, sentence_str=''):
        """Initialize the sentence, remove punctuation, and store as a list."""
        words_list = sentence_str.strip(string.punctuation).split(' ')
        self.__sentence = words_list

    def __repr__(self):
        return "{}.".format(' '.join(self.__sentence))

    def get_all_words(self):
        """Returns a list of words from sentencee"""

        return self.__sentence

    def get_word(self, index):
        """Returns word at specified index or empty string if outside of range"""
        if 0 <= index < len(self.__sentence):
            return self.__sentence[index]
        return ''

    def set_word(self, index, new_word):
        """Changes the word at a given index location in sentence to a new word"""
        if index >= len(self.__sentence):
            # Append new word if index is beyond current list
            self.__sentence.append(new_word)
        else:
            self.__sentence[index] = new_word

    def scramble(self):
        """Returns a scrambled list of all the words in a sentence"""
        scrambled = self.__sentence[:]
        random.shuffle(scrambled)
        return scrambled


if __name__ == "__main__":
    s = Sentence("Here is a great, longer sentence worth testing.")

    s.set_word(2, "fun")
    assert s.get_word(2) == "fun", "set_word failed"

    scrambled = s.scramble()

    print("Sentence unit test successful")
    print("Original sentence:", s)
    print("Scrambled sentence:", scrambled)
    print("Final sentence:", s)
