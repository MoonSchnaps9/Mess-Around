#Create a random walk
#random colors
#Speed/thickness to be choosen before starting
import random
from turtle import Turtle, Screen


vega = Turtle()
useful = Screen()

useful.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colors = (r, g , b)
    return colors

pensize = random.randint(1,15)
speed = random.randint(0,10)

vega.pensize(pensize)
vega.speed(speed)

for _ in range(50):
    colors = random_color()
    vega.setheading(random.randint(0,360))
    vega.color(colors)
    vega.forward(30)


useful.exitonclick()