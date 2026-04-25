# Exercise: Name Badge Generator
# You have three lists:
import random

first_names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
departments = ["Engineering", "Marketing", "Finance", "HR", "Legal"]
id_numbers = [101, 102, 103, 104, 105]

# Write a program that:

# Asks the user how many badges to generate
# For each badge, randomly picks one first name, one department, and one ID number
# Prints each badge like this: Badge: Alice | Engineering | ID: 101

number_of_badge_to_generate = int(input("How many badge would you like to generate? "))

first_name_employee = ""
departments_employee = ""
id_employee = ""

for line in range(number_of_badge_to_generate):
    first_name_employee = random.choice(first_names)
    departments_employee = random.choice(departments)
    id_employee = str(random.choice(id_numbers))
    print("Badge: " + first_name_employee + " | " + departments_employee + " | " + "ID: " + id_employee)

print("---------------")

#Added Claude suggestion
for line in range(number_of_badge_to_generate):
    print(f"Badge: {random.choice(first_names)} | {random.choice(departments)} | ID: {random.choice(id_numbers)}")