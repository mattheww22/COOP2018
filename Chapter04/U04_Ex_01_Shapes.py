# U04_Ex_01_Shapes.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 23 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 01
#     Source: Python Programming
#    Chapter: 04
#
# Program Description
#
# This program prints a rectangle that follows your mouse when you click.
#
#
# Algorith (pseudocode)
#
#   Create a red circle
#   Draw the circle
#   Find the mouse
#   Re-draw the circle on top of the mouse
#

from graphics import *


def main():
    win = GraphWin()
    shape = Rectangle(Point(50, 50), 20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)
    win.close()

main()
