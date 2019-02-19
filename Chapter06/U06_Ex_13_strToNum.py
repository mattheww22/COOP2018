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

    This program turns a string given by the user into a number.

Algorithm

    Get string numbers from the user
    Send to transfer function
        transfer the str to int

    print int
"""


def main():
    print("This program turns a string given by the user into a number.")
    nums = input("Please enter the numbers that you want to have converted. (separated by spaces) ")
    nums = nums.split(" ")
    transfer(nums)
    print(nums)


def transfer(nums):
    for num in nums:

        num = int(num)



main()
