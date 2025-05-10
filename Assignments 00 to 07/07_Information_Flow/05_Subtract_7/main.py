# Function to subtract 7 from a given number
def subtract_7th(number):
    return number - 7

# Main function where execution starts
def main():
    try:
        # Prompt the user to input a number and convert it to float
        num = float(input("Enter a number : ➡ "))
    
    except ValueError:
        # Handle the case when the user enters something that is not a number
        print("❌ Please enter a valid number.")
        return  # Exit the program early if input is invalid
    
    # Call the subtract_7th function to subtract 7 from the entered number
    result = subtract_7th(num)

    # Display the result
    print(f"✅ After subtracting 7 , the result is : {result}")

# Entry point of the program
if __name__ == "__main__":
    main()
