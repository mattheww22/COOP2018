# U04_Ex_11_House.py
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
#   This program draws a house to the users specifications with their clicks
#
#
# Algorith (pseudocode)
#
#   Print intro
#   create graphWin
#
#



from graphics import *
from math import sqrt

def main():

    win = GraphWin("Five-Click House", 600, 600)

    win.setCoords(-11, -11, 11, 12)

    messages = [Text(Point(0, 11), "This program draws a house using five mouse clicks."),
                Text(Point(0, 8), "On the following page, click 5 times, according"),
                Text(Point(0, 7), "to the guide and image below. "),
                Text(Point(0, 4), "• Clicks 1 & 2 define rectangle for house frame\n" +
                                  "• Click 3 is center of door frame                         \n" +
                                  "• Click 4 is for the window                                  \n" +
                                  "• Click 5 is for peak of roof                                  "),
                Text(Point(0, 1), "Click Continue when ready to begin.")]
    for msg in messages:
        msg.setSize(16)
        msg.draw(win)
    button = Rectangle(Point(4, -2.5), Point(6, -1.5))
    button.setFill('black')
    button.draw(win)
    buttonText = Text(Point(5, -2), "Continue")
    buttonText.draw(win)

    img = Image(Point(-5, -5), "FiveClickHouse.gif").draw(win)

    win.getMouse()
    for msg in messages:
        msg.undraw()
    buttonText.undraw()
    button.undraw()
    img.undraw()

    p1 = getMouseClick(win, Point(5,-10), "Click for 1st point...", )

    p2 = getMouseClick(win, Point(5,-10), "Click for 2nd point...", )

    Rectangle(p1, p2).draw(win)

    p3 = getMouseClick(win, Point(5,-10), "Click for 3rd point...", )

    doorWidth = abs(p1.getX() - p2.getX()) / 5
    Rectangle(Point(p3.getX() - doorWidth / 2, p1.getY()),
              Point(p3.getX() + doorWidth / 2, p3.getY())).draw(win)

    p4 = getMouseClick(win, Point(5,-10), "Click for 4th point...", )

    Rectangle(Point(p4.getX() - doorWidth / 4, p4.getY() - doorWidth / 4),
              Point(p4.getX() + doorWidth / 4, p4.getY() + doorWidth / 4)).draw(win)

    p5 = getMouseClick(win, Point(5,-10), "Click for 5th point...", )

    Polygon(Point(p1.getX(), p2.getY()), p2, p5).draw(win)

    win.getMouse()

def getMouseClick(win, center, prompt):
        prompt = Text(center, prompt)
        prompt.setSize(14)
        prompt.setStyle("bold")
        prompt.draw(win)
        p1 = win.getMouse()
        prompt.undraw()
        return p1

main()