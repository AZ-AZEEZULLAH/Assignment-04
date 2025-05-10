# This function takes a list of numbers and doubles each one
def double_number(number):
    # Create a new list where each number is multiplied by 2
    return [numbers * 2 for numbers in number]


# This function asks the user to enter numbers, doubles them, and shows the result
def double_number_2():
    # Ask the user to enter numbers separated by commas
    print("Enter numbers separated by commas: ")
    user_input = input(" ➡ ")  # Take input from the user

    try:
        # Split the input by comma, remove extra spaces, and convert each to an integer
        number_list = [int(num.strip()) for num in user_input.split(",")]
    except ValueError:
        # If something goes wrong (like the user types letters), show an error
        print("❌ Invalid input. Please enter integers only.")
        return  # Stop the function here if the input is bad

    # Call the first function to double the numbers
    doubled = double_number(number_list)

    # Show the result
    print(f"✅ Doubled numbers: {doubled}")


# This line runs the program when you start the file
if __name__ == "__main__":
    double_number_2()
