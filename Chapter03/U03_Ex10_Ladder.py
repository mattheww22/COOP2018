# U03_Ex10_Ladder.py
#
# Author:
# Course: Coding for OOP
# Section: A3
#     Date: 31 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise:
#     Source: Python Programming
#    Chapter:
#
# Program Description
#
#   This program finds the length of a ladder.
#
#
# Algorith (pseudocode)
#
#   Get length and deg from user
#   Convert deg to radians using pi/180* deg
#
#
#
#
from math import pi

def main():

    print("This program finds the length of a ladder.")
    L, Deg = int(input("Enter your length and degrees of your ladder (Separated by commas): "))
    radians = pi / 180 * Deg
    height = L * radians
    print("Your ladder is ", height, "tall")
main()