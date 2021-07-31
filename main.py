from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

# feed in the data to the model
for question in question_data:
    new_question = Question(q_text=question["text"], q_answer=question["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.display_score()
