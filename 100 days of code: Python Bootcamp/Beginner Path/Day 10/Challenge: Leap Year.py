# Leap Year
# ─────────
# Write a function that returns True or False whether a given year is a leap year.

# RULES:
# - Divisible by 4 with no remainder → Leap year
# - EXCEPT divisible by 100 with no remainder → Not a leap year
# - UNLESS also divisible by 400 with no remainder → Leap year

# EXAMPLES:
# 2000 → True
# 2100 → False
# 1989 → False

# WARNING: Your return must be a boolean (True/False), not a string.

# ─────────────────────────────

# def is_leap_year(year):
#   # your code here

# is_leap_year(2400)
# is_leap_year(1989)

def is_leap_year(year):
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

print(is_leap_year(int(input("Year?"))))
