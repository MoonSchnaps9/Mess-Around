# Print each number from 1 to 100
# If divisible by 3: print "Fizz"
# If divisible by 5: print "Buzz"
# If divisible by both 3 and 5: print "FizzBuzz"
# Otherwise: print the number

for number in range (1, 101, 1):
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)