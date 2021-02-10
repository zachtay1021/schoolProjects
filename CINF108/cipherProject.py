print("--------------------------------------------")
print("| This program has four different ciphers. |")
print("| 1. ROT13 Cipher                          |")
print("| 2. Caesar Cipher                         |")
print("| 3. Reverse Cipher                        |")
print("| 4. A1Z26 Cipher                          |")
print("--------------------------------------------")

user_choice = ""
inputSatisfied = False
acceptableInput = [1, 2, 3, 4]


while inputSatisfied is False:
    user_choice = int(input("Please select one of the ciphers from above to use: "))
    if user_choice in acceptableInput:
        inputSatisfied = True
    else:
        continue


if user_choice == 1:
    print("---------------------------------------------------------------")
    print("| This program is designed to encrypt input text by the user. |")
    print("---------------------------------------------------------------")
    input("Press enter to continue...")

    rotation = 13  # Sets a constant rotation / need to make this as input and set to variable
    userMessage = input("Please enter your message: ")  # Input message / maybe add support for entire text documents


    def rotateLetter(letter):  # Function to ensure that input text will output as english characters and not symbols
        numericLetter = ord(letter) - 97
        numericLetter += rotation
        numericLetter = numericLetter % 26
        numericLetter += 97
        encodedLetter = chr(numericLetter)
        return encodedLetter  # Output english characters only


    for lines in userMessage:
        lowerCaseLines = lines.lower()
        for letter in lowerCaseLines:

            isLetter = (ord(letter) >= 97) and (ord(letter) <= 122)

            if (isLetter):
                encodedLetter = rotateLetter(letter)
                print(encodedLetter, end='')
            else:
                print(letter, end='')

    print()
elif user_choice == 2:
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
elif user_choice == 3:
    print("------------------------------------------------------------------")
    print("| This program will reverse your message in order to encrypt it. |")
    print("------------------------------------------------------------------")
    input("Press enter to continue...")


    def reverse(user_message):
        str = ""
        for i in user_message:
            str = i + str
        return str


    user_message = input("Please enter your message to encrypt: ")

    print("The original string is : ", end="")
    print(user_message)

    print("The reversed string is : ", end="")
    print(reverse(user_message))


elif user_choice == 4:
    def A1Z26_encrypt(user_text):
        # Encrypt string by converting each letter to a number
        string = ""  # Placeholder variable
        user_text = user_text.lower()  # Format to Lowercase
        user_text = "".join(user_text.split())  # Remove spaces from string
        for x in range(0, len(user_text)):  # Loop through each character of string
            char = ord(user_text[x]) - 96  # Convert character to numeric 1 - 26
            if 0 < char <= 26: string += str(char) + " "  # Store value in 'string' variable
        return string  # Return cipher string


    def A1Z26():
        print("--------------------------------------------------")
        print("| A1Z26 Cipher : Encrypt user input into numbers |")
        print("--------------------------------------------------")
        input("Press enter to continue...")
        user_text = input("Please enter your message: ")
        print("\nThe starting string is:")
        print(user_text, "\n")
        print("The A1Z26 encrypted string is:")
        print(A1Z26_encrypt(user_text), "\n")


    A1Z26()
else:
    print("Please select one of the ciphers from above.")

