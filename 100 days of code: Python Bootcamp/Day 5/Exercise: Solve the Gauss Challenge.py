#Gauss Challenge
#Work out the total of the number between 1 and 100, inclusive of both 1 and 100

total = 0
for number in range (1, 101, 1):
#I know ",1" is redundant, but this is for me to understand the range()
    total += number

print(total)