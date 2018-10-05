# practice01.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 01 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: practice01
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
# This program converts Joules to Calories
#
# Algorith (pseudocode)
#
#  Introduce program
#  Loop until exit requested
#  Get input for Joules (0 to quit)
#  Test for exit condition (break if true)
#  Calculate Joules to Calories (1 J = 0.239 Cal)
#       calories = joules * 0.239
#  Print result

print("\n" * 100)


def main():

    #  Introduce program
    print("This program converts Joules to Calories")

    # Loop until exit requested
    while True:

        #  Get input for Joules (0 to quit)
        joules = float(input("\nNumber of Joules (0 to quit): "))
        # Test for exit condition (break if true)
        if joules == 0:
            break

        #  Calculate Joules to Calories (1 J = 0.239 Cal)
        #       calories = joules * 0.239
        calories = joules * 0.239

        #  Print result
        print("\n",joules, "Joules is equivalent to: ",calories, "Calories")


main()
