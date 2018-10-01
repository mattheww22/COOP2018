# practice02.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 01 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 02
#     Source: Python Programming
#    Chapter: Practice
#
# Program Description
#
#   This Program is an interactive calculator that accepts mathematical expressions.
#
#
# Algorith (pseudocode)
#
# Introduce program
# Loop until exit requested
# Get input
# Test for exit
# Evaluate mathematical expression
# Print result
#

def main():
    # Introduce program
    print("This Program is an interactive calculator that accepts mathematical expressions.")
    # Loop until exit requested
    while True:
        # Get input
        expr = input("Please enter a mathematical expression to evaluate (0 to quit): ")
        # Test for exit
        if expr == "0":
            break
        # Evaluate mathematical expression
        result = eval(expr)
        # Print result
        print("The expression", expr, "is equivalent to", result)

main()
