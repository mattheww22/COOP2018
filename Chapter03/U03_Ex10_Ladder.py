# U03_Ex10_Ladder.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 31 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 10
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
#
#   This program finds the length of a ladder using the angle and the height.
#
#
# Algorith (pseudocode)
#
#   Get length and deg from user
#   Convert deg to radians using pi/180* deg
#   Find the height using the formula (length * radians)
#   Print the height in inches
#
#

from math import *

def main():
    print("This program finds the length of a ladder.")
    L, Deg = int(input("Enter your length and degrees of your ladder (Separated by commas): "))
    Height = L * degrees()
    print("Your ladder is ", Height, "inches tall")


main()
