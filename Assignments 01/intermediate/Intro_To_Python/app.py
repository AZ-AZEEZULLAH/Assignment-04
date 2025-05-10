# Dictionary storing gravity values relative to Earth for each planet
PLANET_GRAVITY = {
    "MERCURY": 0.376,
    "VENUS": 0.889,
    "MARS": 0.378,
    "JUPITER": 2.36,
    "SATURN": 1.081,
    "URANUS": 0.869,
    "NEPTUNE": 1.12
}

# Function to calculate weight on a selected planet
def calculate_weight(weight, planet):
    # Get gravity value from dictionary
    gravity = PLANET_GRAVITY.get(planet)

    # If planet is valid, calculate weight
    if gravity:
        return round(weight * gravity, 2)  # Rounded to 2 decimal places
    else:
        return "❌ Invalid planet"  # If invalid planet name

# Main function to run the program
def weight_calc_main():
    print("🚀 Planetary Weight Calculator")

    # Ask user to input their weight in KG
    while True:
        try:
            weight = float(input("Enter your weight (KG): "))

            if weight > 0:
                break  # Valid input
            print("🔕 Invalid input! A number greater than 0 is required.")
        except ValueError:
            print("🔕 Invalid input! A number is required.")

    # Show list of available planets
    print("\n💛 Available planets: ", " , ".join(PLANET_GRAVITY.keys()))

    # Ask user to select a valid planet
    while True:
        planet = input("Enter a planet name: ").strip().upper()

        if planet in PLANET_GRAVITY:
            break  # Valid planet name
        print("❌ Invalid planet! Please choose from the list.")

    # Calculate and display the weight on the selected planet
    weight_on_planet = calculate_weight(weight, planet)
    print(f"🌐 Your weight on {planet} is {weight_on_planet} kg")

# Only run the program if this file is executed directly
if __name__ == "__main__":
    weight_calc_main()
