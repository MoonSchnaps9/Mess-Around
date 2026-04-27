# Exercise: Lottery Ticket Generator
import random
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Write a program that:

# Asks the user how many lottery tickets they want to generate
# Each ticket has 5 unique numbers picked from the pool
# Numbers on each ticket are sorted in ascending order
# Prints each ticket numbered

# Example output:
# Ticket 1: [3, 7, 11, 15, 18]
# Ticket 2: [1, 6, 9, 14, 20]


#Ask question
number_of_tickets_to_draw = int(input("How many lottery tickets do you want? \n"))

#Create For loop with random.sample and new function (sort)
for lotteryresult in range (number_of_tickets_to_draw):
    ticket_results_after_draw = random.sample(lottery_pool, 5)
    ticket_results_after_draw.sort()
    print(f"Ticket {lotteryresult + 1}: {ticket_results_after_draw}")
