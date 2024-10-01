import random
import os 

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_encouragement():
    messages = [
        "You're getting closer! 🔍",
        "Keep trying, you got this! 💪",
        "Nice guess, but not quite there! 🚀",
        "Almost there, don't give up! 🌟"
    ]
    return random.choice(messages)

def start_game():
    clear_console()
    print("\n", "*" * 48)
    print(" " * 6, "WELCOME TO THE NUMBER GUESSING GAME!", " " * 6)
    print("", "*" * 48, "\n")
    
    print("Choose your difficulty level:")
    print("1. Easy (1 to 50, unlimited attempts)")
    print("2. Medium (1 to 100, 10 attempts)")
    print("3. Hard (1 to 100, 5 attempts)")
    
    difficulty = input("\nEnter your choice (1/2/3): ")
    if difficulty == '1':
        n = random.randint(1, 50)
        max_attempts = None
    elif difficulty == '2':
        n = random.randint(1, 100)
        max_attempts = 10
    elif difficulty == '3':
        n = random.randint(1, 100)
        max_attempts = 5
    else:
        print("Invalid choice! Defaulting to Medium difficulty.")
        n = random.randint(1, 100)
        max_attempts = 10
    
    print("\nGuess the number between the range based on your chosen difficulty!\n")
    a = -1
    guesses = 0

    while a != n:
        guesses += 1
        if guesses > max_attempts:
            print(f"Sorry, you've run out of attempts! The correct number was {n}.")
            break

        try:
            a = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if a > n:
            print("Lower number please! ❗", get_random_encouragement())
        elif a < n:
            print("Higher number please! ❗", get_random_encouragement())
        else:
            print(f"\n🎉 Congratulations! You've guessed the correct number in {guesses} attempts! 🎉")
            break

    if a != n:
        print("\nBetter luck next time! 😊")
    
    play_again = input("\nWould you like to play again? (y/n): ")
    if play_again.lower() == 'y':
        start_game()
    else:
        print("\n", "*" * 10, "Thank you for playing! Goodbye! 👋", "*" * 10, "\n")


start_game()
 
 