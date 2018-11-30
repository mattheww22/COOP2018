# U05_Ex01_Convert.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 27 Nov 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 1
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#
#   Converts day month and year numbers into two date formats
#
# Algorith (pseudocode)
#
#   Get numeric input of date from user
#   Convert the month number to an actual month name
#   print converted date
#

def main():

    # get the day month and year as numbers
    dateStr = input("Enter a date in number form separated by slashes: ")

    monthStr, dayStr, yearStr = dateStr.split('/')

    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]
    monthStr = months[int(monthStr) - 1]

    print("The converted date is", monthStr, dayStr, yearStr)


main()
