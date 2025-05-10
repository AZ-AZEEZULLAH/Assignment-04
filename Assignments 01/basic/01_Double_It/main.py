def double_it_number():
    try:
        # Prompt the user to enter a number and convert the input to an integer
        current_value = int(input("Enter a Number: "))

        # Check if the entered number is less than 1
        if current_value < 1:
            print("Enter a ✅ Correct Number :")
            return  # Exit the function if the number is not valid

        # Loop: as long as the number is less than 100, keep doubling it
        while current_value < 100:
            current_value *= 2  # Double the current value
            print(current_value, end=" ")  # Print the doubled value on the same line with a space

    except ValueError:
        # If the user enters something that's not an integer, this block will run
        print("Invalid input. Please enter a valid number.")
            

# This block ensures the function only runs if the script is executed directly,
# and not when imported as a module
if __name__ == "__main__":
    double_it_number()
