# "INSTRUCTIONS of Step 2"

#Part 1
# Create an empty string called Placeholder
# For each letter in the chosen_world, add a _ to placeholder
# So if the chosen work is "apple", it should be _ _ _ _ _ with 5 "_" representing each letter to guess 
# Print out hint

#Part 2
# Create an empty string called display
# Loop through each letter in the chosen_world
# If the letter at that position matches guess then reveal that letter in the display at that position
# e.g if the user guessed "p" and the chosen word was "apple", then display should be _ P P _ _. 
# Print display and you should see the guessed letter in the correct position
# but every letter that is not a match is represented by "_"


import random

word_list = ["earth", "jupiter", "andromeda", "nebula", "moon", "asteroid", "galaxy"]

chosen_word = random.choice(word_list)

print(chosen_word)


guess = input("Guess a letter:\n").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")