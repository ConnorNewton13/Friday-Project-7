import random

def generate_powerball_numbers():
    print("Welcome to the PowerBall Number Generator!")
    print("This program will generate your PowerBall ticket numbers.")

    # Generating five white ball numbers (1-69)
    white_ball_1 = random.randint(1, 69)
    white_ball_2 = random.randint(1, 69)
    white_ball_3 = random.randint(1, 69)
    white_ball_4 = random.randint(1, 69)
    white_ball_5 = random.randint(1, 69)

    # Generating one red ball number (1-26)
    red_ball = random.randint(1, 26)

    # Formatting the output
    ticket_numbers = f"{white_ball_1} {white_ball_2} {white_ball_3} {white_ball_4} {white_ball_5}   {red_ball}"
    
    print("\nYour PowerBall ticket numbers are:")
    print(ticket_numbers)
