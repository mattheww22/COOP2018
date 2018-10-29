# U02_Ex08_APRCompound.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 19 Sep 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 8
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
#
#
#
#
# Algorith (pseudocode)
#
#
#
#
#
def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter principal here: "))
    apr = eval(input("Enter the annual intrest rate:"))

    for i in range(10):
        principal = principal * (1 + apr)

    print("The value in 10 years is:", principal)

main()