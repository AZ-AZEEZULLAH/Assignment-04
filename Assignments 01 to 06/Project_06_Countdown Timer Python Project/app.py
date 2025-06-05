import time  # Importing time module to use sleep() function

def countdown_timer(seconds):
    while seconds > 0:
        # Calculate minutes and seconds
        mins = seconds // 60
        secs = seconds % 60

        # Format the output to look like MM:SS
        timer_format = f"{mins:02d}:{secs:02d}"
        print(timer_format, end="\r")  # Print on the same line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1  # Decrease the timer by 1 second

    print("⏰ Time's up!")  # Message when countdown is finished

# 👇 Input from the user in seconds
try:
    total_seconds = int(input("Enter time in seconds: "))
    countdown_timer(total_seconds)  # Call the function with user input
except ValueError:
    print("Please enter a valid number.")
