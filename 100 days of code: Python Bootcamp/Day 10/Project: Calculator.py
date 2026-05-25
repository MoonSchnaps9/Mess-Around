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

