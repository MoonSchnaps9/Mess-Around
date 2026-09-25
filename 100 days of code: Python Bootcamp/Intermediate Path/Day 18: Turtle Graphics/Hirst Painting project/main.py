import colorgram

colors = colorgram.extract('/Users/gschnaps/Documents/Code/Mess-Around/100 days of code: Python Bootcamp/Intermediate Path/Day 18: Turtle Graphics/Hirst Painting project/image.jpg',100)
list_of_colors = []


for color in colors:
    rgb = color.rgb

    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]

    final_result = (red, green, blue)

    list_of_colors.append(final_result)


print(list_of_colors)

final_color_list = [(222, 232, 226), (208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70), (187, 93, 105), (187, 139, 170), (84, 123, 181), (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72), (45, 74, 78), (161, 202, 220), (80, 73, 44), (57, 131, 121), (218, 176, 188), (220, 183, 166), (166, 207, 165), (179, 188, 211), (149, 37, 35), (46, 73, 71), (45, 65, 62)]