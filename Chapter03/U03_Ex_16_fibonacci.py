# U03_Ex_16_fibonacci.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 29 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 16
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
#
# This program computes the number of fibonacci numbers defined by a user.
#
# Algorith (pseudocode)
#
#   print program description
#   Get input of number of sequences
#   if terms is 1 print 1
#   if terms = 2 print 1 1
#   if else, compute other terms, print as you go
#

def main():
    print("This program prints the fibonacci sequence.")
    n = int(input("How many numbers do you want? "))
    a = 1
    b = 1

    if n == 1:
        print("1")

    elif n == 2:
        print("1 1")

    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c


main()
