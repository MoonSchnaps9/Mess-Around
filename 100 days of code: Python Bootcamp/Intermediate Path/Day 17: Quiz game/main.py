from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

#Write a FOR loop to iterate over the question_data.
#Create a Question object from each entry in question_data.
#Append each Question object to the question_bank.

question_bank = []

for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've finished the quiz!\n" \
F"Your final score is {quiz.score}/{quiz.question_number}.")

