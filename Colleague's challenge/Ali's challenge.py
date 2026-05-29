#For loop challenge: Try to build this with a For loop:
# *
# ***
# *****
# *******
# *********

# print("*")

# final_list = ["*"]

# for stars in range(2):
#     final_list.append("*")
#     final_list.append("*")
#     for space in range(2):
#         final_list[space] = " "
#         print(*final_list)


#-------------------
# starting_star = "*"
# variable_star = ""

# print(starting_star)

# for space_step in range(2):
#     variable_star += " "
#     for step in range(2):
#         variable_star += "**"
#         print(variable_star)

# books = ["Dune", "1984", "The Martian"]

# print(books[0])


#---------------------

star_list = [" ", "*", " "]

# print(*star_list)
# star_list[len(star_list) - 1] = "B"
# print(*star_list)
# print(star_list)
# for star in range(2):
#     star_list.insert(0, " ")
#     star_list.append(" ")
#     for space in range(2):
#         star_list[space + 1] = "*"
#         star_list[len(star_list) - 1] = "*"
#         print(star_list)

#---------------------

# star_list_start_point = [" ", "*", " "]
# star_list_ongoing_change = ["*"]
# number_of_try = 2
# # print(star_list_start_point)

# for star in range(number_of_try):
#     star_list_ongoing_change.insert(0, " ")
#     star_list_ongoing_change.append(" ")
#     print(star_list_ongoing_change)
#     for first_space in range(1):
#         star_list_ongoing_change[first_space] = "*"
#         star_list_ongoing_change[len(star_list_ongoing_change) - 1] = "*"
#         print(star_list_ongoing_change)
        
#---------------------

#This is just to ask how many times the for loop will run. Since this is a challenge for Ali, special joke for him :D
number_of_try = int(input("Hey Ali, can you please choose a habibi number?\n"))

#I learned with ClaudeAI how a nested loop work, as I had not had the occasion to work with one before. It gave me an example:

#Me -> Ok so the first for loop runs until it reaches the second loop that will run like not limit until it's done, then the first loop runs again until it reaches the second loop that will run like not limit until it's done?
# Claude -> Exactly right — that's the perfect mental model.
# Outer loop moves one step → inner loop runs completely → outer loop moves one step → inner loop runs completely again → and so on until the outer loop finishes.

#Based on this explanation, as we want at first to have the basic list, I created the starting point
for star in range(1):
    star_list_ongoing_change = ["*"]

#Then, I tried (above) to first add the spaces progressively. I didn't get any good result. So I asked ClaudeAI for the smallest hint possible (and that's the only one it gave me):
# The number of spaces should decrease as you go down, not stay the same or increase.

#Then, I reversed my logic, and wrote this code so we already know how many spaces need to be added based on the input above 
    for number in range(number_of_try):
        star_list_ongoing_change.insert(0, " ")
        star_list_ongoing_change.append(" ")
    print(*star_list_ongoing_change)

#Now that the spaces are in place. The rest of the code is to first, check where the start is in the list:
# Once I have the position, we just add a "*" to the position of the current star - 1
    for space in range(number_of_try):
        star_position_left = star_list_ongoing_change.index("*")
        star_list_ongoing_change[star_position_left - 1] = "*"
#This is where I got lucky a bit. After some thoughts, I was curious to see if len() function - where the index of the current star (before adding * on the left) would give the correct position.. and yes! :D
        star_position_right = len(star_list_ongoing_change) - star_position_left
        star_list_ongoing_change[star_position_right] = "*"
        print(*star_list_ongoing_change)

#I tried to understand why it would work, and it is because len() returns +1 compare to index (as index counts from 0 and index 1)