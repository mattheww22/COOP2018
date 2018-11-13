# U04_Ex_05_Dice.py
#
# Author:
# Course: Coding for OOP
# Section: A3
#     Date: 01 Nov 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise:
#     Source: Python Programming
#    Chapter:
#
# Program Description
#
#   Draws a dice row showing a straight
#
#
# Algorith (pseudocode)
#
#   Create a graphWin
#   set window coordinates for entry
#   get inputs
#   draw coordinate plane
#
#

from graphics import *


def main():
    win = GraphWin(1470, 270)

    win.setCoords(0, 0, 49, 9)
    win.setBackground("black")

def makeRect(p1, p2):
    rect = Rectangle(p1, p2)
    rect.setFill("Forest Green")
    rect.setOutline("Black")
    return rect

def makeDot():
    rect = Rectangle(p1, p2)
    rect.setFill("black")
    rect.setOutline("black")
    return rect


def dice1():
    die = makeRect (Point(1, 1), Point(8, 8))
    die.setOutline("black")
    die.setFill("white")


main()
