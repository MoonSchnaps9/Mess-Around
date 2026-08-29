# Final Exercise — Space Station Resource Manager
#
# Build a resource management system for a space station.
#
# Data structure to start with:
# - A dictionary of crew members, each with a name, role, and status
# - A dictionary of resources with current stock levels
# - A log (list) of all transactions
#
# Functions required (each must return a value):
#   1. display_status(crew, resources) — prints crew and resource overview
#   2. add_resource(resources, item, quantity) — adds stock, logs the transaction
#   3. consume_resource(resources, log, item, quantity) — removes stock if available,
#      warns if not enough, logs the transaction
#   4. add_crew(crew, name, role) — adds a new crew member as "Active"
#   5. update_crew_status(crew, name, status) — updates a crew member's status
#      ("Active", "On EVA", "Injured", "Off Duty")
#   6. mission_report(crew, resources, log) — prints a full summary:
#      active crew count, critical resources (stock below 5), and last 3 log entries
#
# Requirements:
#   - All input handled via function parameters, not input() inside functions
#   - found = False pattern where needed
#   - Handle all edge cases: item not found, crew member not found,
#     invalid status, insufficient stock
#   - Call every function at least twice with different arguments to prove it works

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from os import system
space_station_crew = {
    "crew_1": {"name": "thomas pesquet", "role": "commander", "status": "Off Duty"},
    "crew_2": {"name": "sophie adenot", "role": "spacewalker", "status": "lol"},
    "crew_3": {"name": "peggy whitson", "role": "flight engineer", "status": "Active"}
}


space_station_resources = {
    "food": 58,
    "oxygen": 95,
    "water": 4,
    "electricity": 24,
    "data bandwidth": 56
}

log_list = []

def display_status(crew, resources):
    print(f"This is the current status of:\n"
          "- The Crew members on the ISS\n" \
          "- The Resources on the ISS\n")
    
    for index in crew:
        print(f"\nName: {crew[index]['name']}")
        print(f"Role: {crew[index]['role']}")
        print(f"Status: {crew[index]['status']}\n")

    for resource in resources:
        print(f"{resource}: {resources[resource]}")
    return crew, resources

def add_resource(resources, item, quantity, log):
    found = False
    for resource in resources:
        if item == resource:
            resources[resource] += quantity
            found = True
            log.append(f"User has increased {resource} by {quantity}")
                       
    if found == False:
        print("This resource is not available in our current databe. Try again")

    return resources, log

def consume_resource(resources, item, quantity, log):
    found = False
    for resource in resources:
        if resource == item:
            if resources[resource] - quantity < 0:
                print("You can't do this, as you would create a black hole by going under 0 🧐")
                found = True
            else:
                resources[resource] -= quantity
                found = True
                log.append(f"User has consumed {resource} by {quantity}")

    if found == False:
        print("This resource is not available in our current database. Try again")

    return resources, log

def add_crew(crew, name, role):
    check_length = str(len(crew)+ 1)
    crew[f"crew_{check_length}"] = {"name": name, "role": role, "status": "Active"}
    return crew

def updated_crew_status(crew, name, status):

    if status != "Active" and status != "On Eva" and status != "Injured" and status !="Off Duty":
        print("Invalid status, please try again")
        return crew
    
    found = False
    for resource in crew:
        if name == crew[resource]["name"]:
            crew[resource]['status'] = status
            found = True

    if found == False:
        print("This person is not available in our current database. Try again")

    return crew

def mission_report(crew, resources, log):
    for member in crew:
        if crew[member]["status"] == "Active":
            print(F"{crew[member]['name']} is currently Active and ready for assignment!")

    for item in resources:
        if resources[item] < 5:
            print(F"{item} has almost run out! We have {resources[item]}")

    for data in range(3):
        print(log[data +(len(log)-3)])

# quantity = int(input("How many?\n"))
# item = input("What?\n").lower()
# name = input("Who?\n").lower()
# role = input("Duty?\n").lower()
# status = input("Choose the status: 'Active', 'On Eva', 'Injured', 'Off Duty'\nHere: ").lower().title()

#ADD RESOURCE PATH
display_status(space_station_crew, space_station_resources)

quantity = int(input("How many?\n"))
item = input("What?\n").lower()
add_resource(space_station_resources, item, quantity, log_list)

system('clear') #Clear the system

display_status(space_station_crew, space_station_resources)

quantity = int(input("How many?\n"))
item = input("What?\n").lower()
add_resource(space_station_resources, item, quantity, log_list)

system('clear') #Clear the system

#CONSUMER RESOURCE PATH
display_status(space_station_crew, space_station_resources)

quantity = int(input("How many?\n"))
item = input("What?\n").lower()
consume_resource(space_station_resources, item, quantity, log_list)

system('clear') #Clear the system

display_status(space_station_crew, space_station_resources)

quantity = int(input("How many?\n"))
item = input("What?\n").lower()
consume_resource(space_station_resources, item, quantity, log_list)

system('clear') #Clear the system

#ADD CREW PATH
display_status(space_station_crew, space_station_resources)

name = input("Who?\n").lower()
role = input("Duty?\n").lower()
add_crew(space_station_crew, name, role)

system('clear') #Clear the system

display_status(space_station_crew, space_station_resources)

name = input("Who?\n").lower()
role = input("Duty?\n").lower()
add_crew(space_station_crew, name, role)

system('clear') #Clear the system

#UPDATED STATUS PATH
display_status(space_station_crew, space_station_resources)

name = input("Who?\n").lower()
status = input("Choose the status: 'Active', 'On Eva', 'Injured', 'Off Duty'\nHere: ").lower().title()
updated_crew_status(space_station_crew, name, status)

system('clear') #Clear the system

display_status(space_station_crew, space_station_resources)

name = input("Who?\n").lower()
status = input("Choose the status: 'Active', 'On Eva', 'Injured', 'Off Duty'\nHere: ").lower().title()
updated_crew_status(space_station_crew, name, status)

system('clear') #Clear the system

mission_report(space_station_crew, space_station_resources, log_list)

