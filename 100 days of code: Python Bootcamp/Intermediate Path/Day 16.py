# import turtle

# franklin = turtle.Turtle()

# from turtle import Turtle, Screen

# franklin = Turtle()
# print(franklin)
# franklin.shape("turtle")
# franklin.color("cyan")
# franklin.forward(100)
# my_screen = Screen()
# my_screen.canvheight
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)