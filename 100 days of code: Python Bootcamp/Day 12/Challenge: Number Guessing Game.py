#Challenge: Number Guessing Game

#User needs to guess a number between 1 and 100
#2 levels of difficulty: Easy (10 attempts) and Hard (5 attempts)

#----------------------------------------------------------------
from art import logo
import random

def computer_picks_number():
    computer_number = random.randint(1,100)
    return computer_number

def welcome_message(logo):
    print(logo)
    print("Welcome to the Quantum Edition of 'Guess my Celestial number' 🌌 ")
    print("I am thinking hard to find a number between 1 and 100 to satisfy Uranus 🙃 ")
    difficulty = input("Time to play! Choose a cosmic difficulty: 'Easy' or 'Hard'?\n").lower()
    return difficulty

def easy_mode(computer_number):
    attempt = 10
    game = True
    while game:
        
        print(f"You have {attempt} remaining attempts to guess that number for Uranus! 👊")
        guess = int(input("Make a cosmic guess:\n"))

        if guess == computer_number:
            print("Geeez, you managed! Uranus is very happy 😊")
            game = False
        
        elif guess != computer_number:
            
            if guess > computer_number:
                attempt -= 1
                if attempt == 0:
                    print("You have exhausted all of your attempts.. Uranus is not satisfied..\n There is worst in life, don't worry 🤷‍♂️")
                    game = False
                else:
                    print("This is too high. Keep trying! 🤔")
            
            elif guess < computer_number:
                attempt -=1
                if attempt == 0:
                    print("You have exhausted all of your attempts.. Uranus is not satisfied..\nThere is worst in life, don't worry 🤷‍♂️")
                    game = False
                else:
                    print("This is too low. Keep trying! 🧐")

def hard_mode(computer_number):
    attempt = 5
    game = True
    while game:
        
        print(f"You have {attempt} remaining attempts to guess that number for Uranus! 👊")
        guess = int(input("Make a cosmic guess:\n"))

        if guess == computer_number:
            print("Geeez, you managed! Uranus is very happy 😊")
            game = False
        
        elif guess != computer_number:
            
            if guess > computer_number:
                attempt -= 1
                if attempt == 0:
                    print("You have exhausted all of your attempts.. Uranus is not satisfied..\n There is worst in life, don't worry 🤷")
                    game = False
                else:
                    print("This is too high. Keep trying! 🤔")
            
            elif guess < computer_number:
                attempt -=1
                if attempt == 0:
                    print("You have exhausted all of your attempts.. Uranus is not satisfied..\nThere is worst in life, don't worry 🤷")
                    game = False
                else:
                    print("This is too low. Keep trying! 🧐")

computer_number = computer_picks_number()

difficulty = welcome_message(logo)

if difficulty == "easy":
    easy_mode(computer_number)
elif difficulty == "hard":
    hard_mode(computer_number)
else:
    print("The Galaxy is an intriguing place.. but please write easy or hard properly 😂 ")