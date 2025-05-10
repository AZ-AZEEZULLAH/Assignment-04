## Random Number



import random


def random_number():
    for i in range(20):
        number = random.randint(1, 100)
        print(number)


if __name__ == "__main__":
    random_number()