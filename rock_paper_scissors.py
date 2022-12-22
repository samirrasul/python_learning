import random


def rock_paper_scissors_game():

    user_score = 0
    computer_score = 0
    options = ["rock", "scissors", "paper"]

    while (True):
        user_input = input("Enter Rock/Scissors/Paper or press Q to quit: ").lower()

        if user_input == "q":
            break

        if user_input not in options:
            continue

        computer_suggestion = options[random.randint(0,2)]

        if user_input == "rock" and computer_suggestion == "paper" or user_input == "paper" and computer_suggestion == "scissors" or user_input == "scissors"and computer_suggestion == "rock":
            computer_score += 1
            print("Computer Won!")
            print(f"You - {user_score}, {computer_score} - Computer")
        
        if user_input == "paper" and computer_suggestion == "rock" or user_input == "scissors" and computer_suggestion == "paper" or user_input == "rock" and computer_suggestion == "scissors":
            user_score += 1
            print("You Won!")
            print(f"You - {user_score}, {computer_score} - Computer")

        elif user_input == computer_suggestion:
            print("Draw!")
            print(f"You - {user_score}, {computer_score} - Computer")


rock_paper_scissors_game()