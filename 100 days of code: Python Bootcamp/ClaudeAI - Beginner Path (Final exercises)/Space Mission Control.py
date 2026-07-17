# Project 2 — Space Mission Control
# Build a crew management system for a space agency
#
# Store astronauts as a list of dictionaries, each containing:
#   - "name": astronaut's name
#   - "mission": assigned mission (or "Unassigned")
#   - "status": "Available" or "On Mission"
#
# The program should have a while loop menu with these options:
#   1. List all astronauts and their status
#   2. Add a new astronaut
#   3. Assign an astronaut to a mission
#   4. Return an astronaut from a mission (set back to Available)
#   5. Remove an astronaut from the roster
#   6. Exit
#
# Requirements:
#   - Each menu option must call a dedicated function
#   - Functions that modify data must return the updated list
#   - Use .lower() or .upper() on user input where relevant
#   - Handle the case where the astronaut name doesn't exist
#   - Start with at least 3 astronauts already in the roster

# ------ --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

astronauts = [
    {"name":"THOMAS PESQUET",
     "mission":"unassigned",
     "status":"available"},

    {"name":"SOPHIE ADENOT",
     "mission":"unassigned",
     "status":"available"},

    {"name":"PEGGY WHITSON",
     "mission":"unassigned",
     "status":"available"}
]

def display_astronautname_status(astronauts):
    for astronaut in astronauts:
        print(F"\n"
              F"Name: {astronaut['name']}"
              F"\nStatus: {astronaut['status']}"
              F"\nMission: {astronaut['mission']}"
              F"\n")

def add_astronaut(astronauts, display_astronaut_fx):
    new_name = input("Let me know what is the cosmic full name of your new astronaut 🧑‍🚀\n").upper()
    astronauts.append({"name": new_name, "mission": "unassigned", "status": "available"})
    display_astronaut_fx(astronauts)
    return astronauts

def assign_mission(astronauts, display_astronaut_fx):
    human_for_mission = input("Oh wow, Ok, who should go on mission?\n").upper()
    which_mission = input("Amaze, amaze! ⭐️ And what is the name of the mission?\n").lower()
    found = False
    for astronaut in astronauts:
        if astronaut['name'] == human_for_mission:
            astronaut['mission'] = which_mission
            astronaut['status'] = "unavailable"
            found = True
    if not found:
        print("This human does not seem to be in our database.. 🙃\n"
              "No worries, just make sure you did not make a typo, or register them first and come back here 🥰")
    display_astronaut_fx(astronauts)
    return astronauts

def return_mission(astronauts, display_astronaut_fx):
    human_returning = input("GEEZ, that's nice! 😄\n"
                            "Who has returned from mission?").upper()
    found = False
    for astronaut in astronauts:
        if astronaut['name'] == human_returning:
            astronaut['mission'] = "unassigned"
            astronaut['status'] = "available"
            found = True

    if not found:
        print("This human does not seem to be in our database.. 🙃\n"
            "No worries, just make sure you did not make a typo, or register them first and come back here 🥰")
    display_astronaut_fx(astronauts)
    return astronauts

def remove_astronaut(astronauts, display_astronaut_fx):
    remove_human = input("Oh no!😢 Who is leaving us?\n").upper()
    found = False
    for astronaut in astronauts:
        if astronaut['name'] == remove_human:
            astronauts.remove(astronaut)
            found = True
    if not found:
        print("This human does not seem to be in our database.. 🙃\n"
            "No worries, just make sure you did not make a typo, or register them first and come back here 🥰")
    display_astronaut_fx(astronauts)
    return astronauts


print("Welcome to the mighty Space Terminal"
    "\nWhere the stars remain patient, as the clouds bother them 🤔")

space_terminal = True
while space_terminal:
    user_choice = int(input("\nHow can I can help? (type the number according to your action)"

    "\n1. List all astronauts and their status"
    "\n2. Add a new astronaut"
    "\n3. Assign an astronaut to a mission"
    "\n4. Return an astronaut from a mission"
    "\n5. Remove an astronaut from the roster"
    "\n6. Exit"
    "\nNumber: "))

    if user_choice == 1:
        display_astronautname_status(astronauts)
    elif user_choice == 2:
        astronauts = add_astronaut(astronauts, display_astronautname_status)
    elif user_choice == 3:
        astronauts = assign_mission(astronauts, display_astronautname_status)
    elif user_choice == 4:
        astronauts = return_mission(astronauts, display_astronautname_status)
    elif user_choice == 5:
        astronauts = remove_astronaut(astronauts, display_astronautname_status)
    elif user_choice == 6:
        space_terminal = False