#Added this later during this project -> to clear the terminal
from os import system



#1: Write out the other 4 functions - subtract, mulptiply and divide

def addition(n1, n2):
    result = n1 + n2
    return result

def subtract(n1, n2):
    result = n1 -n2
    return result

def multiply(n1, n2):
    result = n1 * n2
    return result

def divide(n1, n2):
    result = n1 / n2
    return result

#2: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

maths_operation = {
    "+": addition,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

#3: Use the dictionary operations to perform the calculations (Mulptiply 4 * 8 using the dictionary)

print(maths_operation["*"](4, 8))

# Calculator - Day 10
# ────────────────────
# Build a calculator that can perform addition, subtraction, multiplication and division.

# Demo: https://appbrewery.github.io/python-day10-demo/

# FUNCTIONALITY:
# - Program asks the user to type the first number.
# - Program asks the user to type a mathematical operator ("+", "-", "*" or "/").
# - Program asks the user to type the second number.
# - Program works out the result based on the chosen mathematical operator.
# - Program asks if the user wants to continue working with the previous result.
#   - If yes: program loops and uses the previous result as the first number, then repeats the calculation process.
#   - If no: program asks the user for the first number again and wipes all memory of previous calculations.

#----------------------------------------------------------------------------------------------------------------------------------


game = True

while game:
#ask user to choose the first number
    user_first_number = int(input("What's your first galactic number?: "))

#Display the list of operators
    for operator in maths_operation:
        print(operator)

#aks user to choose the mathematical operator
    user_operation_choice = input("Pick an operation: ")

    #ask the user to choose the second number
    user_second_number = int(input("What's your second galactic number?: "))

    #Calculation
    result = maths_operation[user_operation_choice](user_first_number, user_second_number)
    print(f"{user_first_number} {user_operation_choice} {user_second_number} = {result}")

    #ask user to choice if they want to continue working with the previous result
    user_choice_continue_previous_number = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

    #creating IF statement + While Loop
    if user_choice_continue_previous_number == "n":
        result = 0
        system("clear")
    elif user_choice_continue_previous_number == "y":
        #Creating another while loop so the user can still work with his previous number until he's done so it goes back to the previous loop
        game2 = True
        while game2:
            
            user_first_number = result
            
            #Display the list of operators
            for operator in maths_operation:
                print(operator)

            #aks user to choose the mathematical operator
            user_operation_choice = input("Pick an operation: ")
            
            #ask the user to choose the second number
            user_second_number = int(input("What's your second galactic number?: "))
            
            #Calculation
            result = maths_operation[user_operation_choice](user_first_number, user_second_number)
            print(f"{user_first_number} {user_operation_choice} {user_second_number} = {result}")
            
            #ask user to choice if they want to continue working with the previous result
            user_choice_continue_previous_number = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

            #If Statement + While loop
            if  user_choice_continue_previous_number == "n":
                result = 0
                game2 = False
