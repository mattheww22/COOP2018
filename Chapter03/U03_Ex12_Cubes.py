# U03_Ex12_Cubes.py
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
        amount = amount ** 3

    print(amount, "is the sum of the cubes of these numbers.")


main()
