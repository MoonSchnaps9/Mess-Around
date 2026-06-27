# Love Calculator - Day 8 Exercise
# Create a function called calculate_love_score(name1, name2)
# 1. Count how many times each letter in "TRUE" appears in both names combined
# 2. Count how many times each letter in "LOVE" appears in both names combined
# 3. Combine the two totals to make a 2-digit number and print it
# e.g. TRUE total = 5, LOVE total = 3 → Love Score = 53

def calculate_love_score(name1, name2):
    true_count = 0
    love_count = 0
    first_word = "TRUE"
    second_word = "LOVE"
    for letter in (name1 + name2).upper():
        if letter in first_word:
            true_count += 1
        if letter in second_word:
            love_count += 1
    
    love_score = str(true_count) + str(love_count)
    print(love_score)

calculate_love_score("Guillaume", "Luna")