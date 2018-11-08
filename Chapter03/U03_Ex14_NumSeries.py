# U03_Ex14_NumSeries.py
#
# Author:
# Course: Coding for OOP
# Section: A3
#     Date: 25 Sep 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise:
#     Source: Python Programming
#    Chapter:
#
# Program Description

# THis program prints the average of a series of numbers
#
#
# Algorith (pseudocode)
#
# Ask user how many numbers there are
# average numbers
#
#


def main():
    print("This program prints the average of a series of numbers")
    n = int(input("How many numbers are you averaging?"))
    total = 0
    print()
    for i in range(n):
        num2 = int(input("Please enter another number to be averaged: "))
        total += num2
    avg = total / count
    print("The average of these numbes is, ", avg)


main()
