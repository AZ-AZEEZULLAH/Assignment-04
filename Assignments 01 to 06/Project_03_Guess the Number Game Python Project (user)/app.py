import random  # Importing random module to generate random numbers

# Welcome message
print("Welcome to the Guess the Number Game!")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

# Maximum number of attempts allowed
max_attempts = 10

# Game instructions
print("I'm thinking of a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.")

# Game loop
while attempts < max_attempts:
    try:
        # Ask user to enter a guess
        guess = int(input("Enter your guess: "))
        attempts += 1  # Increase attempt count

        # Check if the guess is correct
        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

        # Show remaining attempts
        print(f"Attempts left: {max_attempts - attempts}")

    except ValueError:
        # Handle error if user enters something that's not a number
        print("❌ Invalid input. Please enter a number.")

# If user runs out of attempts
if attempts == max_attempts and guess != secret_number:
    print(f"😢 Game Over! The number was {secret_number}. Better luck next time!")
