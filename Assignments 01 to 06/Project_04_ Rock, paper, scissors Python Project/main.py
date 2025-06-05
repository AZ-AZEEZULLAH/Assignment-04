import random  # Importing the random module to make the computer choose randomly

# List of possible choices
choices = ["rock", "paper", "scissors"]

# Function to determine the winner
def determine_winner(player, computer):
    # If both chose the same
    if player == computer:
        return "It's a tie!"
    
    # Player win conditions
    if (player == "rock" and computer == "scissors") or \
       (player == "scissors" and computer == "paper") or \
       (player == "paper" and computer == "rock"):
        return "You win!"
    
    # If not tie or win, then computer wins
    return "Computer wins!"

# Main game loop
while True:
    # Ask the player for input
    player_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
    
    # Exit the game
    if player_choice == "quit":
        print("Thanks for playing!")
        break
    
    # Check if player entered a valid choice
    if player_choice not in choices:
        print("Invalid input. Please try again.")
        continue
    
    # Computer makes a random choice
    computer_choice = random.choice(choices)
    
    # Show what both players chose
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Determine and show the result
    result = determine_winner(player_choice, computer_choice)
    print(result)
    print()  # Print empty line for better readability
# End of the game loop