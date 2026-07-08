# Project 1 — Space Quiz Game
# Build a quiz game with 10 space-themed questions
# Questions are stored as a list of dictionaries, each containing:
#   - "question": the question text
#   - "answer": the correct answer
#   - "options": a list of 4 possible answers (A, B, C, D)
# The game should:
#   - Ask each question one by one
#   - Display the 4 options
#   - Get the user's answer and check if it's correct
#   - Track the score throughout
#   - Show feedback after each question (correct/wrong + right answer)
#   - Display the final score at the end with a message based on performance
# Requirements:
#   - Questions stored in a list of dictionaries (no hardcoding in the game logic)
#   - At least one function that returns a value
#   - .upper() or .lower() on user input
#   - Score tracked with a variable updated inside a function

#--------------------------------------------------------------------------------------------------------------------------------------------------------
from art import logo

questions = [
    {
        "Question": "What is the brightest star in the night sky?",
        "Options": ["Betelgeuse", "Alpha Centauri", "Polaris", "Sirius"],
        "Answer": "Sirius"
    },
    {
        "Question": "Which NASA rover landed on Mars in 2021 alongside the Ingenuity helicopter?",
        "Options": ["Perseverance", "Curiosity", "Opportunity", "Spirit"],
        "Answer": "Perseverance"

    },
    {
        "Question": "Approximately how long does it take for light from the Sun to reach Earth?",
        "Options": ["8 seconds", "8 minutes", "8 hours", "8 days"],
        "Answer": "8 minutes"

    },
    {
        "Question": "What cosmic event occurs during a solar eclipse?",
        "Options": ["The Earth passes between the Sun and the Moon", "A star explodes in a supernova", "The Moon passes between the Earth and the Sun", "The Sun briefly burns out"],
        "Answer": "The Moon passes between the Earth and the Sun"
    },
    {
        "Question": "What is the currently accepted, estimated age of the universe?",
        "Options": ["4.6 billion years", "13.8 billion years", "100 billion years", "1 trillion years"],
        "Answer": "13.8 billion years"
    },
    {
        "Question": "What is the name of the boundary that marks the edge of the Sun's influence, where the solar wind meets the interstellar medium?",
        "Options": ["The Oort Cloud", "The Kuiper Belt", "The Event Horizon", "The Heliopause"],
        "Answer": "The Heliopause"
    },
    {
        "Question": "In what year was Pluto officially reclassified from a planet to a 'dwarf planet'?",
        "Options": ["1999", "2006", "2012", "2015"],
        "Answer": "2006"  
    },
    {
        "Question": "What specific type of galaxy is our Milky Way",
        "Options": ["Elliptical", "Barred Spiral", "Irregular", "Lenticular"],
        "Answer": "Barred Spiral" 
    },
    {
        "Question": "Which planet in our solar system has the most extensive and visible ring system?",
        "Options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
        "Answer": "Saturn" 
    },
    {
        "Question": "In astrophysics, what exactly is a pulsar?",
        "Options": ["A highly magnetized, rotating neutron star", "A dying red giant star", "A black hole emitting jets of gas", "A comet passing dangerously close to the Sun"],
        "Answer": "A highly magnetized, rotating neutron star"
    }
]

# print(logo)
# print(questions[0]["Question"])

# for question in range(len(questions)):
#     print(questions[question]["Question"])

def display_questions(questions, number):
    question = questions[number]["Question"]
    return question

def display_options(questions, number):
    labels = ["A", "B", "C", "D"]
    for index, option in enumerate(questions[number]["Options"]):
        print(f"{labels[index]}. {option}")

def convert_user_choice(user_choice, questions, number):
    labels = ["A", "B", "C", "D"]
    temporary_v_uchoice = labels.index(user_choice)
    user_choice = questions[number]["Options"][temporary_v_uchoice]
    return user_choice

def check_user_answer(question, number, user_choice, user_score):
    if user_choice == question[number]["Answer"]:
        user_score += 1
        print(F"I am not working for NASA.. but I know that your answer is CELESTIAL!\n Your current score: {user_score}")
        return user_score
    else:
        print(F"I am sad to announce that this is not the correct answer.. You don't believe me? NASA it geez 🧐\n Your current score: {user_score}")
        return user_score
    
user_score = 0

for step in range(len(questions)):
    print(display_questions(questions, step))
    display_options(questions, step)
    user_choice = input("You have to make a Celestial guess mate\n").upper()
    user_choice = convert_user_choice(user_choice, questions, step)
    user_score = check_user_answer(questions, step, user_choice, user_score)