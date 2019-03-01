# U05_Ex10_avg-leng.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 06 Dec 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 10
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#
#   This program prints the average length of words in a sentence given by the user.
#
#
# Algorith (pseudocode)
#
#   Print intro
#   Get input of sentence from user
#   Send sentence to func
#       Split into words by splitting on spaces
#       Loop through each word
#           Split into characters
#           Get the length of each word
#       average the lengths
#       Return average
#   Print average word length
#
#
def main():

    print("This program prints the average length of words in a sentence given by the user.")
    sentence = input("What words do you want to average? ")
    average = findLen(sentence)
    print("There was an average of {0} characters per word.".format(average))

def findLen(sentence):
    total = 0
    words = sentence.split(" ")

    for i in range(len(words)):
        letters = list(words[i])

        for letter in letters:
            total = total + 1

    average = total / len(words)
    return average

main()
