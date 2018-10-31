# U03_Ex09_Triangle.py
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
#   This program calculates the area of a triangle.
#
#
# Algorith (pseudocode)
#
#   Get inpup of a, b, c from user
#   Calculate area using a+ b+ c / 2
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
    A1 = s * s1 * s2 * s3
    A = A1 // 2

    print(A)


main()
