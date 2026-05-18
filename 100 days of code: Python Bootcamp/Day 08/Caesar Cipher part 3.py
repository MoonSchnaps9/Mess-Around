#Part 3

# 1: Import and print the logo from art.py at the start of the program

# 2: Fix the code so that numbers, symbols, and spaces are kept unchanged
# when encoding or decoding
# e.g. "meet me at 3!" → "XXXX XX XX 3!" (spaces, numbers, symbols stay as-is)

# 3: Add a loop that asks the user if they want to go again
# If "yes" → ask for direction, text, and shift again and run caesar()
# If "no" → end the program

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#Import logo of the game
from art import logo
print(logo)

#Alphabet list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Decrypt function
def decrypt(original_text, shift_amount):
    decrypted_message = ""

    for letter in original_text:
        if letter not in alphabet:
            decrypted_message += letter
        else:
            position_in_alphabet_list = alphabet.index(letter)
            position_in_alphabet_list_with_shift = position_in_alphabet_list - shift_amount
            final_position = position_in_alphabet_list_with_shift % 26
            decrypted_message += alphabet[final_position]
    print(f"Here is the decoded result: {decrypted_message}")

#Encrypt function
def encrypt(original_text, shift_amount):
    
    encrypted_message = ""
    for letter in original_text:
        if letter not in alphabet:
            encrypted_message += letter
        else:
            position_in_alphabet_list = alphabet.index(letter)
            position_in_alphabet_list_with_shift = position_in_alphabet_list + shift_amount
            final_position = position_in_alphabet_list_with_shift % 26
            encrypted_message += alphabet[final_position]
    print(f"Here is the encoded result: {encrypted_message}")

#Main Function - Game menu
def caesear():
    game = True
    while game:
        user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
        original_text = input("Type your message:\n").lower()
        shift_amount = int(input("Type the shift number:\n"))
        if user_choice == "encode":
            encrypt(original_text, shift_amount)
        elif user_choice == "decode":
            decrypt(original_text, shift_amount)
        else:
            print(f"Try again and ensure to write 'encode' or 'decode' properly please :)")

        user_choice = input("Do you want to go again? (Yes or No)\n").lower()
        if user_choice == "no":
            print("Thank you and have a great day!")
            game = False


#Calling main function to run the game
caesear()