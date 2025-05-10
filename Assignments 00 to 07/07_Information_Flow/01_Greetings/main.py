# Define a function named 'greeting' that takes a parameter 'name'
def greeting(name):
    # Return a formatted greeting message using the name provided
    return f"Hello , {name} Welcome to the coding journey"


# Define the main function that runs the main part of the program
def main():
    # Prompt the user to enter their name and store it in the variable 'name'
    name = input("Please enter your name : ")

    # Call the greeting function with the user's name and store the result in 'greeting_message'
    greeting_message = greeting(name)

    # Print the greeting message to the screen
    print(greeting_message)


# Check if this file is being run directly (not imported as a module)
if __name__ == "__main__":
    # Call the main function to start the program
    main()
