# U02_Ex05_ConvertCtoF_Table.py
#
# Author:
# Course: Coding for OOP
# Section: A3
#     Date: 29 Aug 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise:
#     Source: Python Programming
#    Chapter:
#
# Program Description
#   This program converts temperature from Celsius to Fahrenheit
#
#
#
# Algorith (pseudocode)
#   Print program introduction
#   Get C° from user and assign to celsius
#   Calculate °F using 9/5 * °C + 32 and assign to fahrenheit
#   Print °F
#



def main():

    #   Print program introduction
    print("This program converts temperature from Celsius to Fahrenheit")

    for i in range(101):
        if i % 10 == 0:
            celsius = i
            fahrenheit = 9 / 5 * celsius + 32
            print(celsius, "°C is equal to", fahrenheit, "°F")

main()
