# U05_Ex16_histogram.py
#
# Author: Matthew
# Course: Coding for OOP
# Section: A3
#     Date: 17 Dec 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 16
#     Source: Python Programming
#    Chapter: 05
#
# Program Description
#
#   This program prints a histogram of the amount of students that got the same score
#
#
# Algorith (pseudocode)
#
#   Import graphics
#   Print introduction
#   Get file name from the user
#   Open specified file
#   Readlines of file
#   Close file
#   Loop for each line
#       split the name and number apart
#       Send to the makeBar function
#
#

from graphics import *


def main():
    win = GraphWin()
    win.setCoords(0, 0, 400, 200)
    fname = input("Enter filename: ")
    infile = open(fname, 'r')
    infile.readlines()
    infile.close()
    x = 0

    for line in infile:
        name, num = line.split()
        makeBar(name, num, x, win)


def makeBar(name, num, x, win):
    """
    keep y axis for bottom of rectangles as 50
    Add 20 on x axis from last bar
    Print name underneath bar
    Create bar by using the num + 50 as height

    :param name: Name of the person with the grade
    :param num: Grade number
    """
    x = x + 20
    rect = Rectangle(Point(x, 50), (x + 10, num))
    rect.draw(win)
    nameprompt = Text(Point(x, 35), name)
    nameprompt.draw(win)

    win.getMouse()
    win.close()


main()
