"""
U06_Ex_13_strToNum.py

  Author: 
  Course: Coding for OOP
 Section: 
    Date: 2019-02-15
     IDE: PyCharm

Assignment Info
  Exercise: 13
    Source: Python Programming
   Chapter: 06

Program Description

    This program turns a string of numbers given by a user into a list of integers.

Algorithm

    Get string numbers from the user
    Split strList into a list of strings
    Send to toNumbers function
        transfer the str to int
        Return int list to main
    print int
"""


def main():
    print("This program turns a string given by the user into a number.")
    strList = input("Please enter the numbers that you want to have converted. (separated by spaces) ")
    strList = strList.split(" ")
    toNumbers(strList)
    print("Your number(s) in integer form are: {0}".format(strList))


def toNumbers(strList):
    for num in strList:

        num = int(num)


if __name__ == '__main__':

    main()
