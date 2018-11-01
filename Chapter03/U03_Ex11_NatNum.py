# U03_Ex11_NatNum.py
#
# Author: Matthew
# Course: Coding for OOP
# Section: A3
#     Date: 31 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 11
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
#
#   This program prints all of the natural numbers to 100
#
#
# Algorith (pseudocode)
#
# Print the natural numbers
#
#
#

def main():
    n = int(input("How many natural numbers do you want?"))

    amount = 0

    for i in range(n):
        amount = amount + 1

        print(amount)


main()
