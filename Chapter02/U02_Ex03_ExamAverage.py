# U02_Ex03_ExamAverage.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 05 Sep 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 5
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
#   This program will average out exam scores.
#
#
# Algorith (pseudocode)
#
#   Explain program
#   Get 3 exam scores from user
#   Calculate average (a + b + c / 3)
#   Print average
#

def main():
    #   Explain program
    print("This program will average your exam scores")

    #   Get 3 exam scores from user
    a,  b,  c = eval(input("Enter your three exam scores separated by commas: "))

    #   Calculate average (a + b + c / 3)
    sum = a + b + c
    average = sum / 3

    #   Print average
    print(average, "is your exam average.")
main()
