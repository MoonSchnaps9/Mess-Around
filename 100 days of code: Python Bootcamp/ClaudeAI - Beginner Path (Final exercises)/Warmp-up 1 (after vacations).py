# Write a function called celsius_to_fahrenheit(celsius) that converts a temperature and returns the result. 
# Then write a second function called describe_temperature(fahrenheit) that returns a string description:
# Below 32°F → "Freezing"
# 32–59°F → "Cold"
# 60–85°F → "Comfortable"
# Above 85°F → "Hot"
# Call both functions and print the description for these inputs: -10°C, 20°C, 37°C, 100°C.
# Formula: F = (C × 9/5) + 32


temperature_celsius = [-10, 20, 37, 100]

def describe_temperature(converted_temperature):
    if converted_temperature < 32:
        return F"Dear human, {converted_temperature}°F it's FREEZING geez, you're in Finland or what? 😠"

    elif 32 <= converted_temperature <=59:
        return F"A bit cold, but it would not kill a comsic snail... Eh? What? 😠"

    elif 60 <= converted_temperature <= 85:
        return F"This is what I am TALKING ABOUT! This is C.O.M.F.O.R.T, like our planet EARTH! (except during winter in Finland.. it's a cold chamber COUNTRY!"

    elif converted_temperature > 85:
        return F"Are you OK? You like sunburn? UV? Dryness? Being naked? I mean... that's HOT dude 😅"

def celsius_to_fahrenheit(temperature_celsius):
    for number in range(len(temperature_celsius)):
        temperature_celsius[number] = round(((temperature_celsius[number] * 9/5) + 32))
        print(F"Your temperature in Fahrenheit is {temperature_celsius[number]}°F")
        print(describe_temperature(temperature_celsius[number]))

celsius_to_fahrenheit(temperature_celsius)


#I went a bit "fancy" (for a beginner yes haha) and merged two functions into one. Not intended design :)