#1: Write out the other 4 functions - subtract, mulptiply and divide

def addition(n1, n2):
    result = n1 - n2
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

