def redText(text):
    return f"\033[31m{text}\033[0m"

def greenText(text):
    return f"\033[32m{text}\033[0m"

def blueText(text):
    return f"\033[34m{text}\033[0m"

def yellowText(text):
    return f"\033[33m{text}\033[0m"

def brownText(text):
    return f"\033[38;5;94m{text}\033[0m"  # ANSI code for a brownish color

def main():
    # Call each function and print the results
    print(redText("This text is red!"))
    print(greenText("This text is green!"))
    print(blueText("This text is blue!"))
    print(yellowText("This text is yellow!"))
    print(brownText("This text is brown!"))

    # User input for color choice and text
    color_choice = input("\nChoose a color (red, green, blue, yellow, brown): ").strip().lower()
    user_text = input("Enter the text you want to display: ")

    if color_choice == "red":
        print(redText(user_text))
    elif color_choice == "green":
        print(greenText(user_text))
    elif color_choice == "blue":
        print(blueText(user_text))
    elif color_choice == "yellow":
        print(yellowText(user_text))
    elif color_choice == "brown":
        print(brownText(user_text))
    else:
        print("Invalid color choice!")

if __name__ == "__main__":
    main()