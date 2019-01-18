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
#   This program prints a fun winter scene!
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
from math import sin, pi, cos


def main():
    win = GraphWin("Winter Scene", 800, 600)
    drawSky(win)
    drawSnowman(win)
    drawTree(win)
    input("Press ENTER to exit")
    win.close()


def drawSky(win):
    drawRect(Point(0, 0), Point(600, 600), "black", "black").draw(win)


def drawSnowman(win):
    """
    Algorithm:
        draw circle for bottom of body
        draw circle for middle
        draw circle for head
        draw face on head

    :return:
    """
    center = drawBody(win, 400, 450)
    drawFace(win, center)
    ef

def drawBody(win, x, y):
    radius = 40
    center = Point(x, y)

    for i in range(3):
        center = Point(400, center.getY() - 2 * radius)
        drawCircle(center, radius, "black", "white").draw(win)
        if i == 1:
            drawArms(win, center, radius)
        radius -= 10
    return center

def drawFace(win):
    drawEyes(win, p)
    drawMouth(win, p)
    drawNose(win, p)


def drawEyes(win):
    drawCircle(Point(p.getX() - 4, p.getY() - 4), 2, "black", "black").draw(win)
    drawCircle(Point(p.getX() + 4, p.getY() - 4), 2, "black", "black").draw(win)

def drawMouth(win):
    drawTriangle([Point(p.getX() - 2, p.getY()),
                  Point(p.getX() + 2, p.getY()),
                  Point(p.getX() - 2, p.getY() + 10)], "orange4", "orange").draw(win)
def drawNose(win):
    Line(Point(p.getX() - 5, p.getY() + 6), Point(p.getX(), p.getY() + 8)).draw(win)
    Line(Point(p.getX(), p.getY() + 8), Point(p.getX() + 5, p.getY() + 7)).draw(win)

def drawTree(win):
    """
    Algorithm: 1) make points for the first triangle; 2) draw rectangle for the trunk; 3) make triangles for tree above the last one
    :return: Graphwin object
    """
    p1x = 90
    p1y = 480
    p2x = 210
    p2y = 480
    p3x = 150
    p3y = 394
    drawRect(Point(145, 500), Point(155, 450), "brown4", "brown").draw(win)
    for i in range(3):
        drawTriangle([Point(p1x, p1y),
                      Point(p2x, p2y),
                      Point(p3x, p3y)], "green4", "green").draw(win)
        p1x = p1x + 10
        p1y = p1y - 40
        p2x = p2x - 10
        p2y = p2y - 40
        p3y = p1y - sin(60 * 180 / pi) * (p2x - p1x)


def drawCircle(center, radius, outline, fill):
    circ = Circle(center, radius)
    circ.setOutline(outline)
    circ.setFill(fill)
    return circ


def drawRect(p1, p2, outline, fill):
    rect = Rectangle(p1, p2)
    rect.setOutline(outline)
    rect.setFill(fill)
    return rect


def drawTriangle(points, outline, fill):
    tri = Polygon(points)
    tri.setOutline(outline)
    tri.setFill(fill)
    return tri

    if __name__ == '__main__':

main()
