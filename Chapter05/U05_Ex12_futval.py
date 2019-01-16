# U05_Ex12_futval.py
#
#
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 06 Dec 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 12
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#
#   This program makes a chart of all of the future values
#
#
# Algorith (pseudocode)
#
#   Calculate fut value
#   print year then value
#   Repeat
#
def main():


    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = int(input("How many years are you tracking? "))

    print('Year\t Value')

    print("-------------")

    for year in range(years):
        principal = principal * (1 + apr)

    print('{0}\t${1:.2}'.format(year+1, principal))

main()
