import time  # Importing the time module to use the sleep function for delays

def countdown_timer():
    # This function counts down from 10 to 1, then prints "Liftoff!!"

    for i in range(10, 0, -1):  # Start at 10, end at 1 (not including 0), decreasing by 1 each time
        print(i, end=" ", flush=True)  
        # Print the current number on the same line, separated by spaces
        # 'flush=True' forces Python to display the output immediately
        time.sleep(1)  # Pause for 1 second between each number

    print("🕑 Lifftoff !!")  # After the loop, print the final message

# This line ensures the countdown only runs if the script is executed directly (not imported)
if __name__ == "__main__":
    countdown_timer()  # Call the countdown function
