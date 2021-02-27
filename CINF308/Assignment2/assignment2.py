# Zach Taylor - CINF308 Programming for Informatics


def main():
    fileNotOpen = True
    wordsOnLine = []
    makeCol = []
    makeColUnq = []
    lowMPGCity = 1000000
    lowMPGCityModel = ''
    lowMPGCityMake = ''
    lowMPGHiway = 1000000
    lowMPGHiwayMake = ''
    lowMPGHiwayModel = ''

    while fileNotOpen:  # Will continue to ask the user for a file name
        try:
            fileInput = input("Please enter the path of your document: ")
            f = open(fileInput, "r")  # Used to open file
            fileNotOpen = False
        except FileNotFoundError:
            print("File does not exist. Please ensure the name is correct.")

    for line in f:
        wordsOnLine = line.split(',')  # Splits each line in file by ','
        if 'Gasoline' in wordsOnLine[31] and 'Cars' in wordsOnLine[62]:  # Looks for specific keyword in certain indexes
            makeCol.append(wordsOnLine[46])  # If specific keyword found, append index value to list
            if float(wordsOnLine[4]) < lowMPGCity:  # Used to find lowest City MPG. Will loop over every line
                lowMPGCity = float(wordsOnLine[4])  # If found, assign value to lowMPGCity variable
                lowMPGCityModel = wordsOnLine[47]  # If found, assign car model to variable
                lowMPGCityMake = wordsOnLine[46]  # If found, assign car make to variable
            if float(wordsOnLine[34]) < lowMPGHiway:
                lowMPGHiway = float(wordsOnLine[4])
                lowMPGHiwayModel = wordsOnLine[47]
                lowMPGHiwayMake = wordsOnLine[46]
    for word in makeCol:
        if word not in makeColUnq:
            makeColUnq.append(word)  # Creates unique list based on words in makeCol list
    makeColUnq.sort()  # Sorts values alphabetically
    print("List of Unique Vehicles:")
    for item in makeColUnq:  # Prints each item in own line
        print(item)

    print("Make:", lowMPGCityMake, "   Model:", lowMPGCityModel, "   Lowest City MPG:", lowMPGCity)
    print("Make:", lowMPGHiwayMake, "   Model:", lowMPGHiwayModel, "   Lowest Highway MPG:", lowMPGHiway)


main()
