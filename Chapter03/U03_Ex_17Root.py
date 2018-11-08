# U03_Ex_17Root.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 29 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 17
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
#
# This program calculates the square root of a number.
#
#
# Algorith (pseudocode)
#
# get number that you want to square root.
# calculate using the formula ()
# print square root
#

from math import sqrt

def main():
    print("This program calculates the square root of a number")

    num = float(input("Enter the number for which you wish to calculate the square root: " ))

    guesses = int(input("How many guesses do you want to use in the calculation? "))

    guess = num / 2

    for i in range(guesses):

        guess = (guess + num / guess) / 2

    print(guess, "is the guess vs", sqrt(num), " Real square root")

main()
