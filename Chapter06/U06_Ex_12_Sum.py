"""
U06_Ex_12_Sum.py

  Author: 
  Course: Coding for OOP
 Section: 
    Date: 2019-02-11
     IDE: PyCharm

Assignment Info
  Exercise: 12
    Source: Python Programming
   Chapter: 06

Program Description

    This program adds all of the numbers given by a user together.

Algorithm

    Get numbers from user
    Convert strings to nums using loop
    Send list to add func addNums
        Add all of the nums together in a loop
    print added sum

"""


def main():
    print("This program gets the sum of all of the numbers given to it.")

    nums = input("Enter numbers you want added (separated by spaces) ")

    nums = nums.split(' ')

    for i in range(len(nums)):
        nums[i] = int(nums[i])

    sumTot = addNums(nums)

    print("{0} is the sum of your numbers.".format(sumTot))


def addNums(nums):

    sumTot = 0
    for numb in nums:
        sumTot = sumTot + numb
    return sumTot


if __name__ == '__main__':
    main()
