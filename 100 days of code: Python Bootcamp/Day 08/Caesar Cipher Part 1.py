#Angela (Teacher) created this below for us

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#End of Angela's help

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1: Create a function called encrypt() that takes original_text 
# and shift_amount as inputs

# 2: Inside encrypt(), shift each letter forwards in the alphabet by shift_amount and print the encrypted text
# Use index() to find the position of a letter in the alphabet list
# e.g. plain_text = "hello", shift_amount = 1 → "ifmmp"
# Output format: "Here is the encoded result: ifmmp"

def encrypt(original_text=text, shift_amount=shift):
    
    encrypted_message = ""
    
    for letter in text:
        position_in_alphabet_list = alphabet.index(letter)
        position_in_alphabet_list_with_shift = position_in_alphabet_list + shift
        final_position = position_in_alphabet_list_with_shift % 26
        encrypted_message += alphabet[final_position]
    print(f"Here is the encoded result: {encrypted_message}")

encrypt()