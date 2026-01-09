import random

def get_user_choice():
    choice = input("Enter rock, paper, or scissors: ").lower()
    if choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Try again.")
        return get_user_choice()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = decide_winner(user_choice, computer_choice)
    print(result)

play_game()
