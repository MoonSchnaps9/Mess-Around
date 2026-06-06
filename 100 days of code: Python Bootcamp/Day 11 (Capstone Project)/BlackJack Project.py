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
from os import system
import random
from Blackjackicon import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
computer_cards = []

total_count_player = 0
total_count_computer = 0

player_above_21 = False
computer_above_21 = False

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

#Player pick another card
def player_pick_another_card(player_cards):
        player_cards.append(random.choice(cards))
        return player_cards

#Computer pick another card
def computer_pick_another_card(computer_cards):
    computer_cards.append(random.choice(cards))
    return computer_cards
    
#Player total count
def player_total_count(total_count_player, player_cards):
    for u in player_cards:
        total_count_player += u
    return total_count_player

#Computer total count
def computer_total_count(total_count_computer, computer_cards):
    for i in computer_cards:
        total_count_computer += i
    return total_count_computer

#Player above 21?
def player_above_21_check(total_count_player, player_above_21):
    if total_count_player > 21:
        player_above_21 = True
    return player_above_21

#Computer above 21?
def computer_above_21_check(total_count_computer, computer_above_21):
    if total_count_computer > 21:
        computer_above_21 = True
    return computer_above_21

#Ace safe check
def ace_safe_check(above_21, someone_cards, total_count):
    if above_21 == True and 11 in someone_cards:
        total_count -= 10
        above_21 = False
        someone_cards[someone_cards.index(11)] = 1
        return total_count, above_21
    else:
        return total_count, above_21

#Who wins?
def winner_decision(total_count_computer, computer_above_21, total_count_player, player_above_21, player_cards, computer_cards):
    if total_count_player > total_count_computer:
        if player_above_21 == False:
            if total_count_player == 21:
                return f"Your final hand: {player_cards}, total score: {total_count_player}\n Computer final hand: {computer_cards}, total score: {total_count_computer}\n Saturn is impressed! Nice Blackjack :O"
            else:
                return f"Your final hand: {player_cards}, total score: {total_count_player}\n Computer final hand: {computer_cards}, total score: {total_count_computer}\n Congrats, you won! :D"
    elif total_count_player < total_count_computer:
        if computer_above_21 == False:
            if total_count_computer == 21:
                return f"Your final hand: {player_cards}, total score: {total_count_player}\n Computer final hand: {computer_cards}, total score: {total_count_computer}\n Titan has won you over with a Blackjack.. What a moon :'("
            else:
                return f"Your final hand: {player_cards}, total score: {total_count_player}\n Computer final hand: {computer_cards}, total score: {total_count_computer}\n Sorry, you lose! :("
        elif computer_above_21 == True:
            if total_count_player == 21:
                return f"Your final hand: {player_cards}, total score: {total_count_player}\n Computer final hand: {computer_cards}, total score: {total_count_computer}\n Saturn is impressed! Nice Blackjack :O"
            else:
                return f"Your final hand: {player_cards}, total score: {total_count_player}\n Computer final hand: {computer_cards}, total score: {total_count_computer}\n Titan has a score over 21.. Well played, you win! :D"
        
    elif total_count_player == total_count_computer:
        return f"Your final hand: {player_cards}, total score: {total_count_player}\n Computer final hand: {computer_cards}, total score: {total_count_computer}\n WOW, that's a draw.. the tension is celestial >:("


#Welcome Phrase
player_choice_start_game = input("Do you want to play our BlackJack 'Saturn' edition? Type 'Ofc' for yes and 'ofc not' for no\n ").lower()

#In case they say no
if player_choice_start_game == "ofc not":
    print("Ok... you've hurt my feelings :(")

