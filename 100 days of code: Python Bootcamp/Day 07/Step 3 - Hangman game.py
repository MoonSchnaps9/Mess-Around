# "INSTRUCTIONS of Step 3"

#Part 1
# Use a while loop to let the user guess again
#The loop should only stop once the user has guessed all the letters in the chosen_world
#At that point Display has no more blanks (_). Then you can tell the user they've won

#Part 2
# Update the for loop that the previous guesses are added to the display string
# At the moment, when user makes a new guess, the previous guess gets replaced by a _. We need to fix that by updating the for loop

#------------------------------------------------------------------------------------------------------------------------------------------------

import random

word_list = ["earth", "jupiter", "andromeda", "nebula", "moon", "asteroid", "galaxy"]

chosen_word = random.choice(word_list)

print(chosen_word)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"+" "

print(placeholder)

guess = input("Guess a letter:\n").lower()

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter+" "
    else:
        display += "_"+" "

print(display)
