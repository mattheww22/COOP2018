# U03_Ex01_Vol-Surface.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 25 Sep 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 1
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
# This program calculates the volume and surface area of a sphere.
#
#
#
# Algorith (pseudocode)
#
# Print program description
# Get input of radius
# Calculate volume using (4/3(π)r2)
# Calculate surface area (4(π)r2)
# Print calculated volume and SA
#


def main():

    print("This program calculates the volume and surface area of a cylinder using the radius.")

# Get input of radius
    radius = int(input("Enter Radius"))

# Calculate volume using (4/3(π)r**2)
    volume = 4/3 * 3.14 * radius**2

# Calculate surface area (4(π)r**2)
    sa = 4 * 3.14 * radius**2

# Print calculated volume and SA
    print("Your volume is: ", volume, "and your surface area is: ", sa, "for a sphere of with the radius of:", radius)


main()
