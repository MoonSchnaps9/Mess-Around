# Exercise 2: Dice Roller
# Write a program that:

# Asks the user how many dice they want to roll
# Asks how many sides each die has
# Rolls each die randomly and prints each result
# Prints the total at the end

# Example output:
# Roll 1: 4
# Roll 2: 2
# Roll 3: 6
# Total: 12
# Go.

import random

number_of_dice_to_roll = int(input("How many dice do you want to roll?\n"))
number_of_side_dice_has = int(input("How many sides each die has?\n"))
total = 0

for result in range(number_of_dice_to_roll):
    roll_result = random.randint(1, number_of_side_dice_has)
    print(f"Roll {result + 1}: {roll_result}")
    total += roll_result

print(f"Total: {total}")

#We could also do

# for result in range(1, number_of_dice_to_roll +1):
#     roll_result = random.randint(1, number_of_side_dice_has)
#     print(f"Roll {result}: {roll_result}")
#     total += roll_result