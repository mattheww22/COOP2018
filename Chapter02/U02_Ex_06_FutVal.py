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
#
#
#
# Algorith (pseudocode)
#   Print program description
#   Get principal, APR and periods from user
#   Repeat (10 * periods) times:
#       Calculate new principal (principal = principal * (1 + (apr/ periods)))
#   Output value of principal
#
#
#
def main():
    years = 10

    # Print program description
    print("This program will calculate APR with certain periods.")

    #   Get principal, APR and periods from user
    principal, apr, periods = eval(input("Enter the principal, APR (As a decimal), and periods (separated by commas): "))

    #   Repeat (10 * periods) times:
    for i in range(years * periods):
        #Calculate new principal(principal=principal * (1 + apr / periods))
        principal = principal * (1 + (apr / periods))

    #   Output value of principal
    print(principal)
main()