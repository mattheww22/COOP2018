# U05_Ex09_words.py
#
# Author: Matthew
# Course: Coding for OOP
# Section: A3
#     Date: 06 Dec 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 5
#     Source: Python Programming
#    Chapter: 9
#
# Program Description
#
#   This program calculates the number of words in a sentence entered by the user.
#
#
# Algorith (pseudocode)
#   Print intro
#   Get input of sentence from the user
#   Send sentence to func
#   Initialize value
#   Split sentence into words on the spaces
#   Loop through the words
#       Add 1 to value each time
#   Return value
#   Print value


def main():
    print('This program counts the number of words in a sentence.')
    words = input('Enter your sentence: ')
    value = calcWords(words)
    print("There are {0} words in your sentence.".format(value))

def calcWords(words):
    value = 0
    numWord = words.split(" ")
    for i in range(len(numWord)):
        value = value + 1
    return value
main()
