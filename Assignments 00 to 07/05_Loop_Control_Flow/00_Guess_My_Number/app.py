## Guess My Number

import random

def guess_my_number():
    secret_number = random.randint(1,20)

    print("Iam thinking of a number between 1 and 20 .......")



    guess = int (input("Take a Guess:"))



    while guess != secret_number:

        if guess < secret_number :
            print("'You guess too low !")


        else :
            print("You guess is too high !")

        guess = int (input("Take a guess :"))

    print("You guessed it ! The number was",secret_number)


if __name__ == "__main__":
    guess_my_number()