#In case they say yes
if player_choice_start_game == "ofc":
    
    first_loop = True
    while first_loop:
        print(logo)

    #Set the variables at 0
        player_cards = []
        computer_cards = []

        total_count_player = 0
        total_count_computer = 0

        player_above_21 = False
        computer_above_21 = False

    # Run the different functions to create main cards for computer and player. Check as well if player is already above 21
        first_player_draw(player_cards)
        first_computer_card(computer_cards)

        total_count_player = player_total_count(total_count_player, player_cards)
        total_count_computer = computer_total_count(total_count_computer, computer_cards)

        computer_above_21 = computer_above_21_check(total_count_computer, computer_above_21)
        player_above_21 = player_above_21_check(total_count_player, player_above_21)

        total_count_computer, computer_above_21 = ace_safe_check(computer_above_21, computer_cards, total_count_computer)
        total_count_player, player_above_21 = ace_safe_check(player_above_21, player_cards, total_count_player)

    #If player is already > 21 (first loop)
        if  player_above_21 == True:
            print(f"Saturn has decided to not like you, since your celestial cards are {player_cards}\nwhich makes your current score at {total_count_player}")
            try_again_player = input("Would you like to do another game? 'Y' for yes and 'I AM SAD' for no\n").upper()
            if try_again_player == "Y":
                  system("clear")
            elif try_again_player == "I AM SAD":
                first_loop = False
                
    #If Player is not > 21 (first loop)
        elif player_above_21 == False:
            print(f"Your celestial cards are {player_cards}. Your current score is {total_count_player}")
            print(f"Titan's first card is {computer_cards[0]}")
            
            player_first_choice_game = input("type 'G' to get another card or type 'P' to pass\n").upper()
        
        #If Player chooses to pick another card (first loop)
            if player_first_choice_game == 'G':
               
            #Second loop starts
                second_loop = True
                while second_loop:

                #Run functions to add another card and check if >21 while reset the total count to 0
                    player_pick_another_card(player_cards)
                    total_count_player = 0
                    total_count_player = player_total_count(total_count_player, player_cards)
                    player_above_21 = player_above_21_check(total_count_player, player_above_21)
                    total_count_player, player_above_21 = ace_safe_check(player_above_21, player_cards, total_count_player)
                    
                #If player is > 21 (second loop)
                    if  player_above_21 == True:
                        print(f"Saturn has decided to not like you, since your celestial cards are {player_cards}\nwhich makes your current score at {total_count_player}.. Sorry :(")
                        try_again_player = input("Would you like to do another game? 'Y' for yes and 'I AM SAD' for no\n").upper()
                        
                        if try_again_player == "Y":
                            system("clear")
                            second_loop = False
                        elif try_again_player == "I AM SAD":
                            second_loop = False
                            first_loop = False
                    
                #If player < 21 (second loop)
                    elif player_above_21 == False:
                        print(f"Your celestial cards are {player_cards}. Your current score is {total_count_player}")
                        print(f"Titan's first card is {computer_cards[0]}")

                        player_second_choice = input("type 'G' to get another card or type 'P' to pass\n").upper()

                    #If player chooses to pass (second loop)
                        if player_second_choice == "P":
                            if total_count_computer > 17:
                                computer_above_21 = computer_above_21_check(total_count_computer, computer_above_21)
                                print(winner_decision(total_count_computer, computer_above_21, total_count_player, player_above_21, player_cards, computer_cards))
                                try_again_player = input("Would you like to do another game? 'Y' for yes and 'I AM SAD' for no\n").upper()
                                
                                if try_again_player == "Y":
                                    system("clear")
                                    second_loop = False
                                elif try_again_player == "I AM SAD":
                                    second_loop = False
                                    first_loop = False
                        
                        #If computer cards < 17 (Computer loop with >17)
                            else:
                                until_17_loop = True
                                while until_17_loop:
                                    total_count_computer = 0
                                #Pick another card and never stop until sum > 17
                                    computer_pick_another_card(computer_cards)
                                    total_count_computer = computer_total_count(total_count_computer, computer_cards)
                                    computer_above_21 = computer_above_21_check(total_count_computer, computer_above_21)
                                    total_count_computer, computer_above_21 = ace_safe_check(computer_above_21, computer_cards, total_count_computer)

                                    if total_count_computer > 17:
                                        print(winner_decision(total_count_computer, computer_above_21, total_count_player, player_above_21, player_cards, computer_cards))
                                        try_again_player = input("Would you like to do another game? 'Y' for yes and 'I AM SAD' for no\n").upper()

                                        if try_again_player == "Y":
                                            until_17_loop = False
                                            second_loop = False
                                            system("clear")
                                        elif try_again_player == "I AM SAD":
                                            until_17_loop = False
                                            second_loop = False
                                            first_loop = False

        #If player chooses to Pass (first loop)
            elif player_first_choice_game == 'P':
                    if total_count_computer > 17:
                        print(winner_decision(total_count_computer, computer_above_21, total_count_player, player_above_21, player_cards, computer_cards))
                        try_again_player = input("Would you like to do another game? 'Y' for yes and 'I AM SAD' for no\n").upper()
                            
                        if try_again_player == "Y":
                            system("clear")
                        elif try_again_player == "I AM SAD":
                            first_loop = False
                    
                    else:
                        until_17_loop = True
                        while until_17_loop:
                            total_count_computer = 0
                        #Pick another card and never stop until sum > 17    
                            computer_pick_another_card(computer_cards)
                            total_count_computer = computer_total_count(total_count_computer, computer_cards)
                            computer_above_21 = computer_above_21_check(total_count_computer, computer_above_21)
                            total_count_computer, computer_above_21 = ace_safe_check(computer_above_21, computer_cards, total_count_computer)

                            if total_count_computer > 17:
                                print(winner_decision(total_count_computer, computer_above_21, total_count_player, player_above_21, player_cards, computer_cards))
                                try_again_player = input("Would you like to do another game? 'Y' for yes and 'I AM SAD' for no\n").upper()
                                    
                                if try_again_player == "Y":
                                    until_17_loop = False
                                    system("clear")
                                elif try_again_player == "I AM SAD":
                                    until_17_loop = False
                                    first_loop = False