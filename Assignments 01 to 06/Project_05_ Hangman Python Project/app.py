import random

# List of words for the hangman game
word_list = ['python', 'hacker', 'coding', 'program', 'developer']

# Randomly choose a word from the list
chosen_word = random.choice(word_list)

# Create an empty list with underscores for the hidden word
display = ['_' for _ in chosen_word]

# Set the number of allowed wrong guesses
lives = 6

# Store letters guessed already
guessed_letters = []

# Print welcome message
print("Welcome to Hangman!")
print(' '.join(display))

# Game loop: runs until the word is guessed or no lives left
while '_' in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    # Check if letter was already guessed
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try another letter.")
        continue
    guessed_letters.append(guess)

    # If guessed letter is in the word
    if guess in chosen_word:
        # Reveal the letter in the display list
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print("Correct!")
    else:
        # Reduce a life for wrong guess
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")

    print(' '.join(display))
    
    

# Check game result
if '_' not in display:
    print("🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("😢 Game Over! The word was:", chosen_word)
# End of the game
# End of the Hangman game