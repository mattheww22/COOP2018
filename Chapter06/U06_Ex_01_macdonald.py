# U06_Ex_01_MacDonald.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 14 Dec 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 01
#     Source: Python Programming
#    Chapter: 06
#
# Program Description
#
#   This program prints the song "Old MacDonald with 4 different animals.
#
#
# Algorith (pseudocode)
#
#  Introduce program
#  Get five different animals from user
#  Print each song using the animals given by the user

def main():

    print("This program prints 'Old MacDonald' for five different animals given by the user")
    an1, s1, an2, s2, an3, s3, an4, s4, an5, s5 = input("Enter the 5 animals and noises you want in the song separated by commas: ")
    print("Old MacDonald had a farm Ee-igh, Ee-igh, Oh!")
    print("And on that farm he had a {0}, Ee-igh, Ee-igh, Oh!".format(an1))
    print("With a {1}{1} here and a {1}{1} there".format(s1, s1))

main()