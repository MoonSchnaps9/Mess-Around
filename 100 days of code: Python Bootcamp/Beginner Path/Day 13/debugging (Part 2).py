from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])

#Randint was incorrect for 1-6 
#1 -> Because the value of ❶ in the list is 0 so never gets printed
#6 -> the maximum value in the list is 5 with ❻

#So 1-6 becomes 0-5