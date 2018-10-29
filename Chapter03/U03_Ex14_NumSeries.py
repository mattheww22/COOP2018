# U03_Ex14_NumSeries.py
#
# Author:
# Course: Coding for OOP
# Section: A3
#     Date: 25 Sep 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise:
#     Source: Python Programming
#    Chapter:
#
# Program Description

# THis program prints the average of a series of numbers
#
#
# Algorith (pseudocode)
#
# Ask user how many numbers there are
# average numbers
#
#

def main():

    print("This program prints the average of a series of numbers")
    n = eval(input("How many numbers are you averaging?"))
    a, b, c, d, e = eval(input("What are the numbers you want to average?"))
    sum = a + b + c + d + e
    average = sum / n
    print(average, "is your average")

main()