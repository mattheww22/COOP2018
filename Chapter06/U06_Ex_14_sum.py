"""
U06_Ex_14_sum.py

  Author: 
  Course: Coding for OOP
 Section: 
    Date: 2019-02-26
     IDE: PyCharm

Assignment Info
  Exercise: 14
    Source: Python Programming
   Chapter: 06

Program Description

    This program converts a list of string numbers in a file and finds their sum and their sum squared

Algorithm

    Import all from last three programs
    Get the file from user
    Open and read the file
    Close the file
    Convert the string of numbers to integers using strToNum.py
        Return list of nums
    Send integers to Sum.py
        Return the sum
    Send numbers to Square.py
        Return the squared values
    Prints the sum of the squared values
"""

from Chapter06.U06_Ex_12_Sum import *
from Chapter06.U06_Ex_11_Square import *
from Chapter06.U06_Ex_13_strToNum import *

def main():
    print("This program converts a list of string numbers in a file and finds their sum and their sum squared")
    file = input("What file do you want to pull from? ")
    nums = open(file, "r")
    nums.readlines()
    nums.close()
    nums = toNumbers(nums)
    squared = squareEach(nums)
    added = addNums(squared)
    print(added)

if __name__ == '__main__':
    main()