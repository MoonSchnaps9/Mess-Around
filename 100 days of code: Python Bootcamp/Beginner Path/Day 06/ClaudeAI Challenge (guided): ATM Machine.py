# Step 1: Define a function called greet that prints a welcome message. Then call it below the definition.
balance = 1000

def greet():
    print("Welcome to the PyBank ATM!")

# Step 2: Now define a function called check_balance that takes one parameter called balance and prints it. Then call it with a starting balance of 1000.

def check_balance(balance):
    print(f"Account balance: {balance}")

# Step 3: Define a function called deposit that takes two parameters — balance and amount. It should add amount to balance and return the new balance. 
# Then call it and print the result.

def deposit(balance, amount):
    result = balance + amount
    print(f"New balance {result}")
    return result
    
# Step 4: Now define a withdraw function. Same idea as deposit but it subtracts. 
# Add one condition — if the amount is greater than the balance, print "Insufficient funds" instead of processing the withdrawal.

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient funds")
    else:
        result = balance - amount
        print(f"New balance {result}")
        return result

# Step 5: Now build the ATM menu using a while loop. 
# Ask the user to choose an option, and call the right function based on their choice. Start with a balance of 1000.

power = True
greet()
while power:
    print("1. Check balance\n2. Deposit\n3. Withdraw")
    user_choice = int(input("Which options do you need?"))
    if user_choice == 1:
        check_balance(balance)
    elif user_choice == 2:
        amount_user_wants_to_add = int(input("Amount?"))
        balance = deposit(balance, amount_user_wants_to_add)
    elif user_choice == 3:
        amount_user_wants_to_writhdraw = int(input("Amount?"))
        balance = withdraw(balance, amount_user_wants_to_writhdraw)
    if user_choice == 4:
        power = False