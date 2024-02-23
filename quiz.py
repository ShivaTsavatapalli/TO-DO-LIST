import random

# Quiz questions and answers
questions = {
    "What is the capital of France?": "Paris",
    "Who wrote Romeo and Juliet?": "William Shakespeare",
    "What is the largest mammal?": "Blue whale",
    "What is the tallest mammal?": "Giraffe",
    "What is the closest planet to the sun?": "Mercury"
}

def quiz():
    score = 0
    questions_list = list(questions.keys())

    print("Welcome to the Quiz Game!")
    print("Answer the following questions:")

    # Ask 5 random questions
    for _ in range(5):
        question = random.choice(questions_list)
        answer = questions[question]
        user_answer = input(f"\n{question}\nYour answer: ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {answer}")

        # Remove the question from the list to avoid repetition
        questions_list.remove(question)

    print("\nQuiz completed!")
    print(f"Your final score is: {score}/5")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        quiz()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    quiz()
