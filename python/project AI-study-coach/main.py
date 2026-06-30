import json

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return f"Question: {self.question}\nAnswer: {self.answer}"

class StudyCoach:
    def __init__(self):
        self.flashcards = []
        self.score = 0

    def add_flashcard(self, question, answer):
        card = Flashcard(question, answer)
        self.flashcards.append(card)

    def study_flashcards(self):

        for card in self.flashcards:
            print(f"\nQuestion: {card.question}")
            print(f"Answer: {card.answer}")

        print("\nYou have finished reading all flashcards.")

    def start_quiz(self):
        self.score = 0

        for card in self.flashcards:
            print("\n" + card.question)

            user_answer = input("Your Answer: ")

            if user_answer.strip().lower() == card.answer.strip().lower():
                print("Correct")
                self.score += 1
            else:
                print("Wrong")
                print("Correct Answer:", card.answer)

        print(f"\nFinal Score: {self.score}/{len(self.flashcards)}")

    def save_progress(self, topic):
        progress = {      "Topic": topic,      "Score": self.score,     "Total": len(self.flashcards)}

        with open("progress.json", "w") as f:
            json.dump(progress, f, indent=4)

        print("\nProgress Saved Successfully.")

    def load_progress(self):
        try:
            with open("progress.json", "r") as f:
                progress = json.load(f)

            print("-----------------------------")
            print("Previous Progress")
            print(f"Topic : {progress['Topic']}")
            print(f"Score : {progress['Score']}/{progress['Total']}")
            print("-----------------------------\n")

        except FileNotFoundError:
            print("No previous progress found.\n")


coach = StudyCoach()
coach.load_progress()

while True:

    coach.flashcards.clear()
    coach.score = 0

    print("\n===== AI Study Coach =====")
    print("1. Python")
    print("2. JSON")
    print("3. Both Topics")

    while True:
        choice = input("Choose Topic: ")

        if choice == "1":

            topic = "Python"
            coach.add_flashcard("What is Python?", "Python is a programming language.")
            coach.add_flashcard("Who created Python?", "Guido van Rossum")
            coach.add_flashcard("What keyword is used for loops?", "for")
            break

        elif choice == "2":

            topic = "JSON"
            coach.add_flashcard("What is JSON?", "JavaScript Object Notation.")
            coach.add_flashcard("Which module is used for JSON?", "json")
            coach.add_flashcard("Which function writes JSON to a file?", "json.dump")
            break

        elif choice == "3":

            topic = "Python + JSON"
            coach.add_flashcard("What is Python?", "Python is a programming language.")
            coach.add_flashcard("Who created Python?", "Guido van Rossum")
            coach.add_flashcard("What keyword is used for loops?", "for")

            coach.add_flashcard("What is JSON?", "JavaScript Object Notation.")
            coach.add_flashcard("Which module is used for JSON?", "json")
            coach.add_flashcard("Which function writes JSON to a file?", "json.dump")
            break

        else:
            print("Invalid Choice! Please enter only 1, 2 or 3.")

    coach.study_flashcards()

    while True:
        start = input("\nDo you want to start the quiz? (yes/no): ").strip().lower()

        if start == "yes":
            coach.start_quiz()
            coach.save_progress(topic)
            break
        elif start == "no":
            print("Study session finished.")
            break
        else:
            print("Invalid input! Please type only 'yes' or 'no'.")

    while True:
        again = input("\nDo you want to study another topic? (yes/no): ").strip().lower()

        if again == "yes":
            break
        elif again == "no":
            print("\nThank you for using AI Study Coach.")
            exit()
        else:
            print("Invalid input! Please type only 'yes' or 'no'.")