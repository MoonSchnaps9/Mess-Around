# def greet():
#     print("Welcome to the Earth's Solar System!")
#     print("This system is very well-reputated for only one thing:")
#     print("its amazing cookies! :D")


# greet()

# #Function with one input

# def greet_with_name(name):
#     print(f"Hi {name}")


# greet_with_name("Ryan")

#Function with inputs (Positional arguments)
def greet_with(name, location):
    print(f"Hey {name}!")
    print(f"What is it like in {location}?")

greet_with("Guillaume", "Kyoto")

#Function with inputs (Keyword arguments)

def greet_with(name, location):
    print(f"Hey {name}!")
    print(f"What is it like in {location}?")

greet_with (location="Kyoto", name="Guillaume")