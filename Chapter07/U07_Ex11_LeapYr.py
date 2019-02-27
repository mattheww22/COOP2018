"""
U07_Ex11_LeapYr.py

  Author: 
  Course: Coding for OOP
 Section: 
    Date: 2019-02-21
     IDE: PyCharm

Assignment Info
  Exercise: 11
    Source: Python Programming
   Chapter: 07

Program Description

    This problem computes whether the year entered was a leap year.

Algorithm

    Print intro
    Ask user for year they want to check
    Send to function
        Check if year is leap
            return leap
        Check if year is leap century
            return leap
        Anything else is not leap

    print results
"""
def main():

    print("This program computes if a given year is a leap year of not.")
    year = int(input("What year do you want to check? "))
    value = checkYr(year)
    if value == 1:
        print("{0} was a leap year.".format(year))
    if value == 2:
        print("{0} was not a leap year".format(year))
def checkYr(year):

    if year % 4 == 0:

        if year % 400 == 0:
            value = 2

        else:
            value = 1

    else:
        value = 2
    return value

if __name__ == '__main__':
    main()
"""
RESULTS:
========
checkYr(1600)   -->   2 |   2 | [ Pass ]
checkYr(1800)   -->   1 |   1 | [ Pass ]
checkYr(2000)   -->   2 |   2 | [ Pass ]
checkYr(2300)   -->   1 |   1 | [ Pass ]
checkYr(1959)   -->   2 |   2 | [ Pass ]
checkYr(1928)   -->   1 |   1 | [ Pass ]
========
"""