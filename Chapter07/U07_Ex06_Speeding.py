"""
U07_Ex06_Speeding.py

  Author: 
  Course: Coding for OOP
 Section: 
    Date: 2019-02-04
     IDE: PyCharm

Assignment Info
  Exercise: 06
    Source: Python Programming
   Chapter: 07

Program Description

    This program calculates the speeding ticket cost based on yoh

Algorithm

    Print introdudction
    Get MPH from user
    Get speed limit from user
    Send the MPH and limit to func

        If the MPH is greater than speed limit
            Subtract to find by how many
            Add 5 to whatever speed was calculated
            If MPH over 90
                add 200 to fine
                send to main
            else
                send to main

        Else
            return nothing


"""


def main():
    print("Welcome to Podunkville This program checks to see if you were speeding and what your fine would be.")
    limit = int(input("What was the speed limit? "))
    MPH = int(input("How fast were you going? "))
    fine = speedCheck(limit, MPH)

    if fine == 1:
        print("You have no fine, you are a good driver. :)")
    else:
        print("You were speeding!! Your fine will be ${0}".format(fine))


def speedCheck(limit, MPH):
    if MPH > limit:
        fine = 50
        over = MPH - limit

        if over >= 90:
            fine = over * 5
            fine = fine + 200

        else:

            fine = over + fine

    else:
        fine = 1
    return fine


if __name__ == '__main__':
    main()
