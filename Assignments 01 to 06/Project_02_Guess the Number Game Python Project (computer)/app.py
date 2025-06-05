# Importing the random module to generate a random number
import random

# Define a function to hold the game logic
def guess_the_number():
    # Generate a random number between 1 and 50
    number_to_guess = random.randint(1, 50)
    
    # This variable will count the number of attempts
    attempts = 0

    # Welcome message for the user
    print("🎯 Welcome to the Guess the Number Game!")
    print("🤖 I have chosen a number between 1 and 50.")

    # Start an infinite loop – this will continue until the user guesses the correct number
    while True:
        try:
            # Ask the user to input their guess
            user_guess = int(input("🔢 Enter your guess: "))
            
            # Increase the attempt count by 1
            attempts += 1

            # Check if the guess is lower than the target number
            if user_guess < number_to_guess:
                print("📉 Too low! Try again.")

            # Check if the guess is higher than the target number
            elif user_guess > number_to_guess:
                print("📈 Too high! Try again.")

            # If the guess is correct
            else:
                print(f"✅ Congratulations! You guessed the number in {attempts} attempts.")
                break  # Exit the loop when the correct number is guessed

        # Handle cases where user inputs something that's not a number
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")

# Call the function to start the game
guess_the_number()
