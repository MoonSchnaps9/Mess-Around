# import colorgram

# colors = colorgram.extract('/Users/gschnaps/Documents/Code/Mess-Around/100 days of code: Python Bootcamp/Intermediate Path/Day 18: Turtle Graphics/Hirst Painting project/image.jpg',100)
# list_of_colors = []


# for color in colors:
#     rgb = color.rgb

#     red = rgb[0]
#     green = rgb[1]
#     blue = rgb[2]

#     final_result = (red, green, blue)

#     list_of_colors.append(final_result)

# print(list_of_colors)
from turtle import Turtle, Screen
import random

vega = Turtle()
hard_stop = Screen()
hard_stop.colormode(255)

final_color_list = [(208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70), (187, 93, 105), (187, 139, 170), (84, 123, 181), (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72), (45, 74, 78), (161, 202, 220), (80, 73, 44), (57, 131, 121), (218, 176, 188), (220, 183, 166), (166, 207, 165), (179, 188, 211), (149, 37, 35), (46, 73, 71), (45, 65, 62)]



                                                                                    # Final Solution #    
y_position = -100
x_position = -100

vega.hideturtle()
vega.penup()
vega.goto(x_position, y_position)

for _ in range(10):
    for _ in range(10):
        vega.dot(20,random.choice(final_color_list))
        vega.hideturtle()
        vega.forward(50)
    y_position += 50
    vega.goto(x_position, y_position)


                                                                                    # WHAT I CAME UP WITH BEFORE CLAUDEAI HINTS#    
# drawing = True
# while_loop_counter = 0
# going_up = 0
# number_color = 0
# vega.penup()

# while drawing:
#     for step in range(10):
#        if while_loop_counter != len(final_color_list):
#         vega.dot(20,final_color_list[number_color])
#         vega.forward(50)
#         number_color += 1
#         while_loop_counter += 1
#        else:
#           drawing = False
#     going_up += 50
#     vega.left(90)
#     vega.forward(50)
#     vega.setposition(0, going_up)
#     vega.right(90)
   


# vega.penup()
# vega.dot(20,final_color_list[0])
# vega.forward(50)
# vega.dot(20,final_color_list[1])
# vega.forward(50)
# vega.dot(20,final_color_list[2])
# vega.forward(50)
# vega.dot(20,final_color_list[3])
# vega.left(90)
# vega.forward(50)
# vega.setposition(0, 50)
# vega.right(90)
# vega.dot(20,final_color_list[4])
# vega.forward(50)
# vega.dot(20,final_color_list[5])
# vega.forward(50)
# vega.dot(20,final_color_list[6])
# vega.forward(50)
# vega.left(90)
# vega.forward(50)
# vega.setposition(0, 100)
# vega.right(90)

hard_stop.exitonclick()