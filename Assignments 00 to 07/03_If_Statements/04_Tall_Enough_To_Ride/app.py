## Tall Enough To Ride

MIN_HEIGHT : int = 40  


def tall_enough_to_ride():
    user : int = int(input (" How tall are you ?"))

    if user >= MIN_HEIGHT:
        print("You are tall enough to ride !")


    else:
        print("You are not tall enough to ride !")

if __name__ == "__main__":
    tall_enough_to_ride()