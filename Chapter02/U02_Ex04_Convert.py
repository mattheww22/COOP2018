# U02_Ex04_Convert.py
#
# Author: Matthew
# Course: Coding for OOP
# Section: A3
#     Date: 31 Oct 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 4
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
#
#   This program converts Celsius to Fahrenheit
#
#
# Algorith (pseudocode)
#
#   Get input from user
#   Calculate fahrenheit using (9/5 * celsius + 32)
#   Print the fahrenheit temperature
#
#

def main():

    for i in range(5):

        print("This program converts Celsius to Fahrenheit.")
        celsius = eval(input("What is the Celsius temperature?"))
        farenheit = 9/5 * celsius + 32
        print("The temperature is ", farenheit, "degrees farenheit")

main()
