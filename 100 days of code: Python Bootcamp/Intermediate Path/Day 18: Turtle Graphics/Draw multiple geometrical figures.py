#Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
#The color changes once the form is drawn
from turtle import Turtle, Screen

vega = Turtle()

colors = [
    "red", 
    "orange", 
    "yellow", 
    "green", 
    "blue", 
    "purple", 
    "magenta", 
    "cyan", 
    "brown", 
    "black"
]

for step in range(3, 11):
    vega.color(colors[step - 3])
    angle = 360 / step
    for _ in range(step):
        vega.forward(100)
        vega.right(angle)



useful = Screen()
useful.exitonclick()

