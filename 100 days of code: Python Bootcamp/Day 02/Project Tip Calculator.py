print("Welcome to the tip calculator!")

total_bill = input("What was the total bill? $ ")
tip_user_want_to_give = input("How much tip would you like to give? 10, 12, or 15? ")
Number_of_People_to_Split_Bill = input("How many people to split the bill? ")

Final_price_per_person = (round,2((total_bill * int(tip_user_want_to_give / 100) ) / int(Number_of_People_to_Split_Bill)))
print(f"Each person should pay: ${Final_price_per_person}")
