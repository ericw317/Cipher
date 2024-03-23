from rotation_cipher import RotationCipher
from letter_to_number import LetterToNumber
from baconian_cipher import BaconianCipher
from columnar_transposition_cipher import ColumnarTransposition
from vigenere_cipher import VigenereCipher
from playfair_cipher import PlayfairCipher
from vernam_cipher import VernamCipher
from atbash_cipher import AtbashCipher
from rail_fence_cipher import RailFenceCipher

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
                          "1) Rotation\n"
                          "2) Letter To Number\n"
                          "3) Baconian Cipher\n"
                          "4) Columnar Transposition Cipher\n"
                          "5) Vigenere Cipher\n"
                          "6) Playfair Cipher\n"
                          "7) Vernam Cipher / OTP\n"
                          "8) Atbash Cipher\n"
                          "9) Rail Fence Cipher\n")
        # input validation
        while not selection.isnumeric() or selection < "1" or selection > "9":
            selection = input("Input must be a number between 1 and 9: ")
        if selection == "1":
            RotationCipher.encrypt()
        elif selection == "2":
            LetterToNumber.encrypt()
        elif selection == "3":
            BaconianCipher.encrypt()
        elif selection == "4":
            ColumnarTransposition.encrypt()
        elif selection == "5":
            VigenereCipher.encrypt()
        elif selection == "6":
            PlayfairCipher.encrypt()
        elif selection == "7":
            VernamCipher.encrypt()
        elif selection == "8":
            AtbashCipher.encrypt()
        elif selection == "9":
            RailFenceCipher.encrypt()

    elif decrypt:
        selection = input("Which cipher would you like to decrypt?\n"
                          "1) Rotation\n"
                          "2) Letter To Numer\n"
                          "3) Baconian Cipher\n"
                          "4) Columnar Transposition Cipher\n"
                          "5) Vigenere Cipher\n"
                          "6) Playfair Cipher\n"
                          "7) Vernam Cipher / OTP\n"
                          "8) Atbash Cipher\n"
                          "9) Rail Fence Cipher\n")

        # input validation
        while not selection.isnumeric() or selection < "1" or selection > "9":
            selection = input("Input must be a number between 1 and 9: ")
        if selection == "1":
            RotationCipher.decrypt()
        elif selection == "2":
            LetterToNumber.decrypt()
        elif selection == "3":
            BaconianCipher.decrypt()
        elif selection == "4":
            ColumnarTransposition.decrypt()
        elif selection == "5":
            VigenereCipher.decrypt()
        elif selection == "6":
            PlayfairCipher.decrypt()
        elif selection == "7":
            VernamCipher.decrypt()
        elif selection == "8":
            AtbashCipher.decrypt()
        elif selection == "9":
            RailFenceCipher.decrypt()
