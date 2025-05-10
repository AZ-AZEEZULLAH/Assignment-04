# Pythagorean Theorem




import math 


def pythagorean_theorem():
    ab : float = float (input("Enter the length of the side ab:"))
    ac : float = float (input("Enter the length of the side ac:"))

    

    bc : float = math.sqrt(ab**2 + ac**2)


    
    print("The length of BC (the hypotenuse) is: " + str(bc))

if __name__ == "__main__":
    pythagorean_theorem()