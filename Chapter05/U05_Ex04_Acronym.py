# U05_Ex04_Acronym.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 30 Nov 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 04
#     Source: Python Programming
#    Chapter: 05
#
# Program Description
#
#   This program creates an acronym out of a string of words given by the user.
#
#
# Algorith (pseudocode)
#
#   Print intro
#   Get phrase from the user
#   Create list of words by splitting on space
#   Send to func
#       Get the first letter of every word and capitalize it
#       Return Acronym
#   Print Acronym and initial phrase
#

def main():
    print("This program makes an acronym out of any string of words you want")

    phrase = input("What are the words you want to be turned into acronyms? ")

    words = phrase.split(" ")
    acronym = Acronym(words)

    print("{0} is the acronym for {1}".format(acronym, phrase))

def Acronym(words):
    acronym = ''
    for word in words:

        acronym += word[0].upper()

    return acronym

main()
