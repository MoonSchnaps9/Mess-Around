# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")

# my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# 2. When is the function meant to print "You got it"?
# 3. What are your assumptions about the value of i?


#-------
#How to debug
# -> either to add i + 1 or go to 21 and not 20 since i == 20 never happens in this configuration
def my_function():
    for i in range(1, 20):
        if i + 1 == 20:
            print("You got it")

my_function()