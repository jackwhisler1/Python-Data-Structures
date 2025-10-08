"""
Jon Whisler

Class: CS 521 - Fall

Date: 10/8/2025

Homework Problem # 6

Description: Class library for Sentence that evaluates and manipulates an English sentence.
"""
import string


class Sentence:
    """"""

    def __init__(self, sentence_str=''):
        """"""
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
            self.__sentence.append(new_word)
        else:
            self.__sentence[index] = new_word

    def scramble(self):
        """"""


s = Sentence("La la la testing out.")

print(s.get_all_words())
print(s.get_word(3))
print(s.get_word(5))
print(s.set_word(5, "newword"))
print(s.get_word(3))
print(s)
