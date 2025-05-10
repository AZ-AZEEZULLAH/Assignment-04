## Triangle Perimeter

print("Triangle Perimeter")

def triangle_perimeter():
    print("This is  a program to calculate the perimeter of a triangle.")

    side1 : float = float (input("Enter the length of side 1: "))
    side2 : float = float (input("Enter the length of side 2: "))
    side3 : float = float (input("Enter the length of side 3: "))



    total_perimeter : float = (side1 + side2 + side3)


    print(f"The total perimeter of the triangle is {total_perimeter} units long .. ")


if __name__=="__main__":
     triangle_perimeter()