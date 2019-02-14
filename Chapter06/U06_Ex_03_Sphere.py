# U06_Ex_03_MacDonald.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 14 Dec 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 03
#     Source: Python Programming
#    Chapter: 06
#
# Program Description
#
#   This program prints the surface area and volume of a sphere using a given radius
#
# Algorith (pseudocode)
#
#   Print introduction
#   Get radius from user
#   Send radius to getSurface
#       Calculate surface area using 4 * 3.14 * r ** 2
#   Send radius to getVol
#       Calculate volume using 4 / 3 * 3.14 * r ** 2
#   Print both using .format
#
from math import *

def main():
    print("This program prints the surface area of a sphere")
    r = float(input("What is the radius of your sphere? "))
    surf = getSurface(r)
    print("{0} is the surface area of your sphere.".format(surf))
    volume = getVol(r)
    print("{0} is the volume of your sphere.".format(volume))


def getSurface(r):
    surf = 4 * pi * r ** 2
    return surf


def getVol(r):
    volume = 4 / 3 * pi * r ** 3
    return volume


if __name__ == '__main__':
    main()
