# U02_Ex09_ConvertFtoC.py.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 31 Aug 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 9
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
# This program converts fahrenheit to celsius
#
#
#
# Algorith (pseudocode)
# Print program introduction
# Get F° from user and assign to celsius
# Calculate °C using 9/5 * °F + 32 and assign to fahrenheit
# Print °F
#
def main():

    #   Print program introduction
    print("This program converts temperature from Fahrenheit to Celsius")
    #   Get F° from user and assign to celsius
    fahrenheit = eval(input("Enter °F to convert:"))

    #   Calculate °C using 9/5 * °F + 32 and assign to fahrenheit
    Celsius = (fahrenheit - 32) * 5/9
    #   Print °F
    print(fahrenheit, "°F is equal to", Celsius, "°C")


main()