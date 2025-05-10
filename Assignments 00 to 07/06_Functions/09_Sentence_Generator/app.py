# Importing the random module to make random selections from lists
import random

# Lists of words used to build sentences
nouns = ["Cat", "Boy", "Girl", "Dog", "Rabbit"]           # Subjects
verbs = ["eats", "plays with", "jumps over", "chases", "looks at"]  # Actions
places = ["the park", "school", "home", "the moon", "a castle"]     # Locations

# Function to generate one random sentence
def generate_sentence():
    # Randomly choose one item from each list
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    place = random.choice(places)
    # Format the sentence and return it
    return f"The {noun} {verb} {place}."

# Main function to run the program
def main():
    try:
        # Ask the user how many sentences they want
        count = int(input("How many sentences do you want to generate? ➡ "))
        
        # If user enters a non-positive number, show a warning and stop
        if count <= 0:
            print("⚠ Please enter a positive number.")
            return
    
    # If user enters something that isn't a number, handle the error
    except ValueError:
        print("✖ Invalid input! Please enter a valid number.")
        return

    # Print each generated sentence
    print("\nGenerated Sentences:")
    for _ in range(count):
        print("⏩", generate_sentence())

# This condition makes sure the main() function runs only when the script is executed directly
if __name__ == "__main__":
    main()
