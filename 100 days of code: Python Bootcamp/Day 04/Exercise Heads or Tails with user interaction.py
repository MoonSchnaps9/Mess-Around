#Heads or Tails
# Create a coin flip program using what you have learnt about
# randomisation in Python. It should randomly print "Heads" or
# "Tails" every time it is run.

import random

user_choice = input("Face your fate: Heads or Tails? ").lower()

coin_result = random.randint(1,2)

if coin_result == 1:
    coin_result = "heads"
else:
    coin_result = "tails"

if user_choice == coin_result:
    print(coin_result)
    print("You win!")
else:
    print(coin_result)
    print("You lose, sorry :/")
    