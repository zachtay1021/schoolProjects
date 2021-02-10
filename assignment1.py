# Zach Taylor - CINF308 Programming for Informatics

import sys

fileInput = input("Please enter the path of the text document you want to analyze: ")

# Must set variable to true for while loop
fileNotOpen = True

# Tries to open file. If file is not found, return error code and exit program
while fileNotOpen:
    try:
        f = open(fileInput, "r")  # Used to open file
        fileNotOpen = False
    except FileNotFoundError:
        print("File does not exist. Please ensure the name is correct.")
        print("Exiting...")
        sys.exit()

# Reads file. Required for string count
f = f.read()

# Splits each line based on line break. Sets int value to string
lineCount = len(f.split("\n"))
lineCount = str(int(lineCount))

# Finds the number of 'and' and 'or' occurrences in open file
numberOfAnd = f.count("and")
numberOfOr = f.count("or")

# Sets int value to string
numberOfAnd = str(int(numberOfAnd))
numberOfOr = str(int(numberOfOr))

print("This file has " + lineCount + " lines.")
print("This file has the word 'and' " + numberOfAnd + " times.")
print("This file has the word 'or' " + numberOfOr + " times.")
