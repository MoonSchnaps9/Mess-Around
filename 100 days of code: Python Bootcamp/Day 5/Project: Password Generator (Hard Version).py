letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Hard version
# Once Easy version is completed, try the Hard version.
# the final password does not follow a pattern.
#Every time you generate a password, the position of the symbols, numbers, and letters are different.


#Trying to add random.shuffle to the easy version and work with one list only
import random

print("Welcome to the PyPassword Generator!")
user_number_letters = int(input("How many letters would you like in your password?\n"))
user_number_symbols = int(input("how many symbols would you like?\n"))
user_number_number = int(input("How many numbers would you like?\n"))

password_result = []

for letters1 in range(user_number_letters):
    password_result += random.choice(letters)
for symbols2 in range(user_number_symbols):
    password_result += random.choice(symbols)
for numbers3 in range(user_number_number):
    password_result += random.choice(numbers)

random.shuffle(password_result)
Final_password = "".join(password_result)
print("Your password is:" +" "+ Final_password)

#Alternative version (without .join)
# Final_password = ""
# for character in password_result:
#     Final_password += character
