import random

def get_user_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0

    for _ in range(3):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}.")
        print(f"The computer chose {computer_choice}.")
        round_winner = determine_winner(user_choice, computer_choice)
        print(round_winner)

        if round_winner == "You win!":
            user_score += 1
        elif round_winner == "Computer wins!":
            computer_score += 1

        print(f"Current score: Human - {user_score} Computer - {computer_score}\n")

    print("Game over!")
    if user_score > computer_score:
        print("You are the overall winner!")
    elif user_score < computer_score:
        print("Computer is the overall winner!")
    else:
        print("It's a tie!")

play_game()
