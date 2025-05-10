import random  # Importing the random module to generate random numbers

# Define the main function that contains the game logic
def guess_my_number():
    # Generate a random number between 1 and 100 (inclusive)
    secret_number = random.randint(1, 100)

    # Initialize the attempt counter
    attempts = 0

    # Print the initial instruction
    print("Guess a Number between 1 and 100")

    # Start an infinite loop until the correct guess is made
    while True:
        try:
            # Take user input and convert it into an integer
            guess = int(input("Enter your guess: "))

            # Increase attempt count each time the user makes a guess
            attempts += 1

            # Check if the guessed number is less than the secret number
            if guess < secret_number:
                print("Too low !! Try again :")

            # Check if the guessed number is greater than the secret number
            elif guess > secret_number:
                print("Too high !! Try again :")

            # If the guess is correct
            else:
                print(f"Congratulations!! You guessed the number {secret_number} in {attempts} attempts.")
                break  # Exit the loop
        except ValueError:
            # Handle non-integer inputs gracefully
            print("Invalid input. Please enter a valid number.")

# This block ensures the game runs only if the file is executed directly
if __name__ == "__main__":
    guess_my_number()
