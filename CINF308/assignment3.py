# Zach Taylor - CINF308 Programming for Informatics
import sys


def open_files():
    fileNotOpen = True
    while fileNotOpen:  # Will continue to ask the user for a file name
        try:
            fileInput = input("Please enter the path of your document: ")
            global f
            f = open(fileInput, "r")  # Used to open file
            fileNotOpen = False
        except FileNotFoundError:
            print("File does not exist. Please ensure the name is correct.")

    global outputFile  # Allows file to be used outside of open_files() function
    outputFile = open('Encrypted.txt', 'w')  # Creates Encrypted.txt file


def main():
    open_files()
    try:
        key = int(f.readline())  # Tries to set first line in file to integer
    except ValueError:  # If first line is not integer, it returns a ValueError
        print("The first line of the input file is not an integer.")
        print("Exiting...")
        sys.exit()

    encryptedWord = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    digit = "1234567890"
    lowerTuple = tuple(alpha.lower())
    upperTuple = tuple(alpha.upper())
    digitTuple = tuple(digit)

    for line in f:  # Reads each line in input file
        if len(line) > 0:  # Skips over any line without text
            for x in range(len(line)):  # Creates a list with the length of the number of characters on a line
                if line[x] in lowerTuple:  # If character is lowercase
                    index = lowerTuple.index(line[x])
                    encryptedWord = encryptedWord + lowerTuple[(index + key) % 26]
                elif line[x] in upperTuple:  # If character is uppercase
                    index = upperTuple.index(line[x])
                    encryptedWord = encryptedWord + upperTuple[(index + key) % 26]
                elif line[x] in digitTuple:  # If character is number
                    index = digitTuple.index(line[x])
                    encryptedWord = encryptedWord + digitTuple[(index + key) % 10]
                elif line[x] == '\n':  # If character is line break
                    encryptedWord = encryptedWord + '\n'  # Print line break to output file to keep same layout as input
                else:
                    continue
    outputFile.write(encryptedWord)  # Writes encrypted string to output file
    return encryptedWord, f


main()
