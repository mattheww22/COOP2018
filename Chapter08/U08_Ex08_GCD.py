"""
U08_Ex08_GCD.py

  Author: Matthew Wiggans
  Course: Coding for OOP
 Section: A3
    Date: 2019-03-25
     IDE: PyCharm

Assignment Info
  Exercise: 06
    Source: Python Programming
   Chapter: 08

Program Description

    This program computes the greatest common divisor of two numbers given by the user.

Algorithm

    Print introduction
    Get m and n from user
    Send m & n to func
        Calculate GCD with n,m = m, n % m
        Return n
    Print GCD
"""


def main():

    print("This program computes the greatest common divisor of two numbers given by the user.")
    n = int(input("Please enter your first number. "))
    m = int(input("Please enter your second number. "))

    GCD = getFactor(m,n)
    print("The greatest common divisor of {0} and {1} is {2}.".format(n, m, GCD))

def getFactor(m, n):

    while m != 0:
        n, m = m, n % m
    return n
if __name__ == '__main__':

    main()

"""

RESULTS:
========
getFactor(27, 36)     -->    9 |    9 | [ Pass ]
getFactor(12, 24)     -->   12 |   12 | [ Pass ]
getFactor(3, 9)       -->    3 |    3 | [ Pass ]
getFactor(100, 625)   -->   25 |   25 | [ Pass ]
getFactor(10, 12)     -->    2 |    2 | [ Pass ]
getFactor(5, 110)     -->    5 |    5 | [ Pass ]
========

"""
