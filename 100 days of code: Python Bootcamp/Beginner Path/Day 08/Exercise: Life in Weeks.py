# Life in Weeks - Day 8 Exercise
# Create a function called life_in_weeks(age)
# Calculate how many weeks are left if we live until 90
# Output format: "You have x weeks left."
# (exact punctuation required — full stop at the end)

def life_in_weeks(age):
    weeks_left = 4680-(age*52)
    print(f"You have {weeks_left} weeks left.")

life_in_weeks(35)

#Or weeks_left = (90 - age) * 52