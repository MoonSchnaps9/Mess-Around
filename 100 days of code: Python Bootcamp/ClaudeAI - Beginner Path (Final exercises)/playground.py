# Project 3 — Space Trading Game
# You are a cargo pilot flying between planets.
# Your goal: reach 1000 credits to retire.
#
# Setup:
#   - Start with 200 credits and an empty cargo hold
#   - There are 5 planets, each selling and buying different resources
#   - Resources: "fuel cells", "minerals", "water", "tech parts", "food"
#   - Each planet has random buy/sell prices generated at the start
#   - Prices fluctuate slightly each time you travel to a new planet
#
# The game loop:
#   1. Show current planet, credits, and cargo hold
#   2. Show available resources to buy and their prices
#   3. Show what the current planet will pay for resources you're carrying
#   4. Let user buy, sell, or travel to another planet
#   5. Travelling costs 20 credits (fuel)
#   6. If credits drop to 0 or below — game over
#   7. If credits reach 1000 or above — you win
#
# Requirements:
#   - Planets and prices stored as dictionaries
#   - At least 3 functions with return values
#   - random used for price fluctuation
#   - Track cargo as a dictionary (resource: quantity)
#   - .lower() or .upper() on all user input

#--------------------------------------------------------------------------------------------------

#Import the tools
import random

#Ressouces
wallet = 200

planet_prices = [

    {"planet": "Jupiter",
     "resources": ["fuel cell", "mineral", "water", "tech part", "food"],
     "buy price": [1, 5, 3, 4, 2],
     "sell price": [23, 34, 45, 43, 34]},

    {"planet": "Saturn",
     "resources": ["fuel cell", "mineral", "water", "tech part", "food"],
     "buy price": [0, 0, 0, 0, 0],
     "sell price": [0, 0, 0, 0, 0]},

    {"planet": "Neptune",
     "resources": ["fuel cell", "mineral", "water", "tech part", "food"],
     "buy price": [0, 0, 0, 0, 0],
     "sell price": [0, 0, 0, 0, 0]},

    {"planet": "Mars",
     "resources": ["fuel cell", "mineral", "water", "tech part", "food"],
     "buy price": [0, 0, 0, 0, 0],
     "sell price": [0, 0, 0, 0, 0]},


    {"planet": "Earth",
     "resources": ["fuel cell", "mineral", "water", "tech part", "food"],
     "buy price": [0, 0, 0, 0, 0],
     "sell price": [0, 0, 0, 0, 0]},
]

cargo_hold = {
    "fuel cell": 5,
    "mineral": 4,
    "water": 0,
    "tech part": 3,
    "food": 4
}

# def wallet_status(wallet):
#     """Function that is used to display the current wallet of the user"""
#     print(F"You currently have {wallet} credits")

# def cargo_hold_status(cargo_hold):
#     """Function that is used to display the current status of the user's cargo hold"""
#     print("In your cargo hold, you currently have:")
#     for key in cargo_hold:
#         print(F"{key}: {cargo_hold[key]}")


# def start_randomize_prices(planet_prices):
#     """Function that is used at the beginning to randomize all prices"""
#     for index in range(len(planet_prices)):
#         for buy_price in range(0, len(planet_prices[index]['buy price'])):
#             planet_prices[index]['buy price'][buy_price] = random.randint(250, 600)
#         for sell_price in range(0, len(planet_prices[index]['sell price'])):
#             planet_prices[index]['sell price'][sell_price] = random.randint(150, 500)
#     return planet_prices


current_planet = random.choice(planet_prices)

print(current_planet)
def current_planet_status(current_planet):
    """Function that is used to display the different resource price |
    it works with current_planet = random.choice(planet_prices)"""
    print(F"\nWelcome to {current_planet['planet']}!"
        "\nThe current buy price:\n")
    for index in range(0, len(current_planet['resources'])):
        print(F"The {current_planet['resources'][index]} is at {current_planet['buy price'][index]}")
    print("\nThe current sell price:\n")
    for index in range(0, len(current_planet['resources'])):
        print(F"The {current_planet['resources'][index]} is at {current_planet['sell price'][index]}")


current_planet_status(current_planet)

def potential_planet_gain(cargo_hold, current_planet):
    """Function that is used to compare the cargo_hold with current_planet prices |
    if there is a match, the price of 1 cell will show up as a potentail gain"""
    for index, merch in enumerate(cargo_hold):
        if cargo_hold[merch] != 0:
            potential_gain = current_planet['buy price'][index]
            print(f"You could sell 1 {merch} for a total gain of {potential_gain}")


user_choice = "E"

def translate_buy_option(user_choice):
    """Function that is used to translate the user choice from 'A' to 'E' to the actual resource"""
    temporary_dict = {
    "fuel cell": "A",
    "mineral": "B",
    "water": "C",
    "tech part": "D",
    "food": "E"
    }
    for key in temporary_dict:
        if user_choice == temporary_dict[key]:
            user_choice = key
    print(user_choice)


translate_buy_option(user_choice)