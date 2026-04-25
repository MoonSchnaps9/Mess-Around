# You have this list:
import random
items = ["apples", "bread", "milk", "eggs", "cheese", "pasta", "rice", "chicken", "coffee", "butter"]

# Write a program that:

# Asks the user how many items they need to buy
# Randomly picks that many items from the list without repeating the same item twice
# Prints the final shopping list numbered

# Example output:
# Your shopping list:
# 1. eggs
# 2. coffee
# 3. milk

number_of_items_buy = int(input("How many items do you need to buy?\n"))

print("Your shopping list: ")

list_of_items = random.sample(items, number_of_items_buy)
final_list = ""

for availableitems in range(number_of_items_buy):
    final_list = list_of_items[availableitems]
    print(F"{availableitems + 1}. {final_list}")
