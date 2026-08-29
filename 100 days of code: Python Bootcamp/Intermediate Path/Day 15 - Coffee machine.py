# ============================================================
# DAY 15 — COFFEE MACHINE
# ============================================================
#
# ------------------------------------------------------------
# 1. PROMPT USER
# ------------------------------------------------------------
#    "What would you like? (espresso/latte/cappuccino): "
#    - Check the user's input to decide what to do next.
#    - The prompt should show every time an action has completed,
#      e.g. once the drink is dispensed, the prompt shows again
#      to serve the next customer.
#
# ------------------------------------------------------------
# 2. TURN OFF THE MACHINE
# ------------------------------------------------------------
#    - Entering "off" at the prompt is the maintainer's secret word.
#    - Code execution should end when this happens.
#
# ------------------------------------------------------------
# 3. PRINT REPORT
# ------------------------------------------------------------
#    - Entering "report" prints the current resource values, e.g.
#
#        Water: 100ml
#        Milk: 50ml
#        Coffee: 76g
#        Money: $2.5
#
# ------------------------------------------------------------
# 4. CHECK RESOURCES SUFFICIENT?
# ------------------------------------------------------------
#    - When a drink is chosen, check there are enough resources.
#    - E.g. Latte requires 200ml water but only 100ml is left:
#      do not make the drink, print "Sorry there is not enough water."
#    - Same applies to any depleted resource (milk, coffee).
#
# ------------------------------------------------------------
# 5. PROCESS COINS
# ------------------------------------------------------------
#    - If resources are sufficient, prompt the user to insert coins.
#
#      COIN VALUES:
#        quarters = $0.25
#        dimes    = $0.10
#        nickles  = $0.05
#        pennies  = $0.01
#
#    - Calculate the monetary value inserted, e.g.
#      1 quarter, 2 dimes, 1 nickel, 2 pennies
#      = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
#
# ------------------------------------------------------------
# 6. CHECK TRANSACTION SUCCESSFUL?
# ------------------------------------------------------------
#    - Check enough money was inserted for the selected drink.
#      E.g. Latte costs $2.50, only $0.52 inserted:
#      "Sorry that's not enough money. Money refunded."
#    - If enough: the cost of the drink is added to the machine
#      as profit, reflected next time "report" is triggered.
#    - If too much: offer change, e.g.
#      "Here is $2.45 dollars in change."
#      Change is rounded to 2 decimal places.
#
# ------------------------------------------------------------
# 7. MAKE COFFEE
# ------------------------------------------------------------
#    - If the transaction is successful and resources are enough,
#      deduct the drink's ingredients from the machine resources.
#
#      BEFORE buying a latte:        AFTER buying a latte:
#        Water: 300ml                  Water: 100ml
#        Milk: 200ml                   Milk: 50ml
#        Coffee: 100g                  Coffee: 76g
#        Money: $0                     Money: $2.5
#
#    - Once deducted, tell the user "Here is your latte. Enjoy!"
#      (matching their choice of drink).
#
# ============================================================
from os import system

#Creating resources + Money
available_drinks = {
    "martian hot chocolate": {
        "ingredients": {
            "milk": 150,
            "chocolate": 100
        },
        "cost": 2.5
    },

    "venusian coffee": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },

    "earthian pleasure": {
        "ingredients": {
            "water": 50,
            "milk": 100,
            "chocolate": 150
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 300,
    "chocolate": 99,
    "coffee": 300
}

type_money = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

machine_money = 0.0

#creating the possible actions with def

def report(resources, money):
    for item in resources:
        print(f"{item}: {resources[item]}ml")
    print(f"Money: {money}")

def check_coffee(user_drink, drinks, resources):
    loop = True
    for ingredient in drinks[user_drink]["ingredients"]:
        if drinks[user_drink]["ingredients"][ingredient] > resources[ingredient]:
            print(F"Sorry there is not enough {ingredient}.")
            loop = False
            return loop
    return loop

def check_money(machine_money, type_money, quarters, dimes, nickles, pennies, drink, user_drink):
    total_quarters = type_money["quarters"] * quarters
    total_dimes = type_money["dimes"] * dimes
    total_nickles = type_money["nickles"] * nickles
    total_pennies = type_money["pennies"] * pennies
    sum = total_quarters + total_dimes + total_nickles + total_pennies

    if sum < drink[user_drink]["cost"]:
        loop = False
        print(F"Sorry that's not enough money, as {drink[user_drink]} cost: {drink[user_drink]["cost"]}\n" 
              "Money refunded.")
        return loop
    elif sum >= drink[user_drink]["cost"]:
        machine_money += drink[user_drink]["cost"]
        if sum - drink[user_drink]["cost"] > 0:
            money_to_return = sum - drink[user_drink]["cost"]
            print(F"Btw, Here is ${money_to_return} dollars in change.")
            loop = True
            return loop











#Creating While loop aka full program
machine = True
while machine:
    user_choice = input("Tell me what whould like for a drink, and I'll explain why I can't help you (..unless you know where Sagittarius A* is 🧐)\n" \
    "Options: Martian Hot Chocolate/ Venusian coffee/ Earthian Pleasure\n" \
    "Answer:").lower()

    #If user choose report, displaying current resources with money
    if user_choice == "report":
        report(resources, machine_money)

    #if user choose one of the available coffee:
    elif user_choice == "martian hot chocolate" or user_choice == "venusian coffee" or user_choice == "earthian pleasure":
        make_coffee_loop = True

        #First check: Enough resources?
        loop = check_coffee(user_choice, available_drinks, resources)
        print(loop)
        if loop == False:
            make_coffee_loop == False

        #Second check: Enough Money?
        elif loop == True:
                quarters = int(input("how many quarters? "))
                dimes = int(input("How many dimes? "))
                nickles = int(input("How many nicles? "))
                pennies = int(input("How many pennies? "))