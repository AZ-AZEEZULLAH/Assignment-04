## Wholesome Macine



AFFERMATION :str = "Iam capable of doing anything .I put mind too"




def wholesome_machine():
    print("Start Wholesome Machine")

    while True:
        user_input = input("Please try the following affermation :" + AFFERMATION)

        if user_input == AFFERMATION:
            print("That\`s right")
            break
        else:
            print("Try again")


if __name__ == "__main__":
    wholesome_machine()