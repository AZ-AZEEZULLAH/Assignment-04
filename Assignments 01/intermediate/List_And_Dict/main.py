def main():
    # Initialize list of fruits with emojis
    fruits = ["Apple 🍎", "Banana 🍌", "Orange 🍊", "Grapes 🍇", "PineApple 🍍"]
    print(f"\n🧺 Current List Of Fruits:\n{fruits}\n")

    while True:
        # Display menu options
        print("\n💌 Choose an option :\n1️⃣ Access Item\n2️⃣ Change Item\n3️⃣ Show Part of List\n4️⃣ Exit")
        choice = input("Enter Choice (1-4): ")

        if choice == "1":
            # Access fruit at specific index
            index = int(input("Enter Index (0-4): "))  # Added colon
            if 0 <= index < len(fruits):
                print(f"Selected Fruit: {fruits[index]}")
            else:
                print("Invalid Index!")

        elif choice == "2":
            # Modify fruit at specific index
            index = int(input("Enter Index (0-4): "))  # Added colon
            if 0 <= index < len(fruits):  # Fixed spacing around <
                new_value = input("Enter New Item: ")  # Added colon
                fruits[index] = new_value
                print(f"✅ Updated List: {fruits}")
            else:
                print("Invalid Index!")

        elif choice == "3":
            # Show slice of the list
            start = int(input("Start Index (0-4): "))  # Fixed colon syntax
            end = int(input("End Index (1-5): "))     # Added colon
            if 0 <= start < end <= len(fruits):       # Fixed spacing
                print(f"List Slice: {fruits[start:end]}")
            else:
                print("Invalid Range!")

        elif choice == "4":
            # Exit the program
            print("Good Bye!")
            break

        else:
            # Handle invalid menu choice
            print("Invalid Choice (1-4)!")

# Corrected the main guard syntax
if __name__ == "__main__":  # Fixed underscore and quotes
    main()