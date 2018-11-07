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
#   calculate distance using x2-x1**2 + y2-y1**2 // 2
#   print distance
#

def main():

    print("This program computes distance between two points on a graph.")
    x1, y1, x2, y2 = eval(input("What are your points?"))
    y = y2 - y1 ** 2
    x = x2 - x1 ** 2
    distance = x + y
    distance = distance // 2
    print(distance, " is your distance")


main()