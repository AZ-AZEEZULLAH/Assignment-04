## Square Number 



print("Welcome to the Square Number program!")

def square_number():
    print("This program calculates the square of a number.")

    num : int = int (input("Enter a number: "))
    print(f"The square of {num} is {num ** 2}.")


if __name__=="__main__":
    square_number()
