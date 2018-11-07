# U03_Ex06_Slope.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 25 Sep 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 6
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
# This program finds the slope of a line.
#
#
#
# Algorith (pseudocode)
#
# Print program description
# Get four points in the separated by commas
# add up a + c and b + d then divide them
# Print slope and the original points
#

def main():

    print("This program finds the slope of a line.")
    x1, y1, x2, y2 = eval(input("Please enter your coordinates (x1, y1, x2, y2) "))
    x = x2 - x1
    y = y2 - y1

    slope = y / x

    print(slope, " is the slope of ", x1, y1, x2, y2)

main()
