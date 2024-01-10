import random

var = ["rock", "paper", "scissors"]
a = 0  # user points
b = 0  # computer points

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in var:
            return user_choice
        else:
            print("Invalid choice. Please choose from rock, paper, scissors.")

def get_computer_choice():
    computer_choice = random.choice(var)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    global a, b  # Declare a and b as global variables
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        a += 1
        print("You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        a += 1
        print("You win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        a += 1
        print("You win!")
    else:
        b += 1
        print("Computer won")

def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Your choice: {user_choice}.")
        print(f"Computer choice: {computer_choice}.")
        determine_winner(user_choice, computer_choice)
        print(f"Your points - {a}, Computer points - {b}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"Final result: You - {a}, Computer - {b}")
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
