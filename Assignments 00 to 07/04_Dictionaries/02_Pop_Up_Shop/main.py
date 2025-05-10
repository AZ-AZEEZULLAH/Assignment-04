## Pop Up Shop


def calculate_total_cost():

    fruits_price = {
        "Apple" : 1.00,
        "Banana" : 0.50,
        "Orange" : 0.75,
        "Grapes" : 1.2,
        "Mango" : 1.5,
    }

    total_cost = 0 

    for fruits , price in fruits_price.items():
        

        while True:
            try:
                quantity = int(input(f"How many {fruits} do you want to buy? "))
                if quantity < 0 :
                    print(" Invalid Input Please enter a positive number.")
                    continue

                total_cost += price * quantity
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                
    print(f"Total cost of your purchase is: ${total_cost:.2f}")


if __name__ == "__main__":
    calculate_total_cost()