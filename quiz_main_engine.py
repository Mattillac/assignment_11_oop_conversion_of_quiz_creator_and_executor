from quiz_loader import QuizLoader
from quiz_executor import Quiz
from ascii_art import AsciiArt

def main():
    filename = "quiz.txt"
    questions = QuizLoader.load_quiz(filename)
    quiz = Quiz(questions)
    quiz.run()
    quiz.show_results()
    AsciiArt.thank_you()

if __name__ == "__main__":
    main()

