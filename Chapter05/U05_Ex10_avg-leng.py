# U05_Ex10_avg-leng.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 06 Dec 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 10
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#
#   This program prints the average length of a word in a sentence.
#
#
# Algorith (pseudocode)
#
#   Get input of sentence
#   get the length of each word
#   average the lengths
#
#
#
def main():
    AvgWrdLth = 0

    print('This program averages the words lengths of a sentence.')
    sentence = input('Type the words you want to average: ')
    words = sentence.split()
    ttlLen = 0
    for word in words:
        word = strip(word)
        ttlLen += len(word)
        AvgWrdLth = ttlLen / len(words)

    print('There were {0} words in that phrase.'.format(AvgWrdLth))

def strip(word):

    stripped = ''

    for char in word.lower():
        if char >= 'a' and char <= 'z':
            stripped += char
    return stripped