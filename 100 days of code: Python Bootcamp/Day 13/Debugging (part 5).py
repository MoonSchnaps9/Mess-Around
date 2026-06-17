# Debugging Leap Year
# - Read the code in exercise.py
# - Spot the problems 🐞.
# - Modify the code to fix the program.   

# Fix the code so that it works and when you hit submit it should pass all the tests. 

# This is how you work out whether if a particular year is a leap year.

# - on every year that is divisible by 4 with no remainder
# - except every year that is evenly divisible by 100 with no remainder
# - unless the year is also divisible by 400 with no remainder

# You can paste the code into PyCharm to help you debug.


def is_leap(year):
    if year % 4 == 0:
        if year % 100 != 0:
            result = True
            return result
        elif year % 400 == 0:
            result = True
            return result
        elif year % 400 != 0:
            result = False
            return result
    else:
        result = False
        return result

    
print(is_leap(2021))

    
