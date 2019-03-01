"""
U07_Ex12_dayChecker.py

  Author: 
  Course: Coding for OOP
 Section: 
    Date: 2019-02-21
     IDE: PyCharm

Assignment Info
  Exercise: 12
    Source: Python Programming
   Chapter: 07

Program Description

    This program checks if the date you entered is valid.

Algorithm

    Print introduction
    Get date from user
    Send to testDay func
        Check month by checking if 12 or less
        Check day by making 3 checks (one for 31 days, one for 30 days, and one for February)
        If any return no, print, this is not a valid date
        If all pass, print: That date is valid
"""
def main():
    print("This program checks if the date you entered is valid.")
    date = input("What date do you want to check?(Separated by slashes) ")
    month, day, year = date.split("/")
    checked = checkDay(month, day)
    if checked == 2:
        print("The date you entered does not exist.")
    if checked == 1:
        print("That date is perfectly valid.")


def checkDay(month, day):
    month = int(month)
    day = int(day)
    if month > 12:
        checked = 2
    else:
        if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            if day > 31:
                checked = 2
            else:
                checked = 1
        elif month == 2:
            if day > 29:
                checked = 2
            else:
                checked = 1
        else:
            if day > 30:
                checked = 2
            else:
                checked = 1

    return checked

if __name__ == '__main__':

    main()

"""
RESULTS:
========
checkDay(12, 24)   -->   1 |   1 | [ Pass ]
checkDay(13, 24)   -->   2 |   2 | [ Pass ]
checkDay(12, 32)   -->   2 |   2 | [ Pass ]
checkDay(11, 31)   -->   2 |   2 | [ Pass ]
checkDay(7, 26)    -->   1 |   1 | [ Pass ]
checkDay(2, 29)    -->   2 |   2 | [ Pass ]
========
"""