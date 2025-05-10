# This function prints all the divisors of a given number
def print_divisor(number):
    # Print a message showing which number we are finding divisors for
    print(f"Divisor of {number} are :")

    # Start a loop from 1 to the number itself
    for i in range(1, number + 1):
        # If the number divides evenly (no remainder), it's a divisor
        if number % i == 0:
            print(f"▶ {i}")  # Print the divisor


# This is the main function where the program starts
def main():
    try:
        # Ask the user to enter a number
        num = int(input("Enter a number to find its divisors: ➡  "))

        # Check if the number is 0 or negative
        if num <= 0:
            print("Please enter a positive integer greater than 0.")
            return  # Stop the program here

    # If the user enters something that's not a number
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")
        return  # Stop the program here

    # If everything is okay, call the function to print divisors
    print_divisor(num)


# This line makes sure the program runs from the main function
if __name__ == "__main__":
    main()
 