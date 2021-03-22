# Zach Taylor - CINF308 Programming for Informatics


def main():
    fileNotOpen = True
    makeDict = {}
    userInput = True

    while fileNotOpen:  # Will continue to ask the user for a file name
        try:
            fileInput = input("Please enter the path of your document: ")
            f = open(fileInput, "r")  # Used to open file
            fileNotOpen = False
        except FileNotFoundError:
            print("File does not exist. Please ensure the name is correct.")

    next(f)  # Skips first line
    for line in f:
        wordsOnLine = line.split(',')  # Splits each line in file by ','
        if wordsOnLine[46] in makeDict:  # If make is already in dictionary
            model, cityMPG, highwayMPG = makeDict[wordsOnLine[46]]  # Unpack key make from dictionary
            if int(cityMPG) > int(wordsOnLine[4]):
                makeDict[wordsOnLine[46]] = [wordsOnLine[47], wordsOnLine[4], wordsOnLine[34]]  # Update values
        else:  # If make is not in dictionary
            makeDict[wordsOnLine[46]] = [wordsOnLine[47], wordsOnLine[4], wordsOnLine[34]]  # Add to dictionary
    makeDict = {x.upper(): y for x, y in makeDict.items()}  # Sets all key values to uppercase, ignores rest

    while userInput is True:  # Continues to ask user until userInput is False
        command = input("Please enter a command [list, quit]: ")
        if command == "quit":  # Closes loop + quits program
            print("Goodbye.")
            userInput = False
        elif command == "list":
            listChoice = input("Please enter a specific make or all: ")
            if listChoice == "all":  # Prints out every value in dictionary
                print("{:40s}{:40s}{:15s}{:10s}\n".format("Make", "Model", "CityMPG", "HighwayMPG"))  # Column headings
                for key, value in makeDict.items():
                    model, cityMPG, highwayMPG = value  # Set list equal to variable
                    print("{:40s}{:40s}{:15s}{:10s}".format(key, model, cityMPG, highwayMPG))
            else:
                if listChoice in makeDict:  # Prints out specific car make
                    print("{:40s}{:40s}{:15s}{:10s}".format("Make", "Model", "CityMPG", "HighwayMPG"))
                    model, cityMPG, highwayMPG = makeDict[listChoice]
                    print("{:40s}{:40s}{:15s}{:10s}\n".format(listChoice, model, cityMPG, highwayMPG))
                else:
                    print("Make not found. Ensure vehicle make is uppercase.")  # If make not found, print error
        else:
            print("Command not found.")


main()
