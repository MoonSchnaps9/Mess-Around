print("Welcome to the tip calculator!")

total_bill = input("What was the total bill? $ ")
tip_user_want_to_give = input("How much tip would you like to give? 10, 12, or 15? ")
Number_of_People_to_Split_Bill = input("How many people to split the bill? ")

Total_bill_with_Tip = int(total_bill) + (int(tip_user_want_to_give) / 100) * int(total_bill)
Price_per_person = Total_bill_with_Tip / int(Number_of_People_to_Split_Bill)

Rounded_Price_per_Person = round(Price_per_person, 2)
print(f"Each person should pay: ${Rounded_Price_per_Person}")