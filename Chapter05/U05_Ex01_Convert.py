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
#   Split date into month, day, and year
#   Initialize string of month names
#   Convert the month number to an actual month name subtracting 1 to get accurate month
#   Print converted date
#

def main():

    # get the day month and year as numbers
    dateStr = input("Enter a date in number form separated by slashes: ")

    monthStr, dayStr, yearStr = dateStr.split('/')

    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]
    monthStr = months[int(monthStr) - 1]

    print("The converted date is: {0} {1},{2}".format(monthStr, dayStr, yearStr))

main()
