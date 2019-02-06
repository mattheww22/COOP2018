# U06_Ex_04_MacDonald.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 14 Dec 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 04
#     Source: Python Programming
#    Chapter: 06
#
# Program Description
#
#   This program prints the surface area and volume of at sphere using a given radius
#
# Algorith (pseudocode)
#
#
#
#
#
def main():
    print("This program makes an acronym out of any string of words you want")

    phrases = input("What are the words you want to be turned into acronyms? ")
    phrase = phrases.split()
    ac = acronym(phrase)
    print(ac, "is the acronym for {0}".format(phrases))

def acronym(phrase):
    ac = ''

    for word in phrase:

        ac += word[0].upper()

    return ac


main()
