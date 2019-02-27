# U06_Ex_04_MacDonald.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 14 Dec 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 04
#     Source: Python Programming
#    Chapter: 06
#
# Program Description
#
#   This program returns the sum of the first "n" natural numbers and the first
#
# Algorith (pseudocode)
#
#   get "numbers" from the user
#   initialize n as 0
#   initialize cubed as 0
#   split numbers on space
#   add the numbers to n in a loop
#   get the cubes of all of the numbers
#   add the cubed numbers to "cubed"
#   print n and cubed
#

def main():
    print("This program calculates the sum of natural numbers imputed by a user.")

    n = int(input("How many natural numbers do you want to calculate? "))

    calc = sum(n)

    print("The sum of your natural numbers is {0}".format(calc))

    sumC = sumCubed(n)

    print("The sum of your natural numbers cubed is {0}".format(sumC))


def sum(n):
    sum = 0
    for num in range(n):
        sum = sum + (num + 1)
    return sum


def sumCubed(n):

    sumC = 0
    for num in range(n):
        sumC = sumC + (num + 1) ** 3
    return sumC


if __name__ == '__main__':
    main()
