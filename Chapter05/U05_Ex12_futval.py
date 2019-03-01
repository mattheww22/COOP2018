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
#   This program makes a chart of all of the future values of a bank account with compound intrest.
#
#
# Algorith (pseudocode)
#
#   Print introduction
#   Get the initial value of the account, apr, and years from user
#   Print heading
#   Loop through however many years user is tracking
#       principal = principal * (1 + apr)
#       Print results with year first, then principal
#
def main():

    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annual interest rate: "))
    years = int(input("How many years are you tracking? "))

    print('Year\t Value')

    print("-------------")
    for i in range(years):

        principal = principal * (1 + apr)

        print('   {0}\t  ${1}'.format(i+1, principal / 10))

main()
