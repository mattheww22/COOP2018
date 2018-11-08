# U04_Ex_06_FutChart.py
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
#   This graph prints a chart for a future value of a bank account.
#
#
# Algorith (pseudocode)
#
#   Print graphwin with input slots
#   Clear window
#   Draw graph
#   Get click before closing window

from graphics import *

def main():

    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    win.setCoords(0, 0, 10, 10)

    Intro = Text(Point(5, 8), "This plots a chart of a 10 year investment plan.")
    Intro.draw(win)

    inputPrincipal = Entry(Point(8, 5), 10)
    inputPrincipal.setText("0.0")
    inputPrincipal.draw(win)

    Principal = Entry(Point(3, 5), "Enter the first principal")
    Principal.setText("0.0")
    Principal.draw(win)

    Rate = Entry(Point(3, 3), "Enter the yearly rate: ")
    Rate.setText("0.0")
    Rate.draw(win)

    inputRate = Entry(Point(8, 3), 10)
    inputRate.setText("0.0")
    inputRate.draw(win)

    win.getMouse()

    principal = float(Principal.getText)
    apr = float(inputRate.getText())

    Intro.undraw()
    Principal.undraw()
    Rate.undraw()
    inputRate.undraw()
    inputPrincipal.undraw()

    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)

    for year in range():
        bar = Rectangle(Point(0, 0), Point(1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    win.getMouse()
    win.close()

