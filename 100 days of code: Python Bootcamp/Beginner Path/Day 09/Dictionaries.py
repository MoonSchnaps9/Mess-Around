programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "a piece of code that you can easily call over and over again.",
    }

print(programming_dictionary["Bug"])
print(programming_dictionary)

#Adding one more key
programming_dictionary["Loop"] =  "The action of doing something over and over again."
print(programming_dictionary)

#Creating empty dictionary
empty_dictionary = {}

#Wipe an entire dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A celestial song that messes around with your program"
print(programming_dictionary)

#loop through a dictionary
for key in programming_dictionary:
    print(programming_dictionary[key])

print(programming_dictionary[0])