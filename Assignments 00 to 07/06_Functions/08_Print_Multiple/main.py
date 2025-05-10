# This function takes two parameters: a message (string) and a number of repeats (integer)
def print_multiple(message, repeats):
    # This loop will repeat 'repeats' times
    for _ in range(repeats):
        print(message)  # Print the message each time

# This is the main function that controls the flow of the program
def main():
    # Ask the user to input a message and store it in the 'message' variable
    message = input("Please type a message: ")
    
    # Ask the user to input how many times the message should be repeated
    # Convert that input from string to integer and store it in 'repeats'
    repeats = int(input("Enter a number of times to repeat your message: "))
    
    # Call the print_multiple function with the user inputs
    print_multiple(message, repeats)

# This checks if the current script is being run directly (not imported)
# If so, it calls the main() function to start the program
if __name__ == "__main__":
    main()
