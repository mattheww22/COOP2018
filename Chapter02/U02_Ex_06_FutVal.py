# U02_Ex_06_FutVal.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 19 Sep 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 6
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
# This program will calculate the future value of a bank account.
#
#
# Algorith (pseudocode)
#
#
#
#
def main():

    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    n = int(input("How many years are you tracking? "))

    for i in range(n):
        principal = principal * (1 + apr)

    print("The value in 10 years is ", principal)

main()
