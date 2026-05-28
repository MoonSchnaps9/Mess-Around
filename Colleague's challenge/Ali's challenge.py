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

star_list_start_point = [" ", "*", " "]
star_list_ongoing_change = ["*"]

# print(star_list_start_point)

for star in range(1):
    star_list_ongoing_change.insert(0, " ")
    star_list_ongoing_change.append(" ")
    print(star_list_ongoing_change)
    for first_space in range(1):
        star_list_ongoing_change[first_space] = "*"
        star_list_ongoing_change[len(star_list_ongoing_change) - 1] = "*"
        print(star_list_ongoing_change)

