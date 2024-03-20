class LetterToNumber:
    @staticmethod
    # Function for Letter to Number encryption
    def encrypt():
        # Variables
        encryptedMessage = ""  # Variable to hold encrypted message

        # Take user input for message to encrypt
        message = input("Enter the message you'd like to encrypt: ")

        # Make message lowercase
        message = message.lower()

        # Dictionary to hold values
        cipherKey = {"a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7", "h": "8", "i": "9",
                     "j": "10",
                     "k": "11", "l": "12", "m": "13", "n": "14", "o": "15", "p": "16", "q": "17", "r": "18", "s": "19",
                     "t": "20", "u": "21", "v": "22", "w": "23", "x": "24", "y": "25", "z": "26"}

        # Go through each character in message converting characters to numbers, if applicable
        for x in message:
            if x in cipherKey:
                print(cipherKey[x], end=' ')
            elif x == ' ':
                print(" ", end='')
            else:
                print(x, end='')

        print("")

    @staticmethod
    # Function for Letter To Number decryption
    def decrypt():
        # Variables
        encryptedMessage = ""  # Variable to hold encrypted message
        tempMessage = ""  # Variable to hold temp

        # Take user input for message to encrypt
        message = str(input("Enter the message you'd like to decrypt: "))

        # Make message lowercase and add space at the end
        message = message.lower()
        message += ' '

        # Dictionary to hold values
        cipherKey = {"1": "a", "2": "b", "3": "c", "4": "d", "5": "e", "6": "f", "7": "g", "8": "h", "9": "i",
                     "10": "j",
                     "11": "k", "12": "l", "13": "m", "14": "n", "15": "o", "16": "p", "17": "q", "18": "r", "19": "s",
                     "20": "t", "21": "u", "22": "v", "23": "w", "24": "x", "25": "y", "26": "z"}

        # Loop through, converting each number to its corresponding letter
        for index, x in enumerate(message):
            if x != ' ':  # if current char is not a space, then add it to the temp string
                tempMessage += x
            else:
                if tempMessage in cipherKey:
                    print(cipherKey[tempMessage], end='')  # convert temp string to corresponding character
                    tempMessage = ''  # reset the temp string

                    try:
                        if message[index + 1] == ' ':  # if there are 2 consecutive spaces, print a space
                            print(' ', end='')
                    except IndexError:  # if we're at the end of the string, do nothing
                        print('')

        print("")
