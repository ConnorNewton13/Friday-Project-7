def trivia_quiz():
    # Define a dictionary with trivia questions and answers
    questions = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "What is the largest planet in our solar system?": "Jupiter",
        "Who wrote 'Romeo and Juliet'?": "Shakespeare",
        "What is the chemical symbol for water?": "H2O"
    }

    print("Welcome to the Trivia Quiz!")
    
    # Loop through the questions in the dictionary
    for question, correct_answer in questions.items():
        print(question)  # Display the question
        user_answer = input("Your answer: ").strip()  # Get user's answer

        # Check if the answer is correct
        if user_answer.lower() == correct_answer.lower():  # Case insensitive check
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer is: {correct_answer}")
    
    print("\nThanks for playing the Trivia Quiz!")

if __name__ == "__main__":
    trivia_quiz()