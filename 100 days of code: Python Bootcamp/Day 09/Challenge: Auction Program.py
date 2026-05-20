# Blind Auction Project - Day 9
# ─────────────────────────────
# 1: Import and display the logo from art.py at the start of the program.
# 2: Ask the user for their name 
# 3: Ask the user for their bid amount
# 4: Add the name (key) and bid (value) to the dictionary.
# 5: Ask if there are other bidders.
#         - If "yes": clear the screen and loop back
#         - If "no": move on
# 6: Find the highest bid in the dictionary.
# 7: Print the winner's name and their winning bid amount.

#---------------------------------------------------------------------------------------------

#Resources like Logo + Clear the terminal for the yes option
from art import logo
from os import system

#Creation of the dictionary to collect participants name + amount
list_of_bidders = {}

#Dictionary to collect amount + variable to collect the name
winner_name = ""

#Variable to keep tracking the highest score all along during For loop
highest_bid = 0

#To keep the while loop alive until "no"
game = True

print(logo)

while game:
    bidder_name = input("What is your name?")
    bidder_bid_amount = int(input("what is your bid?: €"))
    list_of_bidders[bidder_name] = bidder_bid_amount
    print(list_of_bidders)
    other_bidders_question = input("Are there other bidders? Type 'Yes' or 'No'\n").lower()
    if other_bidders_question == "yes":
        system("clear")
    if other_bidders_question == "no":
        for bid in list_of_bidders:
            if list_of_bidders[bid] > highest_bid:
                highest_bid = list_of_bidders[bid]
                winner_name = bid
        
        print(f"The winner is {winner_name} with a bid of €{highest_bid}")
        game = False