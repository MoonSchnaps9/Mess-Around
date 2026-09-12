from data import question_data
from question_model import Question

#Write a FOR loop to iterate over the question_data.
#Create a Question object from each entry in question_data.
#Append each Question object to the question_bank.

question_bank = []

for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

print(question_bank[0].text)