# Import necessary libraries
import random  # For random choice
import string  # For string constants like letters, digits, punctuation

# Function to generate a random password
def generate_password(length):
    # Define possible characters to use in the password
    letters = string.ascii_letters      # a-z, A-Z
    digits = string.digits              # 0-9
    symbols = string.punctuation        # Special characters like !@#$%^&*

    # Combine all characters into one list
    all_chars = letters + digits + symbols

    # Randomly choose characters from the combined list
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

# Ask user for desired password length
try:
    password_length = int(input("Enter the password length: "))  # Take input and convert to integer

    # Check if the password length is valid
    if password_length < 6:
        print("Password length should be at least 6 characters for better security.")
    else:
        # Call the function and print the generated password
        new_password = generate_password(password_length)
        print("Your generated password is:", new_password)

except ValueError:
    print("Please enter a valid number.")
