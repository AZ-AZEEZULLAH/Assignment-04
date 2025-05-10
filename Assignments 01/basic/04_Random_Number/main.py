import random  # Importing the random module to generate random numbers

# Define a function named 'random_number'
def random_number():
    # Print the title text without going to a new line
    print("Random Number Generator:", end=" ")

    # Generate 10 random integers between 1 and 100 (inclusive)
    # Use list comprehension and unpack the list using '*'
    # to print numbers separated by spaces
    print(*[random.randint(1, 100) for _ in range(10)])

# The following block checks if this script is being run directly
if __name__ == "__main__":
    random_number()  # Call the function to generate and print random numbers
