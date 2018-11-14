# U04_Ex_10_Triangle.py
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
#   This program prints the perimeter of a triangle based on 3 points specified by clicks
#
#
# Algorith (pseudocode)
#
#   Print introduction
#   Get click 1
#   Get click 2
#   Get click 3
#   Calculate perimeter using s(s - a)(s - b)(s - c) // 2
#   Print perimeter

from graphics import *
from math import sqrt

def main():

    win = GraphWin("Line Segment Info", 600, 600)

    win.setCoords(-11, -11, 11, 12)

    messages = [Text(Point(0, 11), "This program draws a triangle between three mouse clicks."),
                Text(Point(0, 8), "On the following page, click once for each of the,"),
                Text(Point(0, 7), "vertices of a triangle."),
                Text(Point(0, 5), "The triangle will be drawn and information will be displayed."),
                Text(Point(0, 3), "Click Continue when ready to begin.")]
    for msg in messages:
        msg.setSize(16)
        msg.draw(win)
    button = Rectangle(Point(4, 0.5), Point(6, 1.5))
    button.setFill('black')
    button.draw(win)
    buttonText = Text(Point(5, 1), "Continue")
    buttonText.draw(win)

    win.getMouse()
    for msg in messages:
        msg.undraw()
    buttonText.undraw()
    button.undraw()

    drawAxes(win, -10, -10, 10, 10, "Triangle Info")

    p1 = getMouseClick(win, Point(5, -10), "Click for 1st point", )

    p2 = getMouseClick(win, Point(5, -10), "Click for 2nd point", )

    p3 = getMouseClick(win, Point(5, -10), "Click for 3rd point", )

    Polygon(p1, p2, p3).draw(win)

    pXs = [p1.getX(), p2.getX(), p3.getX()]
    pYs = [p1.getY(), p2.getY(), p3.getY()]
    perimeter = 0
    side = 0
    s = 0
    sides = [0]
    for i in range(3):
        dx = pXs[i] - pXs[(i + 1) % 3]
        dy = pYs[i] - pYs[(i + 1) % 3]
        side = sqrt(dx ** 2 + dy ** 2)
        s += side / 2
        sides.append(side)
        perimeter += side
    area = 1
    for side in sides:
        area *= sqrt(s - side)
    Text(Point(-5, -10), "Area".format(area)).draw(win)
    Text(Point(5, -10), "Perimeter".format(perimeter)).draw(win)

    win.getMouse()


main()
