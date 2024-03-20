import string

class VigenereCipher:
    @staticmethod
    def encrypt():
        # initialize variables needed later on
        key_index = 0
        cipher_text = ""

        # retrieve plaintext and key
        plaintext = input("Enter the message you'd like to encrypt: ")
        plaintext = plaintext.lower()
        key = input("Enter the key you want to use: ")

        # input validation
        while not key.isalpha():
            key = input("The key must consist only of letters. Try again.\n")

        # loop through each character of plaintext
        for char in plaintext:
            if char.isalpha():  # if character is alphabetic, perform encryption on it
                char_value = string.ascii_letters.index(char)  # retrieve number value of current character
                try:  # try to grab the current value of the key
                    key_value = string.ascii_letters.index(key[key_index])
                except:  # if the key has been looped through already, reset the key index and start again
                    key_index = 0
                    key_value = string.ascii_letters.index(key[key_index])

                # add key_value to char_value and concatenate it to the cipher_text
                cipher_text += string.ascii_letters[char_value + key_value]

                key_index += 1
            else:  # if character is not alphabetic, simply add the character to the cipher_text string
                cipher_text += char

        print(cipher_text.lower())  # output the cipher_text

    @staticmethod
    def decrypt():
        # initialize variables needed later on
        key_index = 0
        plaintext = ""

        # retrieve cipher_text and key
        cipher_text = input("Enter the message you'd like to decrypt: ")
        cipher_text = cipher_text.lower()
        key = input("Enter the key: ")

        # input validation
        while not key.isalpha():
            key = input("The key must consist only of letters. Try again.\n")

        # loop through each character of cipher_text
        for char in cipher_text:
            if char.isalpha():  # if character is alphabetic, perform decryption on it
                char_value = string.ascii_letters.index(char)  # retrieve number value of current character
                try:  # try to grab the current value of the key
                    key_value = string.ascii_letters.index(key[key_index])
                except:  # if the key has been looped through already, reset the key index and start again
                    key_index = 0
                    key_value = string.ascii_letters.index(key[key_index])

                # subtract key_value from char_value and concatenate it to the plaintext
                plaintext += string.ascii_letters[char_value - key_value]

                key_index += 1
            else:  # if character is not alphabetic, simply add the character to the plaintext string
                plaintext += char

        print(plaintext.lower())  # output the plaintext
