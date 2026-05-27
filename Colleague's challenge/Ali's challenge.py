#For loop challenge: Try to build this with a For loop:
# *
# ***
# *****
# *******
# *********

print("*")

final_list = ["*"]

for stars in range(2):
    final_list.append("*")
    final_list.append("*")
    print(*final_list)
    for space in range(2):
        final_list[space] = " "

print(final_list)