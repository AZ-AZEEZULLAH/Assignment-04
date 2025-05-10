# Dicesimulator



import random 

NUMBER_SIDES : int = 6



def roll_dice():
    die1 : int = random.randint(1, NUMBER_SIDES)
    die2 : int = random.randint(1, NUMBER_SIDES)

    total : int = die1 + die2

    print(f"Total of two dies :{total}")



def main():
        die1 : int = 10 
        print("die1 in main () star is :" + str (die1))
        roll_dice()
        roll_dice()
        roll_dice()

        print("die1 in main () is :" + str (die1)) 



if __name__ == "__main__":
        main()