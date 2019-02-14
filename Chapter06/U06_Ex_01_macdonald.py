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
#  Send animal info to func
#       Create a loop that chooses a different animal and sound from the list
#       Print each song verse using .format

def main():
    print("This program prints 'Old MacDonald' for five different animals given by the user")

    animals = input("Enter the 5 animals that you want in the song separated by commas: ")
    animals = animals.split(",")

    sounds = input("Enter the sounds these animal's make: ")
    sounds = sounds.split(",")

    makeSong(animals, sounds)


def makeSong(animals, sounds):
    size = len(animals)

    for i in range(size):
        print(" ")
        firstLine()
        print("And on that farm he had a {0}, Ee-igh, Ee-igh, Oh!".format(animals[i]))
        print("With a {1} {1} here and a {1} {1} there".format(sounds[i], sounds[i]))
        print("Here a {1}, there a {1}, everywhere a {1} {1}".format(sounds[i], sounds[i]))
        firstLine()
        print(" ")


def firstLine():
    print("Old MacDonald had a farm Ee-igh, Ee-igh, Oh!")


main()
