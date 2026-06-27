# Project: Space Crew Mission Planner
# You have these lists:
import random
crew_names = ["Yuri", "Valentina", "Neil", "Buzz", "Christa", "Sally", "Mae", "Scott"]
missions = ["ISS Resupply", "Lunar Orbit", "Mars Flyby", "Deep Space Probe", "Satellite Repair"]
roles = ["Commander", "Pilot", "Flight Engineer", "Mission Specialist", "Science Officer"]

# Write a program that:

# Asks the user how many crew members to assign
# Randomly assigns each crew member a mission and a role — no repeated crew members
# Asks the user for a mission duration in days
# Calculates how many weeks and remaining days that is
# Prints the full crew manifest and mission duration

#--------------------------------------------------------------------------------------------------------------------------


number_of_crew_members_needed = int(input("How many crew members to assign?\n"))
if number_of_crew_members_needed > 8:
    print("You have only 8 crew members. It can't be more than 8. Please, try again!")
else:
    mission_length_in_days = int(input("How long the mission should last? In Days please \n"))
    
    crew_member_list = random.sample(crew_names, number_of_crew_members_needed)
    
    final_crew_member = ""
    final_mission = ""
    final_roles= ""
    
    for missionform in range(number_of_crew_members_needed):
        final_crew_member = crew_member_list[missionform]
        final_mission = random.choice(missions)
        final_roles = random.choice(roles)
        print(f"{missionform + 1}. {final_crew_member} | {final_mission} | {final_roles}")
    
    length_in_weeks = (mission_length_in_days // 7)
    length_in_days = mission_length_in_days % 7
    print(f"Mission duration: {mission_length_in_days} days: {length_in_weeks} weeks and {length_in_days} days")


#First attempt! ClaudeAI helped though with the "//" vs "round", because I used "round" but it would give a wrong number
