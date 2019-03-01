# U05_Ex06_numerology.py
#
# Author: Matthew
# Course: Coding for OOP
# Section: A3
#     Date: 06 Dec 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 6
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#
#   This program prints the numeric value of a phrase given to it.
#
#
# Algorith (pseudocode)
#
#   Print intro
#   Get name from user
#   Send to func
#       Make the name lowercase
#       Split it on the spaces
#       Initialize the str of letters
#       Initialize the value
#       Loop through for as many letters in name
#           Parse through, finding the letter and looking how far into the aphabet it is
#           Add new value to previous value
#       Return value
#    Print value
#

def main():
    print("This program calculates the numeric value of your name.")
    name = input('What is your name? ')

    value = calcNumber(name)
    print(value)

def calcNumber(name):
    phr = name.lower()
    phr = phr.strip()
    phr = phr.split(" ")
    value = 0
    letter = "abcdefghijklmonpqrstuvwxyz"
    for char in phr:
        myPhr = myPhr[phr]
        letterValue = letter.index(char)
        value = value + letterValue
    return value

main()