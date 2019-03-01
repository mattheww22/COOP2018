"""
U07_Ex13_dayNumber.py

  Author: 
  Course: Coding for OOP
 Section: 
    Date: 2019-02-21
     IDE: PyCharm

Assignment Info
  Exercise: 13
    Source: Python Programming
   Chapter: 07

Program Description


Algorithm



"""
def main()

    print("This program will show what day of the year that date is.")
    date = input("What date do you want to calculate?(Ex; Jan 24) ")
    number = dayNumber(date)
    print("That day is #{0} out of 365".format(number))

def dayNumber(date):
    month, day = date.split(" ")
    myNum = "Jan" * 31, "Feb" * 28, "Mar" * 31, "Apr" * 30, "May" * 31, "Jun" * 30, "Jul" * 31, "Aug" * 30 * "Sep" * 31, "Oct" * 31, "Nov" * 30, "Dec" * 31
    myNum = myNum[month, ]
