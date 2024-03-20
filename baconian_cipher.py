import string
import random

# dictionary for encoding letters to uppercase
uppercase_positions = {
    'A': [],
    'B': [4],
    'C': [3],
    'D': [3, 4],
    'E': [2],
    'F': [2,4],
    'G': [2,3],
    'H': [2,3,4],
    'I': [1],
    'J': [1,4],
    'K': [1,3],
    'L': [1,3,4],
    'M': [1,2],
    'N': [1,2,4],
    'O': [1,2,3],
    'P': [1,2,3,4],
    'Q': [0],
    'R': [0,4],
    'S': [0,3],
    'T': [0,3,4],
    'U': [0,2],
    'V': [0,2,4],
    'W': [0,2,3],
    'X': [0,2,3,4],
    'Y': [0,1],
    'Z': [0,1,4],
    ' ': [0, 1, 3]
}

# dictionary for numbers to letters
num_to_letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
                 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W',
                 23: 'X', 24: 'Y', 25: 'Z', 26: ' '}

class BaconianCipher:
    @staticmethod
    def encrypt():
        coded_message_index = 0  # tracks the index of the coded message
        coded_message = input("Enter the message you'd like to encode: ")  # user input for coded message

        # input validation for coded_message
        while any(char in string.punctuation for char in coded_message) or any(char in string.digits for char in
                                                                               coded_message):
            coded_message = input("Coded message cannot contain special characters or numbers: ")

        coded_message = coded_message.upper()  # change message to all uppercase
        public_message = input("Enter the message you'd like to hide the coded message in: ")  # public message

        # input validation for public message
        while any(char in string.punctuation for char in public_message) or any(char in string.digits for char in
                                                                                public_message):
            public_message = input("Public message cannot contain special characters or numbers: ")

        # if public message is too few characters to encode coded_message, add random letters to meet length
        if len(public_message.replace(" ", "")) < len(coded_message) * 5:
            slack = (len(coded_message)*5) - len(public_message.replace(" ", ""))
            for x in range(slack):
                public_message += random.choice(string.ascii_letters)

        public_message = public_message.lower()  # initialize message as all lowercase for default binary as 0s
        string_holder = []  # list to hold five letters at a time for encoding
        cipher_text = ""  # initialize cipher_text to hold the cipher

        # loop through each letter in the public message
        for letter in public_message:
            if letter.isalpha():  # check if letter is alphabetic
                string_holder.append(letter)  # if it is, add it to the string_holder list

                if len(string_holder) >= 5:  # execute this code once we have five letters in string_holder
                    try:  # make the proper letters uppercase based on coded message
                        for x in uppercase_positions[coded_message[coded_message_index]]:
                            string_holder[x] = string_holder[x].upper()
                    except:  # break the loop if we are at the end of the list
                        break
                    for y in string_holder:  # add each coded letter to the cipher_text
                        cipher_text += y
                    string_holder = []  # reset string_holder to hold five new letters
                    try:  # increment the index of the coded message to code the next letter in it
                        coded_message_index += 1
                    except:  # if we are at the end of the list, break the loop
                        break

        # put spaces back into the public message
        for index, z in enumerate(public_message):
            if z == " ":
                cipher_text = cipher_text[:index] + " " + cipher_text[index:]

        # print the cipher text
        print(cipher_text)

    @staticmethod
    def decrypt():
        string_holder = []  # initialize string_holder to hold five letters for conversion to binary
        bin_numbers = ""  # empty string to hold all the binary numbers
        bin_numbers_convert = ""  # empty string to hold just five of the binary numbers for conversion
        plaintext = ""  # empty string to hold plaintext as we decrypt
        cipher_text = input("Enter the message you would like to decrypt: ")  # user input for cipher text

        # go through each letter in cipher text
        for letter in cipher_text:
            if letter.isalpha():  # if letter is alphabetic, add it to string_holder
                string_holder.append(letter)

            # execute this block of code when string_holder is holding five letters
            if len(string_holder) >= 5:
                # go through each letter in string_holder
                for x in string_holder:
                    if x.isupper():  # if letter is uppercase, it will equal 1
                        bin_numbers += "1"
                    elif x.islower():  # if letter is lowercase, it will equal 0
                        bin_numbers += "0"
                string_holder = []  # reset string_holder to hold five new letters

        # go through each binary number we've collected
        for num in bin_numbers:
            bin_numbers_convert += num  # add each number to bin_numbers_convert

            # execute this block when bin_numbers_convert has five binary numbers in it
            if len(bin_numbers_convert) >= 5:
                plaintext += num_to_letter[int(bin_numbers_convert, 2)]  # convert binary, to decimal, to letter
                bin_numbers_convert = ""  # reset bin_numbers_convert to hold five new binary numbers

        # print plaintext message
        print(plaintext)

