class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.correct = 0
        self.question_list = q_list

    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {curr_question.text} (True/False):")
        if answer == curr_question.answer:
            self.correct += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def display_score(self):
        print(f"You got {self.correct} out of {len(self.question_list)} correct!")
