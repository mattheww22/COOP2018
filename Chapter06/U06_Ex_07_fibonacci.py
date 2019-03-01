# U06_Ex_07_fibonacci.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 06 Feb 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 07
#     Source: Python Programming
#    Chapter: 6
#
# Program Description
#
#   This program computes the "n"th fibonacci number that is specified by the user.
#
# Algorith (pseudocode)
#
#   Print program description
#   Get the nth fibonacci number from the user
#   Send n to func
#       If n is 1 or 2
#           output = 1
#       Initialize variables
#       Loop through for however big n is
#           Add a and b together to get c
#           Move all variables so c is still total and b can be added to next number
#           Continue to add a and b together
#       Return c
#   Print nth fibonacci number
#

def main():
    print("This program prints the fibonacci sequence.")
    n = int(input("Which fibonacci number do you want? "))
    c = fibonacci(n)

    print(c, end=" ")


def fibonacci(n):
    a = 1
    b = 1

    if n == 1 or 2:
        c = 1

    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return c


main()
