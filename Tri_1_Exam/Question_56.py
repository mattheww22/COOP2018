# Question_56.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 14 Nov 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: N/A
#     Source: Python Programming
#    Chapter: N/A
#
# Program Description
#
#   This program is used to check if the three sticks given equal a triangle.
#
# Algorith (pseudocode)
#
# is_triangle using a, b, c
#   if c > a + b: return true
#   if a > c + b: return true
#   if b > a + c: true
#
#   otherwise, print false
#
# main
#
#   print introduction
#   get a, b and c lengths of sticks from the user
#   calculate triangle using if_triangle
#   if true, print "yes that is a triangle"
#   if false, print "no, that won't work"
#
#
def main():

    # print introduction
    print("This program calculates if it is possible for the 3 stick lengths given to make a triangle")

    # get inputs of a, b and c from user
    a, b, c = eval(input("What are the lengths of your 3 sticks? (separated by commas) "))

    myTriangle = is_triangle(a, b, c)

    # if true print yes
    if myTriangle:
        print("No, that is not a triangle")

    # if false print no
    if not myTriangle:
        print("Yes, that is a triangle")


def is_triangle(a, b, c):
    if c > a + b:
        return True

    if a > b + c:
        return True

    if b > c + a:
        return True

    elif True:
        return False


if __name__ == '__main__':
    main()
