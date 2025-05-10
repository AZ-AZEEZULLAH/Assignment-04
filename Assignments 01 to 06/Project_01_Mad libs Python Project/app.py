# Animal-Themed Mad Libs Story

print("🐾 Welcome to the Wild Animal Adventure! 🐾")

# Get user inputs
animal1 = input("Enter a first animal: ")
animal2 = input("Enter a second animal: ")
adjective = input("Enter an adjective: ")
place = input("Enter a jungle or forest name: ")
sound = input("Enter a sound (like 'roar', 'chirp', 'growl'): ")
activity = input("Enter an activity (like 'jumping', 'hunting'): ")
food = input("Enter a type of food: ")

# Story template
madlib = f"""
Deep inside the {place}, a {adjective} {animal1} was {activity} under the trees.
Suddenly, a loud '{sound}!' echoed through the jungle.
It was a {animal2}, and it looked very hungry.
The {animal1} quickly threw some {food} to distract the {animal2}.
Surprisingly, the two animals became friends and shared the {food}.
From that day on, the {place} was filled with peace and laughter 🐾.
"""

# Print the story
print("\n🌿 Here's your Animal Adventure Story:")
print(madlib)