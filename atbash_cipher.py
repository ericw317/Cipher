import string

class AtbashCipher:
    @staticmethod
    def encrypt():
        alphabet_lower = string.ascii_lowercase  # set variable with lowercase alphabet
        alphabet_upper = string.ascii_uppercase  # set variable with uppercase alphabet
        plaintext = input("Enter the message you'd like to encrypt: ")  # ask user for input

        # loop through each character in plaintext, outputting opposite alphabet character
        for char in plaintext:
            if char.islower():  # handle lowercase characters
                print(alphabet_lower[25 - alphabet_lower.index(char)], end="")
            elif char.isupper():  # handle uppercase characters
                print(alphabet_upper[25 - alphabet_upper.index(char)], end="")
            else:  # any non-alphabetic character will be output as is
                print(char, end="")
        print()

    @staticmethod
    def decrypt():
        alphabet_lower = string.ascii_lowercase  # set variable with lowercase alphabet
        alphabet_upper = string.ascii_uppercase  # set variable with uppercase alphabet
        ciphertext = input("Enter the ciphertext you'd like to decrypt: ")  # ask user for input

        # loop through each character in cipher, outputting opposite alphabet character
        for char in ciphertext:
            if char.islower():  # handle lowercase characters
                print(alphabet_lower[25 - alphabet_lower.index(char)], end="")
            elif char.isupper():  # handle uppercase characters
                print(alphabet_upper[25 - alphabet_upper.index(char)], end="")
            else:  # any non-alphabetic character will be output as is
                print(char, end="")
        print()
