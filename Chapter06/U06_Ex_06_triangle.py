# U06_Ex_06_triangle.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 14 Dec 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 06
#     Source: Python Programming
#    Chapter: 06
#
# Program Description
#
#   This function computes the area of a triangle when given three sides.
#
# Algorith (pseudocode)
#
#   Print intro
#   Get three sides from user
#   Send side lengths to func
#       Compute area using 1/2 a+b+c
#   print area
#

def main():
    print("This function computes the area of a triangle when given three sides.")
    a = int(input("What is the first side length of your triangle? "))
    b = int(input("What is the second side length of your triangle? "))
    c = int(input("What is the third side length of your triangle? "))
    area = getArea(a, b, c)
    print("The area of your triangle is {0}.".format(area))


def getArea(a, b, c):
    area = a + b
    area = area + c
    area = area / 2
    return area


if __name__ == '__main__':
    main()
