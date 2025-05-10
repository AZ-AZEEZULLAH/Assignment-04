# Importing the math module to use mathematical functions like square root
import math 

# Function to analyze a number: calculates square, cube, and square root
def analyze_number(number):
    square = number ** 2         # Square of the number
    cube = number ** 3           # Cube of the number
    square_root = math.sqrt(number)  # Square root using math.sqrt()

    # Returning multiple values (square, cube, square root) as a tuple
    return square, cube, square_root

# Main function that handles input/output
def main():
    try:
        # Taking user input and converting it to float
        num = float(input("Enter a number : ➡ "))
        
    except ValueError:
        # If the input is not a valid number, show an error and exit the function
        print("❌ Please enter a valid number ➡ ")
        return

    # Calling the analyze_number function and unpacking the returned values
    square, cube, square_root = analyze_number(num)

    # Displaying the results
    print(f"✅ The square of {num} is : {square}")
    print(f"✅ The cube of {num} is : {cube}")
    print(f"✅ The square root of {num} is : {square_root: .3f}")

# This checks if the script is being run directly (not imported)
if __name__ == "__main__":
    main()
