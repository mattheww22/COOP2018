# U03_Ex07_Distance.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 25 Sep 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 7
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
# This program prints the distance formula.
#
#
#
# Algorith (pseudocode)
#
#   get points from user
#   calculate distance using x2-x1**2 + y2-y1**2
#   print distance
#

def main():

    print("This program computes distance between two points.")
    a, b, c, d = eval(input("What are your points?"))
    y = d - b ** 2
    x = c - a ** 2
    distance = x + y
    print(distance, " is your distance")


main()