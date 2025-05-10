# Choosing Returns

# This function takes a user's input (option) and returns a message based on the input.
def choose_return(option):
    option = option.strip().upper()  # Removes any extra spaces and converts input to uppercase for consistency
    if option == "A":
        return "You chose option A"  # Returns this message if user chose "A"
    elif option == "B":
        return "You chose option B"  # Returns this message if user chose "B"
    elif option == "C":
        return "You chose option C"  # Returns this message if user chose "C"
    else:
        # If input is not A, B, or C, return this message
        return "Invalid option. Please choose one of the following: A, B, or C."

# The main function controls the flow of the program
def main():
    # Displaying instructions to the user
    print("Choose one of the options: A, B, or C")
    
    # Taking input from the user
    option = input("Enter your choice -> ")
    
    # Calling the function to process the input and storing the result
    result = choose_return(option)
    
    # Printing the result returned by the function
    print(result)

# This line ensures that the main() function only runs when the script is executed directly
if __name__ == "__main__":
    main()
