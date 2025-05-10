## 03 In Stock


# Function to check if a product is in stock
def in_stock(product, stock):
    product = product.lower()  # Convert product name to lowercase to match dictionary keys
    # Check if the product exists in the stock dictionary and has quantity > 0
    if product in stock and stock[product] > 0:
        return True
    else:
        return False 

# Main function to run the stock checker
def main():
    # Dictionary representing the current stock of items
    stock = {
        "apple": 10,
        "banana": 0,
        "orange": 5,
        "grapes": 2
    }

    # Ask the user to enter a product name
    product = input("Enter the product name to check its stock: ➡ ").lower()

    # Call the in_stock function and check availability
    if in_stock(product, stock):
        # Capitalize the first letter of the product for clean display
        print(f"✅ {product.capitalize()} is in stock !!")
    else:
        print(f"❌ {product.capitalize()} is not in stock !!")

# This ensures the main() function runs only if the script is executed directly
if __name__ == "__main__":
    main()
