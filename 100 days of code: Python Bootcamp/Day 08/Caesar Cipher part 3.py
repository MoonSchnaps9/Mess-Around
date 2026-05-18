#Resources
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#---------------------------------------------------------------------------------------------------------------------------------------------------------

#Part 3

# 1: Import and print the logo from art.py at the start of the program

# 2: Fix the code so that numbers, symbols, and spaces are kept unchanged
# when encoding or decoding
# e.g. "meet me at 3!" → "XXXX XX XX 3!" (spaces, numbers, symbols stay as-is)

# 3: Add a loop that asks the user if they want to go again
# If "yes" → ask for direction, text, and shift again and run caesar()
# If "no" → end the program

#---------------------------------------------------------------------------------------------------------------------------------------------------------


def decrypt(original_text=text, shift_amount=shift):
    decrypted_message = ""

    for letter in text:
        position_in_alphabet_list = alphabet.index(letter)
        position_in_alphabet_list_with_shift = position_in_alphabet_list - shift
        final_position = position_in_alphabet_list_with_shift % 26
        decrypted_message += alphabet[final_position]
    print(f"Here is the decoded result: {decrypted_message}")


def encrypt(original_text=text, shift_amount=shift):
    
    encrypted_message = ""
    
    for letter in text:
        position_in_alphabet_list = alphabet.index(letter)
        position_in_alphabet_list_with_shift = position_in_alphabet_list + shift
        final_position = position_in_alphabet_list_with_shift % 26
        encrypted_message += alphabet[final_position]
    print(f"Here is the encoded result: {encrypted_message}")


def caesear(user_choice = direction, original_text = text, shift_amount = shift):
    if direction == "encode":
        encrypt()
    elif direction == "decode":
        decrypt()
    else:
        print(f"Try again and ensure to write 'encode' or 'decode' properly please :)")

caesear()