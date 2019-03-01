"""
U07_Ex01_Overtime.py

  Author: Matthew Wiggans
  Course: Coding for OOP
 Section: A2
    Date: 2019-02-04
     IDE: PyCharm

Assignment Info
  Exercise: 01
    Source: Python Programming
   Chapter: 07

Program Description

    This program calculates the wages of workers throughout a work week

Algorithm

    Print introduction
    Get the hourly pay and number of hours from user
    Send hours and pay to func
        Check if the hours are over 40
        If there are more than 40
            Subtract 40 from hours
            Multiply hours times 40
            For all remaining hours by 1.5
        Print total hours and total wage

"""


def main():
    print("This program calculates the wages of workers throughout a work week")
    hour = float(input("How many hours do you work a week? "))
    wage = float(input("What is your wage? "))
    totalWage = getPay(hour, wage)
    print("${0} is your total pay for the week with {1} hours".format(totalWage, hour))


def getPay(hour, wage):
    if hour > 40:
        hours = hour - 40
        fourty = 40 * wage
        wage = wage * 1.5
        totalWage = wage * hours
        totalWage = totalWage + fourty

    else:
        totalWage = wage * hour

    return totalWage


if __name__ == '__main__':
    main()

"""
RESULTS:
========
getPay(0, 10)    -->     0 |       0 | [ Pass ]
getPay(1, 10)    -->    10 |      10 | [ Pass ]
getPay(10, 10)   -->   100 |     100 | [ Pass ]
getPay(39, 10)   -->   390 |     390 | [ Pass ]
getPay(40, 10)   -->   400 |     400 | [ Pass ]
getPay(41, 10)   -->   415 |   415.0 | [ Pass ]
========
"""
