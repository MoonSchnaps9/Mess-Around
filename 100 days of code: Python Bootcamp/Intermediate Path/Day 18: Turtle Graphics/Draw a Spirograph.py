#Draw a spirograph
from turtle import Turtle, Screen
import random

vega = Turtle()
screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colors = (r, g , b)
    return colors


vega.speed(0)

for _ in range(36):
    colors = random_color()
    vega.color(colors)
    vega.left(10)
    vega.circle(100)





screen.exitonclick()