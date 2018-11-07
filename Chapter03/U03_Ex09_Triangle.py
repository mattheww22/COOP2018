# U03_Ex09_Triangle.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 31 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 9
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
#
#   This program calculates the area of a triangle.
#
#
# Algorith (pseudocode)
#
#   Get input of lengths a, b, c from user
#   Calculate area using the lengths a + b + c / 2 A = s(s-a)(s - b)(s - c) // 2
#   print area
#

def main():
    print("This program calculates the area of a triangle")
    a, b, c = int(input("Please enter your 3 sides separated by commas:  "))
    var = a + b + c
    s = var / 2
    s1 = s - a
    s2 = s - b
    s3 = s - c
    A1 = s * s1
    A1 = A1 * s2
    A1 = A1 * s3
    A = A1 // 2

    print(A, "is the area of your triangle")


main()
