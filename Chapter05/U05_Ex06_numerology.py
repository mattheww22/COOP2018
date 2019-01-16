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
    name = input('What is your name?')

    name = name.lower()

    number = 0
    a = 97
    z = 123

    length = name.lenth

    for char in name:
        alpha = ord(char)
        if alpha >= a and alpha <= z:


        Num += (alpha - 96)

    print('The numeric value of {0} is: {1} '.format(name, Num))
