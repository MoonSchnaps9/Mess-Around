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
from os import system

#Logo 
logo = """
   ✦ · · · · · · · · · · · · · · · · · · · · · · · · · · ✦

  ███████╗██████╗  █████╗  ██████╗███████╗
  ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝
  ███████╗██████╔╝███████║██║     █████╗  
  ╚════██║██╔═══╝ ██╔══██║██║     ██╔══╝  
  ███████║██║     ██║  ██║╚██████╗███████╗
  ╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝

 ████████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
 ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ██║   ██████╔╝███████║██║  ██║█████╗  ██████╔╝
    ██║   ██╔══██╗██╔══██║██║  ██║██╔══╝  ██╔══██╗
    ██║   ██║  ██║██║  ██║██████╔╝███████╗██║  ██║
    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

  · ✦ · 🚀  G A L A X Y   M E R C H A N T  🚀 · ✦ ·

       ·  ★  ·  ·  ✦  ·  ·  ★  ·  ·  ✦  ·  ·  ★  ·

   ✦ · · · · · · · · · · · · · · · · · · · · · · · · · · ✦
"""

#WHY logo (joke)
why_logo = """
   ✦ · · · · · · · · · · · · · · · · · · · · · ✦

  ██╗    ██╗██╗  ██╗██╗   ██╗   ██╗
  ██║    ██║██║  ██║╚██╗ ██╔╝   ██║
  ██║ █╗ ██║███████║ ╚████╔╝    ██║
  ██║███╗██║██╔══██║  ╚██╔╝     ╚═╝
  ╚███╔███╔╝██║  ██║   ██║      ██╗
   ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝

  · ✦ · 🌌  E V E N   T H E   V O I D
            I S   D I S A P P O I N T E D  🌌 · ✦ ·

   ✦ · · · · · · · · · · · · · · · · · · · · · ✦
"""

#Learn how to write joke
write_logo = """
   ✦ · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ✦

  ██╗     ███████╗ █████╗ ██████╗ ███╗   ██╗
  ██║     ██╔════╝██╔══██╗██╔══██╗████╗  ██║
  ██║     █████╗  ███████║██████╔╝██╔██╗ ██║
  ██║     ██╔══╝  ██╔══██║██╔══██╗██║╚██╗██║
  ███████╗███████╗██║  ██║██║  ██║██║ ╚████║
  ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝

  ██╗  ██╗ ██████╗ ██╗    ██╗    ████████╗ ██████╗
  ██║  ██║██╔═══██╗██║    ██║    ╚══██╔══╝██╔═══██╗
  ███████║██║   ██║██║ █╗ ██║       ██║   ██║   ██║
  ██╔══██║██║   ██║██║███╗██║       ██║   ██║   ██║
  ██║  ██║╚██████╔╝╚███╔███╔╝       ██║   ╚██████╔╝
  ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝        ╚═╝    ╚═════╝

  ██╗    ██╗██████╗ ██╗████████╗███████╗
  ██║    ██║██╔══██╗██║╚══██╔══╝██╔════╝
  ██║ █╗ ██║██████╔╝██║   ██║   █████╗
  ██║███╗██║██╔══██╗██║   ██║   ██╔══╝
  ╚███╔███╔╝██║  ██║██║   ██║   ███████╗
   ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝

  · ✦ · 🪐  T H E   U N I V E R S E   A G R E E S  🪐 · ✦ ·

   ✦ · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ✦
"""

#Ressouces
wallet = 200

