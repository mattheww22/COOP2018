# U04_Ex_07_Circle.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 01 Nov 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 7
#     Source: Python Programming
#    Chapter: 4
#
# Program Description
#
#   This program displays the information of a circle intersection.
#
#
# Algorith (pseudocode)
#
#   Print program description
#   Get radius of circle and y intercept from user
#   Print circle and line onto coordinate plane
#
#
#
from graphics import *
from math import sqrt


def main():
    win = GraphWin("Circle Intersection", 600, 600)

    win.setCoords(-10, -10, 10, 10)

    Intro = Text(Point(5, 9), "This program computes and plots the intersection of a circle and line.")
    Intro.setStyle("bold")
    Intro.draw(win)

    Radius = Text(Point(4, 6), "Radius of a circle (≤ 10): ")
    Radius.draw(win)

    inputRadius = Entry(Point(8, 6), 10)
    inputRadius.setText("0.0")
    inputRadius.draw(win)

    Intercept = Text(Point(3, 4), "y-intercept of an horizontal line (-10 ≤ y ≤ 10): ")
    Intercept.draw(win)

    inputIntercept = Entry(Point(8, 4), 10)
    inputIntercept.setText("0.0")
    inputIntercept.draw(win)

    button = Rectangle(Point(4, 0.5), Point(6, 1.5))
    button.setFill("black")
    button.draw(win)
    buttonText = Text(Point(5, 1), "Continue")
    buttonText.draw(win)
    win.getMouse()

    radius = float(inputRadius.getText())
    intercept = float(inputIntercept.getText())

    Intro.undraw()
    Radius.undraw()
    Intercept.undraw()
    inputRadius.undraw()
    inputIntercept.undraw()
    button.undraw()
    buttonText.undraw()

    win.setCoords(-11, -11, 11, 12)

    drawAxes(win, -10, -10, 10, 10, "Intersection Between Circle and the Line")

    circle = Circle(Point(0, 0), radius)
    circle.setOutline("blue")
    circle.draw(win)

    line = Line(Point(-10, intercept), Point(10, intercept))
    line.setOutline("blue")
    line.draw(win)

    x2 = sqrt(radius ** 2 - intercept ** 2)
    if x2 > 0:
        x1 = x2 * -1
    else:
        x1 = None

    negIntercept = 1
    if intercept < 0:
        negIntercept = -1
    count = 0
    xCoord = x1
    while count < 2:
        p1 = Circle(Point(xCoord, intercept), 0.2)
        p1.setOutline("red")
        p1.setFill("red")
        p1.draw(win)
        Text(Point(copysign(abs(xCoord) + 1, xCoord), (abs(intercept) + 1) * negIntercept),
             "x".format(xCoord)).draw(win)
        if type(x2) == None:
            break
        count += 1
        xCoord = x2

    win.getMouse()


def drawAxes(win, minX, minY, maxX, maxY, title):
    Line(Point(minX, 0), Point(maxX, 0)).draw(win)
    Line(Point(0, minY), Point(0, maxY)).draw(win)
    for i in range(minX, maxX + 1, 2):
        if i != 0:
            Line(Point(i, 0.1), Point(i, -0.1)).draw(win)
            Text(Point(i, -0.5), i).draw(win)
            Line(Point(-0.1, i), Point(0.1, i)).draw(win)
            Text(Point(-0.5, i), i).draw(win)

    titleText = Text(Point(0, maxY + 1), title)
    titleText.setSize(18)
    titleText.setStyle("bold")
    titleText.draw(win)

    main()
