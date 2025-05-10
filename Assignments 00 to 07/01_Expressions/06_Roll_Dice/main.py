# Roll Dice

import random

def roll_dice():
    die1 :int = random.randint(1,6)
    die2 : int = random.randint(1,6)
    total : int = int(die1) + int(die2)
    print("First die: " + str (die1))
    print("Second die: " + str (die2))
    print("Total: " + str (total))
    print(f"die2 :{die2}")



if __name__ == "__main__":
    roll_dice()