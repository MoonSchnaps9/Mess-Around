# Rock Paper Scissors - Day 4 Project
# Build a Rock, Paper, Scissors game using randomisation and lists.

#I'll start by building the foundations
import random

rock = '''   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#I create a list to represent the possibilities. This should be useful for the random function later on
list_of_possibilities = [rock, paper, scissors]

#I create the random fuction
computer_choice = random.choice(list_of_possibilities)

#I create the user input + assign its value to the correct variable

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice == 0:
    user_choice = rock
elif user_choice == 1:
    user_choice = paper
elif user_choice == 2:
    user_choice = scissors
else:
    print("Dear human, could you please ensure that you respect the rules.. type your answer correctly geez :D")

#Now, the final part = Print user choice against computer choice, and decide who wins

print(user_choice)
print("Computer chose:\n" + computer_choice)

#Draw case
if user_choice == computer_choice:
    print("This is a draw.. the pressure is intense")

#Rock Case
elif user_choice == rock and computer_choice == scissors:
    print("You win!")
elif user_choice == rock and computer_choice == paper:
    print("You lose")

#Paper case
elif user_choice == paper and computer_choice == rock:
    print("You win!")
elif user_choice == paper and computer_choice == scissors:
    print("You lose!")

#Scissors case
elif user_choice == scissors and computer_choice == paper:
    print("You win!")
elif user_choice == scissors and computer_choice == rock:
    print("You lose!")

