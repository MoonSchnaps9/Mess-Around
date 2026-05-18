#Resources
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#---------------------------------------------------------------------------------------------------------------------------------------------------------

#Caesar Cipher - Part 2

# 1: Create a function called decrypt() that takes original_text
# and shift_amount as inputs

# 2: Inside decrypt(), shift each letter backwards in the alphabet
# by shift_amount and print the decrypted text

# 3: Combine encrypt() and decrypt() into a single function called caesar()
# Use the direction variable to determine whether to encode or decode
# Call caesar() passing in direction, text, and shift

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