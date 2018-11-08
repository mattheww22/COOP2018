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
from U04_Ex04_WinterScene import drawCircle

def main():
    win = GraphWin("Dice", 560, 120)
    win.setBackground("green4")

    # draw dies 1 - 5 for straight
    for i in range(1, 6):
        drawDie(win, i)
    win.getMouse()

def drawDie(win, rank):
    """
    Draws 1 die of given rank
    Algorithm: 1) draw rectangle for die; 2) draw pips based on rank
    :param win: GraphWin object
    :param rank: int -> rank of die
    """
    rect = Rectangle(Point(10 + 110*(rank - 1), 10), Point(110 + 110*(rank - 1), 110))
    rect.setOutline("black")
    rect.setFill("white")
    rect.draw(win)

    if rank % 2 == 1:
        drawPipCenter(win, rect.getCenter())

    if rank == 2 or rank == 3:
        drawPipTL(win, rect.getCenter())
        drawPipBR(win, rect.getCenter())


    if rank == 4 or rank == 5:
        drawPipTL(win, rect.getCenter())
        drawPipBL(win, rect.getCenter())
        drawPipTR(win, rect.getCenter())
        drawPipBR(win, rect.getCenter())

def drawPipCenter(win, dieCenter):

    drawCircle(dieCenter, 7, "black", "black").draw(win)

def drawPipTL(win, dieCenter):

    drawCircle(Point(dieCenter.getX() - 30, dieCenter.getY() - 30), 7, "black", "black").draw(win)

def drawPipTR(win, dieCenter):

    drawCircle(Point(dieCenter.getX() + 30, dieCenter.getY() - 30), 7, "black", "black").draw(win)

def drawPipBL(win, dieCenter):

    drawCircle(Point(dieCenter.getX() - 30, dieCenter.getY() + 30), 7, "black", "black").draw(win)

def drawPipBR(win, dieCenter):

    drawCircle(Point(dieCenter.getX() + 30, dieCenter.getY() + 30), 7, "black", "black").draw(win)

main()