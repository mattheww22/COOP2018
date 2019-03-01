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
#   This program prints the numeric value of
#
#
# Algorith (pseudocode)
#
#   Get input of name
#   Change the name into a list of letters
#   Translate the list of letters into unicode -27
#   print total of name

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