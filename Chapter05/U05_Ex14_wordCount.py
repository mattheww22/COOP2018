# U05_Ex14_wordCount.py
#
# Author: Matthew Wiggans
# Course: Coding for OOP
# Section: A3
#     Date: 17 Dec 2018
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: 14
#     Source: Python Programming
#    Chapter: 05
#
# Program Description
#
#   This program prints the number of words and characters in a file that is provided by the user
#
#
# Algorith (pseudocode)
#
#   Print introduction
#   Get file from user
#   Open, read, and close the file
#   Run getLines
#       add 1 to linCt
#   Run getWords
#       loop counting
#           Count the words
#   Run getChar
#       Use the list of words to get the number of characters in each word
#       Add all together for sum of characters
#   Print characters, and words
#
def main():
    file = input("What is the file that you want to be calculated? ")
    f = open(file, "r")
    phr = f.readlines()
    f.close()
    charNum, wordNum = getLines(phr)

    print("There are {0} lines, {1} words, and {2} characters in your sentence.".format(len(phr), charNum, wordNum))

def getLines(phr):
    wordNum = 0
    charNum = 0

    for line in phr:
        words = line.split(" ")
        wordNum += len(words)

        for word in wordNum:
            charNum += len(word)

    return charNum, wordNum

if __name__ == '__main__':

    main()
