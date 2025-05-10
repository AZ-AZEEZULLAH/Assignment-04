# Define the main function
def main():
    # Loop through numbers from 10 to 20 (inclusive). `range(10, 21)` goes from 10 up to, but not including, 21.
    for num in range(10, 21):  
        # Check if the number is odd using the is_odd() function
        if is_odd(num):
            # If it's odd, print the number followed by "Odd Number"
            print(f"{num} Odd Number")
        else:
            # If it's not odd (i.e., even), print the number followed by "Even Number"
            print(f"{num} Even Number")


# Define the is_odd function to check if a number is odd
def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns True.
    """
    remainder = value % 2  # Get the remainder when the value is divided by 2
    return remainder == 1  # If remainder is 1, it's an odd number


# This block ensures the main function runs only if this script is run directly
if __name__ == '__main__':
    main()
