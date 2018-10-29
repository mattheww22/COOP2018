# U03_Ex03_MolWeight.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 25 Sep 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 3
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
# This program calculates the molecular weight of a Carbohydrate.
#
#
#
# Algorith (pseudocode)
#
#   get inputs of hydrogen, carbon, oxygen
#   add up the values
#   print mol weight in grams per mole
#

def main():

    print("This program calculates the molecular weight of a carbohydrate.")
    hydrogen, carbon, oxygen = eval(input())
    weight = hydrogen + carbon + oxygen
    print(weight, " grams per mole")

main()
