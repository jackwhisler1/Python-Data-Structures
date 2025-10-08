"""
Jon Whisler

Class: CS 521 - Fall

Date: 10/8/2025

Homework Problem # 6

Description: Class library for Sentence that evaluates and manipulates an English sentence.
"""

class Sentence:
  def __init__(self, sentence_str):
    self.sentence = sentence_str

  def __str__(self):
    return 'Your sentence: {}'.format(self.sentence.upper())


s = Sentence("La la la testing out.")
print(s)