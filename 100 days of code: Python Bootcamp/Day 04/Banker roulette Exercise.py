# Banker Roulette
# Figure out how to pick a random name from the list of friends.
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#Option1
print(random.choice(friends))

#Option 2
random_selection = random.randint(0,4)
print(friends[random_selection])