#Create a class called QuizBrain
# Write an __init__() method
# Initialise the question_number to 0
# Initialise the question_list to an input

class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank

#Retrieve the item at the current question_number from the question_list
#use the input() function to show the user the question text and ask for the user's answer
    
    def next_question(self):
        user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?: ")
        self.question_number += 1