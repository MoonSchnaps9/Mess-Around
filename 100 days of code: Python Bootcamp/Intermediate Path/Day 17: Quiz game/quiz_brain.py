#1ST INSTRUCTIONS
#Create a class called QuizBrain
# Write an __init__() method
# Initialise the question_number to 0
# Initialise the question_list to an input

class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank

#2ND INSTRUCTIONS
#Retrieve the item at the current question_number from the question_list
#use the input() function to show the user the question text and ask for the user's answer
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)?: ")
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

#3RD INSTRUCTIONS
#Create method called Still_has_question()
#Return a bolean depending on the value of question_number
#Use the while loop to show the next question until the end
    
    def still_has_question(self):
        return self.question_number < len(self.question_list)

#4TH Instructions
#Follow what Angela demonstrates, there's no instructions here

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
        else:
            print(" You got it wrong!")
        print(f"The correct answer was: {correct_answer}")

#5TH -> create the score tracking