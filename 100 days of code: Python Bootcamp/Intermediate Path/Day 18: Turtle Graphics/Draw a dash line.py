#Draw a dash line with Turtle
from turtle import Turtle

vega = Turtle()

for _ in range(50):
    vega.pendown()
    vega.forward(10)
    vega.penup()
    vega.forward(10)

