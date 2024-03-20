import numpy as np

class ColumnarTransposition:
    @staticmethod
    def encrypt():
        def is_lowest(number, number_list):
            return number == min(number_list)

        letter_number = {"a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7", "h": "8", "i": "9",
                         "j": "10",
                         "k": "11", "l": "12", "m": "13", "n": "14", "o": "15", "p": "16", "q": "17", "r": "18",
                         "s": "19",
                         "t": "20", "u": "21", "v": "22", "w": "23", "x": "24", "y": "25", "z": "26"}

        # obtain the key and store the length of it
        key = input("Enter the encryption key: ") # ask user for encryption key
        # input validation
        while not key.isalpha():
            key = input("The key must only be letters (no spaces, numbers, or special characters): ")
        key_length = len(key)  # store length of key

        message = input("Enter the message you'd like to encrypt: ")

        columns = len(key)
        if len(message) == columns:
            rows = 1
        elif len(message) < columns:
            rows = 1
            while not columns % len(message) == 0:
                message += "x"
        elif len(message) > columns:
            while not len(message) % columns == 0:
                message += "x"
            rows = int((len(message) / columns))

        # initialize array based on key
        message_array = np.full((columns, rows), "empty")

        message_index = 0
        # populate array
        for x in range(rows):
            for y in range(columns):
                message_array[y][x] = message[message_index]
                message_index += 1

        # convert key to numbers
        numbered_key = []
        for letter in key:
            numbered_key.append(int(letter_number[letter]))

        numbered_key_temp = numbered_key

        coded_array = np.full(columns, "empty", dtype=object)
        for x in range(columns):
            index = numbered_key_temp.index(min(numbered_key))
            coded_array[x] = message_array[index]
            numbered_key_temp[index] = 100

        output = ""
        for x in range(len(coded_array)):
            output += str(coded_array[x]) + "-"
        output = output.replace("[", "").replace("]", "").replace("'", "")

        formatted_string = ""

        # formatting the string
        for index, x in enumerate(output):
            if x == " " and not output[index+1] == " ":
                formatted_string += ""
            elif x == "-" and index+1 == len(output):
                formatted_string += ""
            else:
                formatted_string += x

        formatted_string = formatted_string.replace("-", " ")

        print(formatted_string)

    @staticmethod
    def decrypt():
        letter_number = {"a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7", "h": "8", "i": "9",
                         "j": "10",
                         "k": "11", "l": "12", "m": "13", "n": "14", "o": "15", "p": "16", "q": "17", "r": "18",
                         "s": "19",
                         "t": "20", "u": "21", "v": "22", "w": "23", "x": "24", "y": "25", "z": "26"}

        key = input("Enter the key: ")
        message = input("Enter the message you'd like to decrypt: ")
        columns = 1
        rows = 0

        # determines columns
        for x in message:
            if x == " ":
                columns += 1

        # determines rows
        for x in message:
            if x == " ":
                break
            else:
                rows += 1

        message = message.replace(" ", "")

        # initialize array to fit columns and rows
        message_array = np.full((columns, rows), "empty")

        # populate array
        message_index = 0
        for x in range(columns):
            for y in range(rows):
                message_array[x][y] = message[message_index]
                message_index += 1

        # convert key to numbers
        numbered_key = []
        for letter in key:
            numbered_key.append(int(letter_number[letter]))

        # create new array tracking true order
        sorted_indices = np.argsort(numbered_key)

        ordered_message = np.full((columns, rows), "empty")
        for index, x in enumerate(sorted_indices):
            ordered_message[x] = message_array[index]

        deciphered_message = ""
        for x in range(rows):
            for y in range(columns):
                deciphered_message += ordered_message[y][x]

        deciphered_message = deciphered_message.upper()
        print(deciphered_message)
