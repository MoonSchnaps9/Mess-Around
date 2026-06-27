# "INSTRUCTIONS of Step 5"

#Part 1
#Update the word list to use the word_list from hangman_words.py

#Part 2
#Update the code to use the stages from hangman_art.py

#Part 3
#Import the logo from hangman_art.py and print it at the start of the game

#Part 4
#If the user has entered a letter they've already guessed, print the letter and let them know
#We should not deduct a life for this.

#Part 5
#If the letter is not in the chosen_word, print out the letter and let them know it's not in the word. 

#Part 6
#Update the code to tell users how many lives they have left

#Extra - Beyond Angela's instructions - ClaudeAI
#   (wrong guess tracking)
# Create a variable called wrong_guess as an empty list
# If the user guesses a letter that is not in the chosen_word AND not already in wrong_guess:
# Deduct a life and add the letter to wrong_guess
# If the letter IS already in wrong_guess, warn the user but do NOT deduct a life
#------------------------------------------------------------------------------------------------------------------------------------------------
import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

chosen_word = random.choice(word_list)

print(logo)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"+" "

print(placeholder)

display = placeholder
correct_guess = []
wrong_guess =[]
lives = 6
game_on = True

while game_on:
    new_display = ""
    guess = input("Guess a letter:\n").lower()

    if guess in wrong_guess:
         print(f"Be careful, you have already tried '{guess}', and this is wrong!")

    if guess not in chosen_word:
        if guess not in wrong_guess:
            lives -= 1
            wrong_guess.append(guess)
            print(f" '{guess}' is not in the word, sorry :(")
            print(f"Wrong, you've lost 1 life. Remaining: {lives}")

    if guess in correct_guess:
         print(f"Well, you have already guessed '{guess}!\nTry another one! :)")

    for letter in chosen_word:
        if letter == guess:
                correct_guess.append(letter)
                new_display += letter+" "
        elif letter in correct_guess:
                new_display += letter+" "
        else:
            new_display += "_"+" "
    display = new_display
    
    print(display)
    print(f"{stages[lives]}")

    if "_" not in display:
         print("Congrats, you won!")
         print(f"It was {chosen_word}")
         game_on = False
    elif lives == 0:
         print("Sorry, you lost!")
         print(f"It was {chosen_word}")
         game_on = False