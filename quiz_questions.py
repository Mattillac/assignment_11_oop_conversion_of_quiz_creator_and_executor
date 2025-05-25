class Question:
    def __init__(self, question_text, answers, correct_answer):
        self.question_text = question_text
        self.answers = answers
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        return answer == self.correct_answer
