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
     "resources": ["fuel cells", "minerals", "tech parts", "food"],
     "buy price": [0, 0, 0, 0, 0],
     "sell price": [0, 0, 0, 0, 0]},

    {"planet": "Saturn",
     "resources": ["fuel cells", "minerals", "tech parts", "food"],
     "buy price": [0, 0, 0, 0, 0],
     "sell price": [0, 0, 0, 0, 0]},

    {"planet": "Neptune",
     "resources": ["fuel cells", "minerals", "tech parts", "food"],
     "buy price": [0, 0, 0, 0, 0],
     "sell price": [0, 0, 0, 0, 0]},

    {"planet": "Mars",
     "resources": ["fuel cells", "minerals", "tech parts", "food"],
     "buy price": [0, 0, 0, 0, 0],
     "sell price": [0, 0, 0, 0, 0]},


    {"planet": "Earth",
     "resources": ["fuel cells", "minerals", "tech parts", "food"],
     "buy price": [0, 0, 0, 0, 0],
     "sell price": [0, 0, 0, 0, 0]},
]

cargo_hold = {
    "fuel cells": 0,
    "minerals": 0,
    "tech parts": 0,
    "food": 0
}


for step in planet_prices:
    step['buy price'][0] += 15
    print(step['buy price'][0])

print(planet_prices)