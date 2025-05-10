

# This function calculates the average of a list of numbers
def calculates_averages(numbers):
    # If the list is empty, return 0
    if not numbers:
        return 0
    
    # Add all the numbers and divide by how many numbers there are
    return sum(numbers) / len(numbers)


# This is the main function that runs the program
def main():
    # Ask the user to enter numbers with commas
    print("Enter numbers separated by commas:")

    # Take input from the user
    user_input = input("➡ ")

    try:
        # Split the input by commas, remove spaces, and turn each part into a number
        number_list = [float(num.strip()) for num in user_input.split(",")]

    except ValueError:
        # If the user types something that's not a number, show this message
        print("❌ Invalid input. Please enter numbers separated by commas.")
        return

    # Call the function to find the average
    avg = calculates_averages(number_list)

    # Show the average with 2 decimal places
    print(f"✅ Average of the given numbers: {avg:.2f}")


# This makes sure the main() function runs when we run the file
if __name__ == "__main__":
    main()
