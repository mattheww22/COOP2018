# U05_Ex04_Acronym.py
#
# Author:
# Course: Coding for OOP
# Section: A3
#     Date: 30 Nov 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise:
#     Source: Python Programming
#    Chapter:
#
# Program Description
#
#   This program makes an acronym out of any string of words you want
#
#
# Algorith (pseudocode)
#
#   Get string inputs from user
#   Get the first letter of every word
#   print all acronym letters capitalized in a string
#

def main():
    print("This program makes an acronym out of any string of words you want")

    acroStr = input("What are the words you want to be turned into acronyms? ")

    words = acroStr.split(' ')
    acronym = ' '

    for word in words:
        acronym += word[0].upper
        print(acronym, "is the acronym for ", acroStr)


main()
