# Step 1: Define a function called greet that prints a welcome message. Then call it below the definition.

def greet():
    print("Welcome to the PyBank ATM!")

greet()

# Step 2: Now define a function called check_balance that takes one parameter called balance and prints it. Then call it with a starting balance of 1000.

def check_balance(balance):
    print(f"Account balance: {balance}")

check_balance(1000)

# Step 3: Define a function called deposit that takes two parameters — balance and amount. It should add amount to balance and return the new balance. 
# Then call it and print the result.

def deposit(balance, amount):
    result = balance + amount
    print(f"New balance {result}")
    return result
    

deposit(1000, 20)

# Step 4: Now define a withdraw function. Same idea as deposit but it subtracts. 
# Add one condition — if the amount is greater than the balance, print "Insufficient funds" instead of processing the withdrawal.

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient funds")
    else:
        result = balance - amount
        print(f"New balance {result}")
        return result

withdraw(1000, 500)

