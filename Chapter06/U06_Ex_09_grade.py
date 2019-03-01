# U06_Ex_09_grade.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 14 Dec 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 09
#     Source: Python Programming
#    Chapter: 06
#
# Program Description
#
#   This program converts a number grade provided by the user into a letter grade.
#
# Algorith (pseudocode)
#
#
#   Get input of number grade from user.
#   Send input to getLetter
#       Initialize the string of grade letters
#       Parse the string for the correct
#       Return letter grade
#   Print letter grade
#
#


def main():
    print("This program converts number grades to letter grades.")
    gradeStr = int(input('What is the number grade of your exam? '))
    Ltr = getLetter(gradeStr)
    print('Your letter grade for {0}% is {1}'.format(gradeStr, Ltr))

def getLetter(gradeStr):
    Ltr = 'F' * 60 + 'D' * 10 + 'C' * 10 + 'B' * 10 + 'A' * 11

    Ltr = Ltr[gradeStr]

    return Ltr


main()
