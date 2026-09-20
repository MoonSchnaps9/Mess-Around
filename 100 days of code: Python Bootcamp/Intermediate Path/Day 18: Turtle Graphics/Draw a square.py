#Draw a square (100x100)
from turtle import Turtle, Screen
import heroes


vega = Turtle()
for _ in range(4):
    vega.forward(100)
    vega.right(90)

screen = Screen()
screen.exitonclick()