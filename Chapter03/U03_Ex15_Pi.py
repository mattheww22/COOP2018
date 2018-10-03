# U03_Ex15_Pi.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 25 Sep 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 15
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
# This program approximates pi
#
#
#
# Algorith (pseudocode)
#
# Introduce program
# Get number of terms to from user
# Initialize approxPI to zero
#     ApproxPI = 0
# in a loop from 1 to n
#   add current term to approxPI
#       approxPI += 4 / (2n-1)
# calculate difference between approxPI and math.pi
#   diff = math.pi - approxPI
# display results
#
# Thanks for the help Will!!
#
import math

def main():
amount = input
switch = 1
total = 0

for i in range(amount * 2):
    if i !=0 and i%2 !=0:
        if switch ==1:
            total += 4/i
            switch = 2
    elif switch == 2:
        total == 4/i
        switch = 1

    print("\n Pi is equal to: ", str(total))


