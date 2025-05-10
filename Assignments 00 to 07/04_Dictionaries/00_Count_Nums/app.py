# This function collects numbers from the user and counts how many times each number is entered.
def count_nums():
    count_dict = {}  # Initialize an empty dictionary to store number counts.

    while True:  # Start an infinite loop to repeatedly ask for input.
        num = input("Enter a number (or 'exit' to stop): ")  # Ask user for input.

        if num.lower() == "exit":  # If user types 'exit' (case-insensitive), break the loop.
            break

        if num.isdigit():  # Check if the input is a positive integer (no negatives or decimals).
            num = int(num)  # Convert the input string to an integer.
            # Use dictionary's get method to update the count or start at 1 if not already in dict.
            count_dict[num] = count_dict.get(num, 0) + 1
            print(count_dict)  # Show the current state of the dictionary.
        else:
            # If the input is not a valid number, show an error message.
            print("Invalid input. Please enter a valid number.")

    return count_dict  # Return the dictionary containing the counts.


# This function takes the dictionary from above and prints how many times each number was entered.
def display_count(count_dict):
    print("\nCount of numbers:")  # Heading for clarity
    for key, value in count_dict.items():  # Loop through the dictionary's key-value pairs.
        print(f"{key} appears {value} times.")  # Display the result.


# This block runs when the script is executed directly.
if __name__ == "__main__":
    counts = count_nums()  # Call the function to collect input and get the counts.
    display_count(counts)  # Call the function to display the final counts.
