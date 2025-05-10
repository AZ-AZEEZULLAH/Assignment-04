import random

# Total number of rounds to play
NUM_ROUNDS = 5

def play_rounds():
    # Generate a random number for the player and the computer
    player_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)  # Fixed typo: randit → randint

    print(f"\n🎲 Your number is {player_number}")

    # Ask player to guess if the computer's number is higher or lower
    while True:
        guess = input("🔊📢 Will the computer's number be 'Higher' or 'Lower'? ").strip().lower()
        if guess in ["higher", "lower"]:
            break
        print("🔕 Invalid input. Please enter 'Higher' or 'Lower'.")

    # Determine outcome
    if (guess == "higher" and computer_number > player_number) or (guess == "lower" and computer_number < player_number):
        print(f"✅ Correct! The computer's number was {computer_number}")
        return 1  # Return 1 point for correct guess
    elif player_number == computer_number:
        print(f"🤝 Tied! Both numbers were {player_number}")
        return 0  # No points for a tie
    else:
        print(f"❌ Incorrect. The computer's number was {computer_number}")
        return 0  # No points for wrong guess

def main():
    print("💖 Welcome to The High and Low Game 💖")
    print(f"💟 You will play {NUM_ROUNDS} rounds. Try to guess correctly!\n")

    score = 0  # Initialize score

    # Loop through the rounds
    for _ in range(NUM_ROUNDS):
        score += play_rounds()

    print("🌐 Game is over")
    print(f"🧿 Your final score: {score} / {NUM_ROUNDS}")

    # Display performance message
    if score == NUM_ROUNDS:
        print("🤩 Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("💔 Good job, you played well!")
    else:
        print("🧧 Best of luck, try again!")

# Only run the game if this script is run directly
if __name__ == "__main__":
    main()
