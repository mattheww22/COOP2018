# U05_Ex15_Scores.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 17 Dec 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 15
#     Source: Python Programming
#    Chapter: 05
#
# Program Description
#
#   This program prints a graphical chart of student scores received from a file
#
# Algorith (pseudocode)
#
#   Import Graphics
#   Print introduction
#   Loop through reading a line of the file
#       Print chart with name and score from 0 - 100
#       Print the name of the student
#       Make the bar chart using createBar
#           Take the number grade and make it into a chart through 100
#
from graphics import *


def main():
    win = GraphWin(4000, 4000)
    win.setCoords(0, 0, 120, 120)

    scores = open("U05_Ex15_ExamScores.txt", "r")
    scores.readlines()
    scores.close()
    for line in scores:
        grade(line)


def grade(line):
    name, grade = line.split()

    name = [Text(Point(10, 110), name)]
    grade = grade + 100
    makeBar(grade, name)


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
    rect = Rectangle(x, 50, x + 10, num)
    rect.draw(win)
    nameprompt = Text(Point(x, 35), name)
    nameprompt.draw(win)

    win.getMouse()
    win.close()


main()
