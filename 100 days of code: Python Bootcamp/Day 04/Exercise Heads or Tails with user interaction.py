#Heads or Tails
# Create a coin flip program using what you have learnt about
# randomisation in Python. It should randomly print "Heads" or
# "Tails" every time it is run.

import random

user_choice = input("Face your fate: Heads or Tails? ").lower()

random_number_result = random.randint(1,2)
heads = 1
tails = 2

if heads == random_number_result and user_choice == "heads":
    print("Heads!\nYou win!")
elif tails == random_number_result and user_choice == "tails":
    print("Tails!\nYou win!")
else:
    print("You lose, sorry :/")
    