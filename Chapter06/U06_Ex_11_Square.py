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

    This program accepts a list of numbers and prints their squared values.

Algorithm

    Get nums from user
    Split into list using spaces
    Send nums to func
        Make each number an integer
        Square each number
        Return squared value
    Print list of squared numbers

"""


def main():
    print("This program gets the squared result of a list of numbers entered by the user.")
    nums = input("What numbers do you want squared? ")
    nums = nums.split(" ")
    squareEach(nums)
    print("{0} is the squared result of your numbers".format(nums))


def squareEach(nums):
    for i in range(len(nums)):
        num = int(nums[i])
        nums[i] = num ** 2

main()
