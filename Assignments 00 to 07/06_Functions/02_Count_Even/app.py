# Function to count even numbers from a list
def count_even(numbers):
    # Make a list of numbers that are even (divisible by 2)
    even_numbers = [num for num in numbers if num % 2 == 0]
    
    # Return how many even numbers there are and the list of them
    return len(even_numbers), even_numbers

# Main function where the program starts
def main():
    # Ask the user to enter numbers with commas
    print("Enter numbers separated by commas: ")
    user_input = input(" ➡ ")  # Get input from the user

    try:
        # Split the input by commas and convert each part to an integer
        number_list = [int(num.strip()) for num in user_input.split(",")]
    except ValueError:
        # If the user enters something that's not a number, show an error
        print("❌ Invalid input. Please enter integers only.")
        return

    # Call the count_even function and get the result
    count, evens = count_even(number_list)

    # Show the total count of even numbers
    print(f"✅ Total even numbers: {count}")
    
    # Show the list of even numbers
    print(f"Even numbers: {evens}")

# This line means "start here" when the file is run
if __name__ == "__main__":
    main()
