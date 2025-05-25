class QuizLoader:
    @staticmethod
    def load_quiz(filename):
        quiz = []
        try:
            with open(filename, 'r') as file:
                lines = [line.strip() for line in file.readlines() if line.strip()]
        except FileNotFoundError:
            print(f"ERROR! File '{filename}' not found.")
            return quiz

        looper = 0
        while looper < len(lines):
            if lines[looper].startswith("Question:"):
                question = lines[looper][len("Question:"):].strip()
                looper += 1

                if looper < len(lines) and lines[looper].startswith("Answers and Correct Answer():"):
                    answer_line = lines[looper][len("Answers and Correct Answer():"):].strip()
                    looper += 1

                    if "(" in answer_line and ")" in answer_line:
                        last_paren = answer_line.rfind('(')
                        correct_answer = answer_line[last_paren+1:answer_line.rfind(')')].strip()
                        all_answers = [a.strip() for a in answer_line[:last_paren].split(',') if a.strip()]

                        if correct_answer not in all_answers:
                            all_answers.append(correct_answer)

                        from quiz_questions import Question
                        quiz.append(Question(question, all_answers, correct_answer))
                else:
                    looper += 1
            else:
                looper += 1

        return quiz
