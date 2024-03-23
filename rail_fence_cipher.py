class RailFenceCipher:
    @staticmethod
    def encrypt():
        rails = input("Enter the number of rails you want to encrypt with: ")  # get number of rails

        # input validations
        while not rails.isnumeric() or int(rails) <= 0:
            rails = input("Must be a number greater than 0.")

        rails = int(rails)  # convert rails to integer
        plaintext = input("Enter the plaintext you'd like to encrypt: ")  # get plaintext
        rail_array = [[] for _ in range(rails)]  # initialize rail array

        rail_counter = 0  # initialize rail counter to keep track of which rail we are writing to
        forward = True  # boolean to tell us if we are moving forward in the rails or backward

        # loop through plaintext, writing each character to proper position in rail array
        for char in plaintext:
            if forward:
                rail_array[rail_counter].append(char)
                rail_counter += 1
                if rail_counter == rails - 1:
                    forward = False
            else:
                rail_array[rail_counter].append(char)
                rail_counter -= 1
                if rail_counter == 0:
                    forward = True

        print("Ciphertext: ", end="")

        # read from each array to output ciphertext
        for x in range(len(rail_array)):
            for y in range(len(rail_array[x])):
                print(rail_array[x][y], end="")

        print()

    @staticmethod
    def decrypt():
        rails = input("Enter the number of rails the ciphertext uses: ")  # take number of rails

        # input validation
        while not rails.isnumeric() or int(rails) <= 0:
            rails = input("Must be a number greater than 0.")

        rails = int(rails)  # convert rails to integer
        ciphertext = input("Enter the ciphertext you want to decrypt: ")  # take ciphertext
        ciphertext_sim = []  # initialize array to holder simulation values
        rail_array_sim = [[] for _ in range(rails)]  # initialize rail array
        rail_array = [[] for _ in range(rails)]  # initialize simulation array

        # simulate rail array layout order
        rail_counter = 0
        forward = True
        for x in range(len(ciphertext)):
            if forward:
                rail_array_sim[rail_counter].append(x)
                rail_counter += 1
                if rail_counter == rails - 1:
                    forward = False
            else:
                rail_array_sim[rail_counter].append(x)
                rail_counter -= 1
                if rail_counter == 0:
                    forward = True

        # simulate ciphertext
        for x in range(len(rail_array_sim)):
            for y in range(len(rail_array_sim[x])):
                ciphertext_sim.append(str(rail_array_sim[x][y]))

        print("Plaintext: ", end="")

        # use simulation ciphertext to output the correct order of the real ciphertext
        for x in range(len(ciphertext)):
            print(ciphertext[ciphertext_sim.index(str(x))], end="")

        print()
