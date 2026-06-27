# "INSTRUCTIONS"
#1 Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it
#2 Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
#3 Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is, "Wrong" if it's not
#-----------------------------------------------------------------------------------------------------------------------------------------


#1 import Random + create list + choose a random word + display it

import random

word_list = ["earth", "jupiter", "andromeda", "nebula", "moon", "asteroid", "galaxy"]

chosen_word = random.choice(word_list)

print(chosen_word)


guess = input("Guess a letter:\n").lower()

#ClaudeAI helped me understand how For In technically work depending on what the variable contains:
#If the variable contains a list -> Word by Word | If it contains numbers -> number by number | if it contains a word -> letter by letter
#I was a bit stuck as I didn't think that for loop would go letter by letter

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")