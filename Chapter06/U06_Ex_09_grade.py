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
#   This program gets a number grade from the user and returns a letter grade.
#
# Algorith (pseudocode)
#
#
#   Get input of number grade from user.
#   Send input to getLetter
#       Convert the number to a letter grade
#       Print letter grade
#
#


def main():

    print("This program converts number grades to letter grades.")
    gradeStr = int(input('What is the number grade of your exam? '))
    getLetter(gradeStr)


def getLetter(gradeStr):
    myGrade = 'F' * 60 + 'D' * 10 + 'C' * 10 + 'B' * 10 + 'A' * 11

    myGrade = myGrade[gradeStr]

    print('Your letter grade is {}'.format(myGrade))


main()
