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

#------------------------------------------------------------------------------------------------------------------------------------------------
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

word_list = ["earth", "jupiter", "andromeda", "nebula", "moon", "asteroid", "galaxy"]

chosen_word = random.choice(word_list)

print(chosen_word)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"+" "

print(placeholder)

display = placeholder
correct_guess = []
lives = 6
game_on = True

while game_on:
    new_display = ""
    guess = input("Guess a letter:\n").lower()

    if  guess not in chosen_word:
        lives -= 1
        print(f"Wrong, you've lost 1 life. Remaining: {lives}")

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
         game_on = False
    elif lives == 0:
         print("Sorry, you lost!")
         game_on = False
