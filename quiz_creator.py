#class here
class QuizCreator:
#some def in here or using imports
#source code goes here
    def __init__(self):
        self.quiz_name = ""
        self.file = None

    def get_quiz_name(self):
        self.quiz_name = input("Enter the quiz name: ")
        if not self.quiz_name.endswith(".txt"):
            self.quiz_name += ".txt"
        self.file = open(self.quiz_name, "a")

    def add_question(self):
        question = input("Enter a question: ")
        answer_sheet = input("Enter the answer sheet like this (a, b, c, d (a) ) and enclose with parenthesis the correct answer!: ")
        self.file.write("Question: " + question + "\n")
        self.file.write("Answers and Correct Answer: " + answer_sheet + "\n\n")

def run(self):
        self.get_quiz_name()
        while True:
            self.add_question()
            more = input("Do you want to add more questions? [YES/NO]: ").upper()
            if more == "YES":
                continue
            elif more == "NO":
                break
            else:
                print("SHAME ON YOU WHY YOU DIDN'T FOLLOW THE INSTRUCTIONS")
                break
        self.file.close()
            print("File is saved! Thank you for using this program.")

#and create a different file for the main function