#Planets and their prices
planet_prices = [

    {"planet": "Jupiter",
     "resources": ["fuel cell", "mineral", "water", "tech part", "food"],
     "buy price": [0, 0, 0, 0, 0],
     "sell price": [0, 0, 0, 0, 0]},

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

#Cargo hold of the user's space ship
cargo_hold = {
    "fuel cell": 0,
    "mineral": 0,
    "water": 0,
    "tech part": 0,
    "food": 0
}
def welcome_message(logo):
    """Function that is used to welcome the user"""
    print(f"{logo}"
          f"\nWelcome to the Space trader game! Your goal is to trade resources between planets! 🌍🪐"
          f"\nYour objective is to reach 1000 credits in your wallet!\n" 
          f"\nIf your wallet reach 0 or lower, then we'll have to throw you to TON 618 😨"
          f"\n(..Yes, that far 😠)")

def welcome_joke(why_logo, write_logo, yolo):
    """unnecessary function that is used to ask if the user wants to play"""
    can_user_play = input(f"\nAre you ready to risk your ENTIRE existence attempting to have 1000 credits?\n"
                      f"write 'YOLO' for yes and 'HELL NO' for.. I guess no 🤷"
                      f"\nAstral answer: ").upper()

    if can_user_play == "HELL NO":
        system('clear')
        print(why_logo)
        print(f"OK ok, maybe TON 618 is... WAY TOO MUCH? I know, but hey, there's no success without taking risks 🥹")

    elif can_user_play != "HELL NO" and can_user_play != "YOLO":
        system('clear')
        print(write_logo)
        print(f"You had one celestial job, and you managed to make a typo.. or you tested if the program was working properly? 🧐"
            f"\nEither way, the universe bans you for your lack of trust. Bad human! 😠")

    elif can_user_play == "YOLO":
        yolo = "yes"
        return yolo

def wallet_status(wallet):
    """Function that is used to display the current wallet of the user"""
    print(F"You currently have {wallet} credits")

def cargo_hold_status(cargo_hold):
    """Function that is used to display the current status of the user's cargo hold"""
    print("In your cargo hold, you currently have:")
    for key in cargo_hold:
        print(F"{key}: {cargo_hold[key]}")


def start_randomize_prices(planet_prices):
    """Function that is used at the beginning to randomize all prices"""
    for index in range(len(planet_prices)):
        for sell_price in range(0, len(planet_prices[index]['sell price'])):
            planet_prices[index]['sell price'][sell_price] = random.randint(150, 450)
        for buy_price in range(0, len(planet_prices[index]['buy price'])):
            planet_prices[index]['buy price'][buy_price] = round(planet_prices[index]['sell price'][buy_price] * random.uniform(0.4, 0.7))
    return planet_prices


def price_fluctuation_travel(planet_prices):
    """Function that is used when the user decides to travel | Price fluctuation"""
    for index in range(len(planet_prices)):
        for buy_price in range(0, len(planet_prices[index]['buy price'])):
            planet_prices[index]['buy price'][buy_price] += random.randint(-50, 50)
        for sell_price in range(0, len(planet_prices[index]['sell price'][buy_price])):
            planet_prices[index]['sell price'][sell_price] += random.randint(-50, 50)
    return planet_prices


def current_planet_status(current_planet):
    """Function that is used to display the different resource price |
    it works with current_planet = random.choice(planet_prices)"""
    print(F"\nWelcome to {current_planet['planet']}!"
        "\nThe current buy price:\n"
        f"(How much the merchands here are willing to pay for the resources)\n")
    for index in range(0, len(current_planet['resources'])):
        print(F"The {current_planet['resources'][index]} is at {current_planet['buy price'][index]}")
    print("\nThe current sell price:\n"
f"(How much you will pay to buy some resources here)\n")
    for index in range(0, len(current_planet['resources'])):
        print(F"The {current_planet['resources'][index]} is at {current_planet['sell price'][index]}")


def potential_planet_gain(cargo_hold, current_planet):
    """Function that is used to compare the cargo_hold with current_planet prices |
    if there is a match, the price of 1 cell will show up as a potentail gain"""
    for index, merch in enumerate(cargo_hold):
        if cargo_hold[merch] != 0:
            potential_gain = current_planet['buy price'][index]
            print(f"You could sell 1 {merch} for a total gain of {potential_gain}")


def user_action_choice(user_action):
    user_action = int(input(f"\nTime to strategi..strate..." 
    f"\n😅 it's time tell me what you want to do!" 
    f"\n1. Buy resources on this planet" 
    f"\n2. Sell resources on this planet" 
    f"\n3. Travel to another planet (cost: 20)"
    "\nAnswer: "))
    return user_action



def translate_user_option(user_choice):
    """Function that is used to translate the user choice from 'A' to 'E' to the actual resource"""
    temporary_dict = {
    "fuel cell": 1,
    "mineral": 2,
    "water": 3,
    "tech part": 4,
    "food": 5
    }
    for key in temporary_dict:
        if user_choice == temporary_dict[key]:
            user_choice = key
    return user_choice


def buy_operation(current_planet, cargo_hold, wallet, user_choice):
    """Function that is used to when user wants to sell resources from cargo_hold"""
    temp_value = current_planet['resources'].index(user_choice)

    if cargo_hold[user_choice] == 0:
        print("You can't do this!"
              F"\nYou don't have enough {user_choice}!")
        return cargo_hold, wallet
    else:
        wallet += current_planet['buy price'][temp_value]
        cargo_hold[user_choice] -= 1
        return cargo_hold, wallet

def sell_operation(current_planet, cargo_hold, wallet, user_choice):
    """Function that is used to when user wants to buy resources from planet"""
    temp_value = current_planet['resources'].index(user_choice)

    if current_planet['sell price'][temp_value] > wallet:
        print("You can't do this!"
              F"\nYou don't have enough money!")
        return cargo_hold, wallet
    else:
            temp_value = current_planet['resources'].index(user_choice)
            wallet -= current_planet['sell price'][temp_value]
            cargo_hold[user_choice] += 1
            return cargo_hold, wallet


def travel_operation(current_planet, planet_prices, wallet):
    """Function that is used when user wants to travel to another planet"""
    wallet -= 20
    temp_variable = current_planet
    current_planet = random.choice(planet_prices)
    while temp_variable == current_planet:
        current_planet = random.choice(planet_prices)
    return current_planet, wallet


yolo = ""
welcome_message(logo)
yolo = welcome_joke(why_logo, write_logo, yolo)

if yolo == "yes":
    #Clear the system + show current wallet + current cargo_hold
    system('clear')
    wallet_status(wallet)
    print(f"\n")
    cargo_hold_status(cargo_hold)

    #randomzie prices at the beginning, select planet among 5
    print(f"\n")
    start_randomize_prices(planet_prices)
    current_planet = random.choice(planet_prices)

    #Displaying current planet
    current_planet_status(current_planet)
    user_action = 0
    user_action = user_action_choice(user_action)
