# Build an automatic pizza order program that uses input() to get a user's preferences and calculate their final bill.
# Pricing:

# Small (S): $15
# Medium (M): $20
# Large (L): $25
# Pepperoni on small: +$2
# Pepperoni on medium or large: +$3
# Extra cheese (any size): +$1

# Expected output example:
# Welcome to Python Pizza Deliveries!
# What size pizza do you want? S, M or L: L
# Do you want pepperoni on your pizza? Y or N: Y
# Do you want extra cheese? Y or N: N
# Your final bill is: $28.

#Guillaume's version (Effective but very long. S size took a bit of time, but then copy-paste for M & L + rename variables was way faster)

print("Welcome to the Galactic Python Pizza Delivery of Jupiter!")

size_of_pizza = input("What size pizza do you want? S, M or L?: ")

if size_of_pizza == "S":
    price_of_s_pizza = 15
    
    pepperoni_on_s_pizza = input("Do you want pepperoni on your pizza? Y or N?: ")
    if pepperoni_on_s_pizza == "Y":
        price_of_s_pizza += 2

    extra_cheese_s_pizza = input("Do you want extra cheese? Y or N?: ")
    if extra_cheese_s_pizza == "Y":
        price_of_s_pizza += 1

    print(f"Your final bill is: ${price_of_s_pizza}")

elif size_of_pizza == "M":
    price_of_m_pizza = 20
    
    pepperoni_on_m_pizza = input("Do you want pepperoni on your pizza? Y or N?: ")
    if pepperoni_on_m_pizza == "Y":
        price_of_m_pizza += 3

    extra_cheese_s_pizza = input("Do you want extra cheese? Y or N?: ")
    if extra_cheese_s_pizza == "Y":
        price_of_m_pizza += 1

    print(f"Your final bill is: ${price_of_m_pizza}")

elif size_of_pizza == "L":
    price_of_l_pizza = 25

    pepperoni_on_l_pizza = input("Do you want pepperoni on your pizza? Y or N?: ")
    if pepperoni_on_l_pizza == "Y":
        price_of_l_pizza += 3

    extra_cheese_l_pizza = input("Do you want extra cheese? Y or N?: ")
    if extra_cheese_l_pizza == "Y":
        price_of_l_pizza += 1

    print(f"Your final bill is: ${price_of_l_pizza}")

#ClaudeAI suggestion: What a cleaner structure looks like conceptually:
    # Ask the size, set the base price
    # Ask pepperoni once, add $2 or $3 depending on the size already stored
    # Ask cheese once, add $1
    # Print the bill once

#Guillaume attempt to make ClaudeAI Happy (it works!)

print("Welcome to the Galactic Python Pizza Delivery of Jupiter!")
size_of_pizza = input("What size pizza do you want? S, M or L?: ")

if size_of_pizza == "S":
    price_pizza = 15
elif size_of_pizza == "M":
    price_pizza = 20
elif size_of_pizza == "L":
    price_pizza = 25

pepperoni_pizza = input("Do you want pepperoni on your pizza? Y or N?: ")
if pepperoni_pizza == "Y":
    if size_of_pizza == "S":
        price_pizza += 2
    else:
        price_pizza += 3

extra_cheese = input("Do you want extra cheese? Y or N?: ")
if extra_cheese == "Y":
    price_pizza += 1

print(f"Your final bill is: ${price_pizza}")