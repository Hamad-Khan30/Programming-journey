from flashcard import Flashcard
from quiz import Quiz
from ai import generate_flashcards
import json

class Studycoach:

    def __init__(self):

        self.flashcards = []
        self.all_flashcards = []
        self.study_topics = []
        self.quiz = Quiz()

    def add_flashcard(self, question, answer):
        card = Flashcard(question, answer)

        self.flashcards.append(card)
        self.all_flashcards.append(card)

    def get_flashcards(self, topic):
        cards = generate_flashcards(topic)
        if not cards:
            print("No flashcards generated.")
            return False

        for card in cards:
            self.add_flashcard(card["question"],card["answer"])

        return True

    def study_flashcards(self):

        for index, card in enumerate(self.flashcards, start=1):
            print(f"\nFlashcard {index}")
            print(card)

        print("\nYou have finished reading this topic.")

    def save_progress(self):
        progress = {"topics": self.study_topics,"score": self.quiz.score}

        with open("progress.json", "w") as file:
            json.dump(progress, file, indent=4)

        print("\nProgress Saved Successfully.")

    def load_progress(self):
        try:

            with open("progress.json", "r") as file:
                progress = json.load(file)

            print("Topics :", progress["topics"])
            print("Last Score :", progress["score"])

        except FileNotFoundError:
            print("No previous progress found.\n")

    def start(self):
        self.load_progress()

        while True:
            self.flashcards.clear()

            while True:
                topic = input("\nEnter Topic : ").strip()

                if topic == "":
                    print("Topic cannot be empty.")
                else:
                    break

            self.study_topics.append(topic)
            print("\nGenerating Flashcards\n")

            success = self.get_flashcards(topic)
            if not success:
                continue

            self.study_flashcards()

            while True:
                quiz_choice = input("\nDo you want to start the quiz? (yes/no): ").strip().lower()

                if quiz_choice == "yes":
                    self.quiz.start_quiz(self.flashcards,5)

                    break

                elif quiz_choice == "no":
                    print("Quiz skipped.")
                    break

                else:
                    print("Please type only yes or no.")

            while True:
                another = input("\nDo you want to study another topic? (yes/no): ").strip().lower()

                if another == "yes":
                    break

                elif another == "no":

                    if len(self.study_topics) >= 2:
                        while True:
                            combined = input("\nDo you want to take a Combined Quiz? (yes/no): ").strip().lower()

                            if combined == "yes":
                                self.quiz.start_quiz(self.all_flashcards,10)

                                break

                            elif combined == "no":
                                break

                            else:
                                print("Please type only yes or no.")

                    self.save_progress()
                    print("\nThank you for using AI Study Coach.")
                    return
                else:
                    print("Please type only yes or no.")