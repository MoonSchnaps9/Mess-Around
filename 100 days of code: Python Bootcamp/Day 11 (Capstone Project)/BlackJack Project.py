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
import random
from Blackjackicon import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
total_count_player = 0

#Player start hand
def first_player_draw(player_cards):
    for card in range(2):
        player_cards.append(random.choice(cards))
    return player_cards

print(first_player_draw(player_cards))


# #Computer start hand
# computer_card_start = []
# for card in range(2):
#     computer_card_start.append(random.choice(cards))

# #Welcome Phrase
# player_choice_start_game = input("Do you want to play our BlackJack 'Saturn' edition? Type 'Ofc' for yes and 'ofc not' for no\n ").lower()

# #In case they say no
# if player_choice_start_game == "ofc not":
#     print("Ok... you've hurt my feelings :(")

# #In case they say yes
# if player_choice_start_game == "ofc":
    
#     game = True
#     while game:
#         print(logo)
#         print(f"Your celestial cards are {player_card_start[0]}, {player_card_start[1]}. Your current score is {total_count_player}")
#         print(f"Titan's first card is {computer_card_start[0]}")
#         Player_choice_during_game = input("type 'M' to get another card or type 'A' to pass").upper()
#         if player_choice_during_game 
        