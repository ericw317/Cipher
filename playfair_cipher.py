import string

class PlayfairCipher:
    @staticmethod
    def encrypt():
        def print_array(array_2d):
            for row in array_2d:
                print(' '.join(map(str, row)))

        def row_index(key_grid, char):
            for i, row in enumerate(key_grid):
                if char in row:
                    return i  # Return the row index where char is found
            return None  # Return None if char is not found

        def col_index(key_grid, char):
            for row in key_grid:
                if char in row:
                    return row.index(char)  # Return the column index where char is found
            return None  # Return None if char is not found

        # obtain key and plaintext
        key = input("Enter the key: ")
        # input validation
        while not key.isalpha():
            key = input("Key must only consists of letters: ")

        plaintext = input("Enter the plaintext: ")
        # input validation
        while not plaintext.replace(" ", "").isalpha():
            plaintext = input("This encryption can only encrypt letters. Try again: ")

        # formatting the plaintext
        # remove all spaces
        plaintext = plaintext.replace(" ", "")

        # adding a bogus character between sets of repeating characters
        index_holder = ""
        for index, char in enumerate(plaintext):
            if index < len(plaintext) - 1:
                if char == plaintext[index + 1]:
                    index_holder += str(index + 1)
        for index, x in enumerate(index_holder):
            plaintext = plaintext[:int(x) + index] + "x" + plaintext[int(x) + index:]

        # add a bogus character to plaintext if the length is uneven
        if len(plaintext) % 2 != 0:
            plaintext += "x"

        # initialize 5x5 array
        key_grid = [["0" for _ in range(5)] for _ in range(5)]

        # populate array with key
        key_counter = 0
        for x in range(5):
            for y in range(5):
                # check if plaintext_counter is less than plaintext length to prevent out of bounds error
                if key_counter < len(key):
                    no_repeat = False  # set this to false, so we can start the checking loop
                    # loop will run as long as any repetition of characters is detected
                    while not no_repeat and key_counter < len(key):
                        # go through every row in the grid searching for repeating characters
                        for row in key_grid:
                            # if repetition is found, increment plaintext_counter and repeat the loop
                            if key[key_counter] in row:
                                no_repeat = False
                                key_counter += 1
                                break
                            # if no repetition are found, exit entire while loop
                            else:
                                no_repeat = True
                    # if plaint_text counter is still in bounds and passes previous check, add it to the grid
                    if key_counter < len(key):
                        key_grid[x][y] = key[key_counter]
                        key_counter += 1

        # populate remainder of array with letters
        letters = string.ascii_letters  # letters we will use
        letters_counter = 0  # counter to increment for cycling through letters
        repeat = True  # setting this true for the while loop located later on
        # loop through each element in the array
        for x in range(5):
            for y in range(5):
                # check if letter exists in grid or is a 'j', if neither of these are true, we mark it for adding
                while repeat:
                    for row in key_grid:
                        if letters[letters_counter] in row or letters[letters_counter] == "j":
                            repeat = True
                            letters_counter += 1
                            break
                        else:
                            repeat = False
                            character_add = letters[letters_counter]
                # if the grid element is empty, we add the character then set repeat to true to loop again
                if key_grid[x][y] == "0":
                    key_grid[x][y] = character_add
                    repeat = True

        # encrypt message
        cipher_text = ""
        pos_1 = ""
        pos_2 = ""
        for index, char in enumerate(plaintext):
            if index % 2 == 0:
                pos_1_row = row_index(key_grid, char)
                pos_1_col = col_index(key_grid, char)
            elif not index %2 == 0:
                pos_2_row = row_index(key_grid, char)
                pos_2_col = col_index(key_grid, char)
                if pos_1_row == pos_2_row:
                    try:
                        new_char_1 = key_grid[pos_1_row][pos_1_col + 1]
                    except:
                        new_char_1 = key_grid[pos_1_row][0]
                    try:
                        new_char_2 = key_grid[pos_2_row][pos_2_col + 1]
                    except:
                        new_char_2 = key_grid[pos_2_row][0]
                    cipher_text += new_char_1 + new_char_2 + " "
                elif pos_1_col == pos_2_col:
                    try:
                        new_char_1 = key_grid[pos_1_row + 1][pos_1_col]
                    except:
                        new_char_1 = key_grid[0][pos_1_col]
                    try:
                        new_char_2 = key_grid[pos_2_row + 1][pos_2_col]
                    except:
                        new_char_2 = key_grid[0][pos_2_col]
                    cipher_text += new_char_1 + new_char_2 + " "
                else:
                    new_char_1 = key_grid[pos_1_row][pos_2_col]
                    new_char_2 = key_grid[pos_2_row][pos_1_col]

                    cipher_text += new_char_1 + new_char_2 + " "
        print(cipher_text)

    @staticmethod
    def decrypt():
        def print_array(array_2d):
            for row in array_2d:
                print(' '.join(map(str, row)))

        def row_index(key_grid, char):
            for i, row in enumerate(key_grid):
                if char in row:
                    return i  # Return the row index where char is found
            return None  # Return None if char is not found

        def col_index(key_grid, char):
            for row in key_grid:
                if char in row:
                    return row.index(char)  # Return the column index where char is found
            return None  # Return None if char is not found

        # obtain key and cipher_text
        key = input("Enter the key: ")
        # input validation
        while not key.isalpha():
            key = input("Key must only consists of letters: ")

        cipher_text = input("Enter the ciphertext: ")
        # input validation
        while not cipher_text.replace(" ", "").isalpha():
            cipher_text = input("This encryption can only encrypt letters. Try again: ")

        # formatting the cipher_text
        # remove all spaces
        cipher_text = cipher_text.replace(" ", "")

        # initialize 5x5 array
        key_grid = [["0" for _ in range(5)] for _ in range(5)]

        # populate array with key
        key_counter = 0
        for x in range(5):
            for y in range(5):
                # check if plaintext_counter is less than plaintext length to prevent out of bounds error
                if key_counter < len(key):
                    no_repeat = False  # set this to false, so we can start the checking loop
                    # loop will run as long as any repetition of characters is detected
                    while not no_repeat and key_counter < len(key):
                        # go through every row in the grid searching for repeating characters
                        for row in key_grid:
                            # if repetition is found, increment plaintext_counter and repeat the loop
                            if key[key_counter] in row:
                                no_repeat = False
                                key_counter += 1
                                break
                            # if no repetition are found, exit entire while loop
                            else:
                                no_repeat = True
                    # if plaint_text counter is still in bounds and passes previous check, add it to the grid
                    if key_counter < len(key):
                        key_grid[x][y] = key[key_counter]
                        key_counter += 1

        # populate remainder of array with letters
        letters = string.ascii_letters  # letters we will use
        letters_counter = 0  # counter to increment for cycling through letters
        repeat = True  # setting this true for the while loop located later on
        # loop through each element in the array
        for x in range(5):
            for y in range(5):
                # check if letter exists in grid or is a 'j', if neither of these are true, we mark it for adding
                while repeat:
                    for row in key_grid:
                        if letters[letters_counter] in row or letters[letters_counter] == "j":
                            repeat = True
                            letters_counter += 1
                            break
                        else:
                            repeat = False
                            character_add = letters[letters_counter]
                # if the grid element is empty, we add the character then set repeat to true to loop again
                if key_grid[x][y] == "0":
                    key_grid[x][y] = character_add
                    repeat = True

        # encrypt message
        plaintext = ""
        pos_1 = ""
        pos_2 = ""
        for index, char in enumerate(cipher_text):
            if index % 2 == 0:
                pos_1_row = row_index(key_grid, char)
                pos_1_col = col_index(key_grid, char)
            elif not index %2 == 0:
                pos_2_row = row_index(key_grid, char)
                pos_2_col = col_index(key_grid, char)
                if pos_1_row == pos_2_row:
                    try:
                        new_char_1 = key_grid[pos_1_row][pos_1_col - 1]
                    except:
                        new_char_1 = key_grid[pos_1_row][4]
                    try:
                        new_char_2 = key_grid[pos_2_row][pos_2_col - 1]
                    except:
                        new_char_2 = key_grid[pos_2_row][4]
                    plaintext += new_char_1 + new_char_2 + " "
                elif pos_1_col == pos_2_col:
                    try:
                        new_char_1 = key_grid[pos_1_row - 1][pos_1_col]
                    except:
                        new_char_1 = key_grid[4][pos_1_col]
                    try:
                        new_char_2 = key_grid[pos_2_row - 1][pos_2_col]
                    except:
                        new_char_2 = key_grid[4][pos_2_col]
                    plaintext += new_char_1 + new_char_2 + " "
                else:
                    new_char_1 = key_grid[pos_1_row][pos_2_col]
                    new_char_2 = key_grid[pos_2_row][pos_1_col]

                    plaintext += new_char_1 + new_char_2 + " "

        plaintext = plaintext.replace(" ", "")
        print(plaintext)
