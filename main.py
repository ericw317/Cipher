import string

########################################################################################################################

# Function for encrypting a rotation cypher
def rotationEncrypt():
    # Takes input for the number of rotations
    rotationNum = input("Enter the number of letters you'd like to rotate: ")

    # Input validation
    while not rotationNum.isnumeric() or rotationNum < "1" or rotationNum > "25":
        rotationNum = input("Input must be a number between 1-25: ")

    # Convert rotationNum to integer
    rotationNum = int(rotationNum)

    # Takes input for message to be encrypted
    message = input("Enter the message you would like to encrypt in ROT-" + str(rotationNum) + ": ")

    message = message.lower()

    #Encrypt message

    #Create variable to store the encrypted message
    cipher = ""

    #Loop through each character in message, rotating the character if it is an ascii letter
    for x in message:
        if x in string.ascii_letters:
            i = 0
            while x != string.ascii_letters[i]:
                i += 1
            cipher = cipher + string.ascii_letters[i + rotationNum]
        else:
            cipher = cipher + x

    # Print encrypted message
    print(cipher.lower())

########################################################################################################################

# Function for decrypting a rotation cypher
def rotationDecrypt():
    # Takes input for the number of rotations
    rotationNum = input("Enter the ROT number you'd like to decrypt (Enter '0' to decrypt all): ")

    # Input validation
    while not rotationNum.isnumeric() or int(rotationNum) < 0 or int(rotationNum) > 25:
        rotationNum = input("Input must be a number between 1-25: ")

    # Convert rotationNum to integer
    rotationNum = int(rotationNum)

    # Takes input for message to be encrypted
    message = input("Enter the message you would like to decrypt in ROT-" + str(rotationNum) + ": ")

    # convert message to app uppercase
    message = message.upper()

    # Decrypt message

    # Create variable to store the decrypted message
    cipher = ""

    # Show every rotation
    if rotationNum == 0:
        counter = 26
        for x in range(25, 0, -1):
            for y in message:
                if y in string.ascii_letters:
                    i = 51
                    while y != string.ascii_letters[i]:
                        i -= 1
                    cipher = cipher + string.ascii_letters[i - x]
                else:
                    cipher = cipher + y
            counter -= 1
            print(str(counter) + ") " + cipher.lower())
            cipher = ""

    # Loop through each character in message, rotating the character if it is an ascii letter
    for x in message:
        if x in string.ascii_letters:
            i = 51
            while x != string.ascii_letters[i]:
                i -= 1
            cipher = cipher + string.ascii_letters[i - rotationNum]
        else:
            cipher = cipher + x

    # Print encrypted message
    print(cipher.lower())

########################################################################################################################

program = True

while program:
    # boolean operators to decide whether program will encrypt or decrypt
    encrypt = False
    decrypt = False

    # Selection Screen
    print("Would you like to encrypt or decrypt a message?")
    print("1) Encrypt\n"
          "2) Decrypt\n"
          "0) Exit")

    encryptOrDecrypt = input()

    # Input validation
    while not encryptOrDecrypt.isnumeric() or encryptOrDecrypt < "0" or encryptOrDecrypt > "2":
        encryptOrDecrypt = input("Input must be a number between 1-2: ")

    if encryptOrDecrypt == "1":
        encrypt = True
    elif encryptOrDecrypt == "2":
        decrypt = True
    else:
        program = False

    if encrypt:
        selection = input("Which cipher would you like to encrypt with?\n"
                          "1) Rotation\n")
        # input validation
        while not selection.isnumeric() or selection < "1" or selection > "1":
            selection = input("Input must be a number: ")
        if selection == "1":
            rotationEncrypt()
    elif decrypt:
        selection = input("Which cipher would you like to decrypt?\n"
                          "1) Rotation\n")
        # input validation
        while not selection.isnumeric() or selection < "1" or selection > "1":
            selection = input("Input must be a number: ")
        if selection == "1":
            rotationDecrypt()
