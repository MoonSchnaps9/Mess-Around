# Warm-up 2:
# Write a program that manages a simple space inventory. No menu needed — just functions.
# Start with this dictionary:
inventory = {
    "fuel cells": 10,
    "minerals": 5,
    "water": 8,
    "tech parts": 3,
    "food": 12
}
# Write three functions:
# display_inventory(inventory) — prints each item and its quantity
# add_item(inventory, item, quantity) — adds quantity to an existing item, or creates it if it doesn't exist. Returns the updated inventory.
# remove_item(inventory, item, quantity) — removes quantity from an item. If quantity would go below 0, print a warning and don't remove. If the item doesn't exist, print a warning. Returns the updated inventory.


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def display_inventory(inventory):
    for item in inventory:
        print(f"You have {inventory[item]} {item}")