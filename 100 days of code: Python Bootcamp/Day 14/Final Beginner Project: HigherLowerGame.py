#Final Beginner Project
#Build from scratch the HigherLowerGame
#Teacher gave us a variable that contained a list of dictionaires (I came up with my own) + Logo

#----------------------------------------------------------------------------------------------------------
import random
from os import system
from art import logo
from game_data import data

option_a = {}
option_b = {}
score = 0

def random_choice(option_a, option_b, data):
    option_a = random.choice(data)
    option_b = random.choice(data)

    if option_a == option_b:
        same_result = True
        while same_result:
            option_b = random.randint(data)
            if option_a != option_b:
                same_result = False
    return option_a, option_b

def compare_choice(user_choice, option_a, option_b):
    if option_a["follower_count"] > option_b["follower_count"]:
        if user_choice == "A":
            user_choice = option_a
            return True, user_choice
        
        elif user_choice == "B":
            return False, user_choice
        
        elif user_choice == "MERCURY":
            return False, user_choice
        
    if option_b["follower_count"] > option_a["follower_count"]:
        if user_choice == "B":
            user_choice = option_b
            return True, user_choice
        
        elif user_choice == "A":
            return False, user_choice
        
        elif user_choice == "MERCURY":
            return False, user_choice
        
    if option_a["follower_count"] == option_b["follower_count"]:
        if user_choice == "MERCURY":
            user_choice = option_a
            return True, user_choice
        else:
            return False, user_choice

def random_choice_part2(option_b, data):
    option_b = random.choice(data)
    return option_b

print(logo)

option_a, option_b = random_choice(option_a, option_b, data)

print(f"First option ⭐️: {option_a['name']}, a {option_a['description']} from {option_a['country']}")

game = True
while game:
    print(f"Second option ⭐️: {option_b['name']}, a {option_b['description']} from {option_b['country']}\n")

    user_choice = input("Who has more celestial followers? type 'A' for first choice and 'B' for second choice\n PS: If you think they have the same number... bold but type 'Mercury'\n").upper()
    result, user_choice = compare_choice(user_choice, option_a, option_b)

    if result == True:
            # system("clear")
            print(logo)
            score +=1
            print(f"I've never seen a black hole.. but I can recognize a good answer! Your current score: {score}\n")
            print(f"First option ⭐️: {user_choice['name']}, a {user_choice['description']} from {user_choice['country']}")
            option_a = user_choice
            option_b = random_choice_part2(option_b, data)

    elif result == False:
        game = False
        # system("clear")
        print(logo)
        print(f"I've never seen a black hole... but I've seen the emptiness in your eyes when this is unfortunately a wrong guess...😢\n Your final score: {score}")