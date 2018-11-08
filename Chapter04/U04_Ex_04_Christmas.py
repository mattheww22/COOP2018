# U04_Ex_04_Christmas.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 25 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 4
#     Source: Python Programming
#    Chapter: 4
#
# Program Description
#
#
#
#
# Algorith (pseudocode)
#
#   Import Graphics
#   Create a GraphWin
#   Draw backgraound
#       draw sky
#       draw ground
#   Draw snowman
#   Draw tree
#
#
from graphics import *


def main():

    win.setCoords(-10)
    win = GraphWin("Winter Scene", 800, 600)
    drawSky()
    # drawGround()
    drawSun()
    drawSnowman()
    drawTree()
    input("Press ENTER to exit")
    win.close()


def drawSky():

    drawRect(Point(0,0), Point(600,600), "black", "black").draw(win)


def drawSun():
    pass


def drawSnowman():
    """
    Algorithm:
        draw circle for bottom of body
        draw circle for middle
        draw circle for head
        draw face on head

    :return:
    """


def drawTree():
    """
    Algorithm: 1) make points for first triangle; 2) draw rectangle for trunk; 3) make triangles for tree above the last one
    :return: Graphwin object
    """
    p1x
    p1y

main()
