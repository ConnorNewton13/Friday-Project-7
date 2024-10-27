import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Asking the user if they want to play
    play = input("Do you want to play? (yes/no): ").strip().lower()

    if play == "no":
        print("Maybe next time!")
        return  # End the program

    elif play == "yes":
        # Generate a secret number between 1 and 10
        secret_number = random.randint(1, 10)
        guess = None  # Initialize guess

        # Loop until the user guesses correctly
        while guess != secret_number:
            try:
                guess = int(input("Guess a number between 1 and 10: "))

                if guess == secret_number:
                    print("Congratulations! You've guessed the number!")
                else:
                    print("Try again!")
            except ValueError:
                print("Please enter a valid number.")

    else:
        print("Invalid input. Please type 'yes' or 'no'.")

    print("Thanks for playing the Number Guessing Game. Goodbye!")

if __name__ == "__main__":
    number_guessing_game()