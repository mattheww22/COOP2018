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
#   Print introduction
#   Get input of number grade from user.
#   Create string of all grades
#   Parse the string and find the correct letter corresponding to the number
#   Print letter grade
#
def main():
    print("This program converts number grades to letter grades.")
    gradeStr = int(input('What is the number grade of your exam? '))

    myGrade = 'F' * 60 + 'D' * 10 + 'C' * 10 + 'B' * 10 + 'A' * 11

    myGrade = myGrade[gradeStr]

    print('Your letter grade is {}'.format(myGrade))


main()
