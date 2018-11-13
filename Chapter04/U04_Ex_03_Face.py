# U04_Ex_03_Face.py
#
# Author:
# Course: Coding for OOP
# Section: A3
#     Date: 25 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise:
#     Source: Python Programming
#    Chapter:
#
# Program Description
#
#   This program draws a face using circles and a line for a mouth
#
#
# Algorith (pseudocode)
#
#   Draw face
#   Draw eyes
#   Draw nose
#

from graphics import *




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

def main():
    win = GraphWin("Face", 800, 800)
    drawHead(win)
    drawEyes(win)
    drawNose()
    drawMouth()
    input("Press enter to exit")
    win.close()

def drawHead(win):
    makeCircle(Point(400, 400), 350, "yellow").draw(win)


def drawEyes(win):
    """
    make left eye
    make right eye
    move clone to left
    :return:
    """

    leftEye = makeCircle(Point(250, 267), 20, "black")
    rightEye = leftEye.clone()
    rightEye.move(300, 0)
    leftEye.draw(win)
    rightEye.draw(win)


def drawNose(win):
    """

    Make circle in center of face
    :return:
    """
    nose = makeCircle(Point(200, 200), 50, "blue")
    nose.draw(win)

def drawMouth(win):

    """
    Draw a line in the bottom half of the circle for mouth
    :return: Line
    """

    mouth = makeCircle(Point(200, 300), 75, "black")
    mouth.draw(win)

main()
