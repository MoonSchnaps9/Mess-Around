# Blackjack Project
# ──────────────────

# HOUSE RULES:
# - The deck is unlimited in size.
# - There are no jokers.
# - The Jack/Queen/King all count as 10.
# - The Ace can count as 11 or 1.
# - The cards in the list have equal probability of being drawn.
# - Cards are not removed from the deck as they are drawn.
# - The computer is the dealer.
from Blackjackicon import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_choice = input("Do you want to play our BlackJack 'Saturn' edition? Type 'Ofc' for yes and 'ofc not' for no\n ").lower()

if player_choice == "ofc not":
    print("Ok... you've hurt my feelings :(")

if player_choice == "ofc":
    print(logo)
