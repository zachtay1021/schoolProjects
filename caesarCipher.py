print("-------------------------------------------------------------------------------------")
print("| This program will take user input for the number of rotation and encrypt the text |")
print("-------------------------------------------------------------------------------------")
input("Press enter to continue...")

rotation = ""
rotationSatisfied = False
acceptableKey = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

while rotationSatisfied is False:
    rotation = int(input("Please enter the number of characters to rotate by (0-25): "))
    if rotation in acceptableKey:
        rotationSatisfied = True
    else:
        continue

message = input("Please enter your message to encrypt: ")


def rotateLetter(letter):
    numericLetter = ord(letter) - 97
    numericLetter += rotation
    numericLetter = numericLetter % 26
    numericLetter += 97
    encodedLetter = chr(numericLetter)
    return encodedLetter


for lines in message:
    lowerCaseLines = lines.lower()  # Returns input as lowercase so all input is between our unicode table values
    for letter in lowerCaseLines:

        isLetter = (ord(letter) >= 97) and (ord(letter) <= 122)

        if (isLetter):
            encodedLetter = rotateLetter(letter)
            print(encodedLetter, end='')
        else:
            print(letter, end='')

print()
