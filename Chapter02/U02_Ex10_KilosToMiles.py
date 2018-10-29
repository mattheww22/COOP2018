# U02_Ex10_KilosToMiles.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 31 Aug 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 10
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
#   This program converts Kilometers into Miles!!
#
#
#
# Algorith (pseudocode)
#   Take Kilometers from the user
#   Calculate num of miles (kilometers * .62)
#   Print Miles
#
#

def main():

    #   Take Kilometers from the user
    print("This program converts kilometers to miles!")
    kilometers = eval(input("Enter °kilometers to convert: "))

    #   Calculate num of miles (kilometers * .62)
    miles = kilometers * .62

    #   Print Miles
    print(kilometers, "kilometers is equal to: ", miles, "miles")


main()
