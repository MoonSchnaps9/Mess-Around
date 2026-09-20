#Draw a square (100x100)
from turtle import Turtle, Screen


vega = Turtle()
for _ in range(4):
    vega.forward(100)
    vega.right(90)

screen = Screen()
screen.exitonclick()