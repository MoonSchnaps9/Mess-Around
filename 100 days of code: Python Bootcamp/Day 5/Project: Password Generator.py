letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Easy version
#Generate the password in sequence. Letters then symbols, then numbers. If the user wants:
# 4 letters, 2 symbols, and 3 numbers then the password might look like this:
#fgdx$*924
#Each category is together. Go
#Import random thingy
import random

print("Welcome to the PyPassword Generator!")
user_number_letters = int(input("How many letters would you like in your password?\n"))
user_number_symbols = int(input("how many symbols would you like?\n"))
user_number_number = int(input("How many numbers would you like?\n"))

letters_results = ""
symbols_results = ""
number_results = ""

for letters1 in range(user_number_letters):
    letters_results += random.choice(letters)
for symbols2 in range(user_number_symbols):
    symbols_results += random.choice(symbols)
for numbers3 in range(user_number_number):
    number_results += random.choice(numbers)

print("Your passsord is: "+letters_results+symbols_results+number_results)

