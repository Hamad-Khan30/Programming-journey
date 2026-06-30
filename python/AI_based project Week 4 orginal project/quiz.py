import random

class Quiz:
    def __init__(self):
        self.score = 0

    def start_quiz(self, flashcards, number_of_questions):
        self.score = 0
        if len(flashcards) > number_of_questions:
            questions = random.sample(flashcards, number_of_questions)
        else:
            questions = flashcards

        for index, card in enumerate(questions, start=1):
            print(f"\nQuestion {index}: {card.question}")
            answer = input("Your Answer: ").strip()

            if answer.lower() == card.answer.lower():
                print("Correct!")
                self.score += 1
            else:
                print("Wrong!")
                print("Correct Answer:", card.answer)

        print(f"Score : {self.score}/{len(questions)}")