# U05_Ex03_Grades.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 30 Nov 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 03
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#
#   This program converts a number grade to a letter grade.
#
#
# Algorith (pseudocode)
#
#   Get input of number grade from user.
#   Convert the number to a letter grade
#   Print letter grade
#
def main():
    print("This program converts number grades to letter grades.")
    gradeStr = input('What is the number grade of your exam? ')

    myGrade = 'F' * 60 + 'D' * 10 + 'C' * 10 + 'B' * 10 + 'A' * 11

    myGrade = gradeStr

    print(myGrade, "is your letter grade.")


main()
