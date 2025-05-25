#class here again
#since i have different parts and it was defined already so it'll be esay to be organized.
import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.results = []

    def run(self):
        if not self.questions:
            print("ERROR! No quiz data available.")
            return

        random.shuffle(self.questions)  # Shuffle questions

        for index, question in enumerate(self.questions, start=1):
            print(f"\nQuestion {index}: {question.question_text}")

            # Shuffle answers for display
            answers = question.answers[:]
            random.shuffle(answers)

            for i, ans in enumerate(answers, start=1):
                print(f"  {i}. {ans}")

            # Get user input
            while True:
                try:
                    choice = input(f"Your answer (1-{len(answers)}): ").strip()
                    if not choice:
                        raise ValueError
                    choice = int(choice)
                    if 1 <= choice <= len(answers):
                        selected = answers[choice - 1]
                        correct = question.is_correct(selected)
                        if correct:
                            print("NICE CORRECT!")
                            self.score += 1
                        else:
                            print(f"Sorry, NICE TRY THOUGH! The correct answer was: {question.correct_answer}")
                        self.results.append((question.question_text, selected, question.correct_answer, correct))
                        break
                    else:
                        print(f"Please enter a number between 1 and {len(answers)}")
                except ValueError:
                    print("Please enter a valid number.")

    def show_results(self):
        print(f"\nQuiz complete! YOUR RECORD!:{self.score}/{len(self.questions)}")
        print("\nQUIZ RESULTS:")

        for i, (question, your_answer, correct_answer, is_correct) in enumerate(self.results, start=1):
            status = " Correct" if is_correct else " Incorrect"
            print(f"\n{i}. {question}")
            print(f"   Your answer: {your_answer}")
            print(f"   Correct answer: {correct_answer}")
            print(f"   Result: {status}")

#define here 
#source code
#and other files when creating class and the main engine as well.