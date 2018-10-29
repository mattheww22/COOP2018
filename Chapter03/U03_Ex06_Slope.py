# U03_Ex06_Slope.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 25 Sep 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 6
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
# This program finds the slope of a line.
#
#
#
# Algorith (pseudocode)
#
# Get two points in the separated by commas
# add up a + c and b + d
# Print slope
#

def main():

print("This program finds the slope of a line.")
a, b, c, d = eval(input("What are your four values?"))
aa = c - a
bb = d - b

slope = bb / aa

print(slope, " is your slope.")

main()