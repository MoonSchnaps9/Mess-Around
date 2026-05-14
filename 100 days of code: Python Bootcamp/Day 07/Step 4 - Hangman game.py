# "INSTRUCTIONS of Step 4"

#Part 1
# Create a variable called lives to keep track of the number of lives left. 
# Set lives to equal 6

#Part 2
# If guess is not a letter in the chosen_word, then reduce lives by 1
# If lives goes down to 0 then the game should end, and it should print " You loose "

# Part 3 
# print the ASCII art from the list stages that corresponds to the current number of lives the users has remaining

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
