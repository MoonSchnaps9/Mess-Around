# Prime Number Checker
# Prime numbers are numbers that can only be cleanly divided by themselves and 1. Wikipedia  

# You need to write a function called is_prime() that checks whether if the number passed into it is a prime number or not.  It should return True or False.
# e.g.
# 7 is a primer number because it is only divisible by 1 and itself.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.
# Note: 2 is a prime number because it's only divisible by 1 and itself, but 1 is not a prime number because it is only divisible by 1.

# Example Input 1
# 73
# Example Output 1
# True

# Example Input 2
# 75
# Example Output 2
# False

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

num = int(input("What is your number?\n"))
number_match = []

def is_prime(number_match, num):
    def check_loop(num):
        for number in range (num):
            if num % (number + 1) == 0:
                number_match.append(number + 1)
    check_loop(num)
    if len(number_match) > 2:
        return False
    elif len(number_match) == 2:
        return True
    elif len(number_match) <2:
        return False

print(is_prime(number_match, num))