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

def add_item(inventory):
    quantity, item = int(input("How many Pluto do you.. I mean, how many to add?\n").lower()), (input("name?\n").lower())
    for_loop_check = False
    for resources in inventory:
        if resources == item:
            inventory[resources] += quantity
            for_loop_check = True

    if for_loop_check == False:
        inventory[item] = quantity

    print(inventory)
    return(inventory)

def remove_item(inventory):
    quantity, item = int(input("How many Pluto do you.. I mean, how many to remove?\n").lower()), (input("name?\n").lower())
    for_loop_check_T = False
    for resources in inventory:
        if resources == item:
            if inventory[resources] - quantity < 0:
                print("So, basically you would go below 0.. and it's like creating a black hole.. and we don't want that so.. try again please? 😅")
                for_loop_check_T = True
            else:
                inventory[resources] -= quantity
                print(inventory)
                for_loop_check_T = True

    if for_loop_check_T == False:
        print("You basically want to remove some stuff in your inventory that do not exist...\n" \
        "I mean.. it's like removing air in space where there's no air... but hey, I like this clean freak spirit!")

    return(inventory)


display_inventory(inventory)
add_item(inventory)
remove_item(inventory)