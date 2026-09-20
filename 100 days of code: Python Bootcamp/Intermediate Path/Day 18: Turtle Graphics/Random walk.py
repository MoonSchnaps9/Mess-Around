#Create a random walk
#random colors
#Speed/thickness to be choosen before starting
import random
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

pensize = random.randint(0,15)
speed = random.randint(0,10)

vega.pensize(pensize)
vega.speed(speed)

for _ in range(50):
    vega.setheading(random.randint(0,360))
    vega.color(random.choice(colors))
    vega.forward(30)


useful = Screen()
useful.exitonclick()