## Feet to Inches 



INCHES_IN_FOOT : int = 12  # Number of inches in a foot


def feet_to_inches():
    feet : int = int(input("Enter feet Convert into Inches:"))
    print(f"There are {INCHES_IN_FOOT * feet} inches in {feet} feet.")

if __name__ == "__main__":
    feet_to_inches()
