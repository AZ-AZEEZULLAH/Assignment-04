# Function to check if a number is within a specified range
def in_range(number, start, end):
    # Check if 'number' lies between 'start' and 'end' (inclusive)
    if start <= number <= end:
        return True  # Return True if in range
    else:
        return False  # Return False if not in range

# Main function to interact with the user
def main():
    try:
        # Taking integer input from the user
        num = int(input("Enter a number: "))
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

    # Catching the error if user enters non-integer values
    except ValueError:
        print("Please enter valid integers:")
        return  # Exit the function early if error occurs

    # Calling the function to check if number is in the range
    if in_range(num, start, end):
        print(f"✅ {num} is within the range of {start} and {end}")
    else:
        print(f"❌ {num} is not within the range of {start} and {end}")

# Only run the main function if this script is executed directly
if __name__ == "__main__":
    main()
