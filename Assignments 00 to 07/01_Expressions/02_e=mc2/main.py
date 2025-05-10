# 02 e=mc2

C: int = 299792458  # Speed of light in m/s

def energy():
    mass_in_kg: float = float(input("Enter kilo of mass: "))
    energy_in_joules: float = mass_in_kg * (C ** 2)
    print("e = m * C^2...")
    print("Mass = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    print("e = " + str(energy_in_joules) + " Joules of energy")

if __name__ == "__main__":
    energy()
