from quiz_loader import QuizLoader 
from quiz_executor import Quiz
from ascii_art import AsciiArt
import os

def main():
    filename = input("Enter the quiz filename (e.g., quiz.txt): ").strip()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)

    print(f"Attempting to load file from: {filepath}")

    questions = QuizLoader.load_quiz(filepath)
    if not questions:
        print("No quiz data found or failed to load the file.")
        return

    quiz = Quiz(questions)
    quiz.run()
    quiz.show_results()
    AsciiArt.thank_you()

if __name__ == "__main__":
    main()
