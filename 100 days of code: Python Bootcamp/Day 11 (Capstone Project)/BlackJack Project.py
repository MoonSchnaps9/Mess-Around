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
computer_cards = []
total_count_player = 0
total_count_computer = 0

#Player start hand function
def first_player_draw(player_cards):
    for card in range(2):
        player_cards.append(random.choice(cards))
    return player_cards

#Computer start hand function
def first_computer_card(computer_cards):
    for i in range(2):
        computer_cards.append(random.choice(cards))
    return computer_cards
    
#Player total count
def player_total_count(total_count_player, player_cards):
    for score in player_cards:
        total_count_player += score
    return total_count_player

#Computer total count
def computer_total_count(total_count_computer, computer_cards):
    for score in computer_cards:
        total_count_computer += score
    return total_count_computer

print(first_player_draw(player_cards))
print(first_computer_card(computer_cards))
print(player_total_count(total_count_player, player_cards))
print(computer_total_count(total_count_computer, computer_cards))

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
#         print(f"Your celestial cards are {player_cards[0]}, {player_cards[1]}. Your current score is {total_count_player}")
#         print(f"Titan's first card is {computer_card_start[0]}")
#         Player_choice_during_game = input("type 'M' to get another card or type 'A' to pass").upper()
#         if player_choice_during_game 
        