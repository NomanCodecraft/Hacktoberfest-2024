import random

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "You lose!"

def start_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = input("Enter Rock, Paper, or Scissors (or 'exit' to quit): ").capitalize()
        
        if user_choice == 'Exit':
            print("Thanks for playing!")
            break
        elif user_choice not in ["Rock", "Paper", "Scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        print()  # Print a new line for better readability

if __name__ == "__main__":
    start_game()
