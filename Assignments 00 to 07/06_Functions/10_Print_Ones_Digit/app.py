

## Print Ones Digit 
# This function takes a number and prints its one's digit
def print_ones_digit(numbers):
    # Get the one's digit using modulus operator (%)
    ones_digit = numbers % 10 

    # Print the result using f-string formatting
    print(f" The ones Digit is {ones_digit} ")

# This is the main function where program execution begins
def main():
    # Prompt the user to enter a number and convert the input to an integer
    numbers = int(input("Enter a number ▶ :"))
    
    # Call the function to print the one's digit of the entered number
    print_ones_digit(numbers)

# This condition ensures the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()
