"""
U06_Ex_11_Square.py

  Author: 
  Course: Coding for OOP
 Section: 
    Date: 2019-02-06
     IDE: PyCharm

Assignment Info
  Exercise: 11
    Source: Python Programming
   Chapter: 06

Program Description

    This program accepts a list of numbers and prints their square root.

Algorithm

    Get nums from user
    Send nums to program
    Square each number
    Print list of squared numbers

"""


def main():
    print("This program gets the squared result of a list of numbers entered by the user.")
    nums = input("What numbers do you want squared? ")
    squared, num = square(nums)
    print("{0} is the squared result of {1}".format(squared, num))


def square(nums, ):
    for num in nums:
        squared = num ** 2
        return num, squared


main()
