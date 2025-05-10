# We need these two modules:
import random   # This is for mixing up the numbers randomly
import time     # This is for adding a delay between prints


# This function will print numbers in a random (chaotic) order
def chaotic_counting(start, end, delay=0.5):
    # Make a list of numbers from start to end
    number = list(range(start, end + 1))

    # Shuffle the list to make the order random
    random.shuffle(number)

    # Show that counting has started
    print("Chaotic Counting Begins:")

    # Go through each number in the list
    for numbers in number:
        print(numbers)       # Print the number
        time.sleep(delay)    # Wait for some time (default 0.5 seconds)

    # Say that counting is done
    print("Done with chaotic counting!")


# This is the main function where the program starts
def main():
    print("Welcome to Chaotic Counting!")
    print("Enter the start and end numbers for chaotic counting.")

    try:
        # Ask user for the start number
        start = int(input("Start number ➡ : "))
        # Ask user for the end number
        end = int(input("End number ➡ : "))

        # Check if start is greater than end (which is not allowed)
        if start > end:
            print("❌ Start number should be less than end number.")
            return  # Stop the program if the start is wrong

        # Call the function to do chaotic counting
        chaotic_counting(start, end)

    # If user enters letters instead of numbers, show an error
    except ValueError:
        print("❌ Invalid input. Please enter valid numbers.")


# This means: run the main function when this file is executed
if __name__ == "__main__":
    main()
# This is the end of the code