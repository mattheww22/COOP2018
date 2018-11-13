# U04_Ex_02_Target.py
#
# Author: Matthew
# Course: Coding for OOP
# Section: A3
#     Date: 25 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 2
#     Source: Python Programming
#    Chapter: 4
#
# Program Description
#
#   Draws an archery target with circles that are half of the previous one
#
#
# Algorith (pseudocode)
#   Import graphics library
#   Create a GraphWin
#   Draw 5 concentric circles (yellow, red, blue, black, white)
#       each outer ring has a radius greater than the previous in increments equal to the center circle's radius
#   Draw circles from outside in
#
#
from graphics import *


def main(winSide):
    win = GraphWin("Target", winSide, winSide)
    radius = win.getWidth() / 12
    center = Point(win.getWidth() / 2, win.getHeight() / 2)
    circles = makeCircle(center, radius * 5, "white"),
    makeCircle(center, radius * 4, "black"),
    makeCircle(center, radius * 3, "blue"),
    makeCircle(center, radius * 2, "red"),
    for circle in circles:
        circle.draw(win)


def makeCircle(c, r, color):
    """
    Make a circle object that is centered with c and r w/ color
    :param c: Point -> center of circle
    :param r: int -> radius of circle
    :param color: str -> color name for fill
    :return: Circle -> circle object
    """

    circ = Circle(c, r)
    circ.setOutline("black")
    circ.setFill(color)
    return circ


input("Press <Enter> to close graphics window")

main(600)
