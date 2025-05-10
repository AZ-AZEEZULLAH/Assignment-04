### Leap Year




YEAR :int = int(input("Enter the year: "))



def leap_year():
    if YEAR % 4 == 0:
        if YEAR % 100 == 0:
            if YEAR % 400 == 0:
                print(f"{YEAR} is a leap year")
            else:
                print(f"{YEAR} is not a leap year")
        else:
            print(f"{YEAR} is a leap year")
    else:
        print(f"{YEAR} is not a leap year")

if __name__ == "__main__":
    leap_year()