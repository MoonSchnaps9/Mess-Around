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
    for astronaut in astronauts:
        if astronaut['name'] == human_for_mission:
            astronaut['mission'] = which_mission
            astronaut['status'] = "unavailable"
    display_astronaut_fx(astronauts)
    return astronauts

def return_mission(astronauts, display_astronaut_fx):
    human_returning = input("GEEZ, that's nice! 😄\n"
                            "Who has returned from mission?").upper()
    for astronaut in astronauts:
        if astronaut['name'] == human_returning:
            astronaut['mission'] = "unassigned"
            astronaut['status'] = "available"
    display_astronaut_fx(astronauts)
    return astronauts

def remove_astronaut(astronauts, display_astronaut_fx):
    remove_human = input("Oh no!😢 Who is leaving us?\n").upper()
    for astronaut in astronauts:
        if astronaut['name'] == remove_human:
            astronauts.remove(astronaut)
    display_astronaut_fx(astronauts)
    return astronauts




