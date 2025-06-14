from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in range(len(question_data)):
    new_q = Question(question_data[i]["question"], question_data[i]["correct_answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    if not quiz.still_has_questions():
        print("You've completed the Quiz.")
        print(f"Your Final score is: {quiz.score}/{quiz.question_num}")
