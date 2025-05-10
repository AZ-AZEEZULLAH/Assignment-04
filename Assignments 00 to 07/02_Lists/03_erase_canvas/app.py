import tkinter as tk  # Import the tkinter module to create windows and drawings

# Set the size of the canvas (drawing area)
CANVAS_WIDTH = 400     # Width of the window in pixels
CANVAS_HEIGHT = 400    # Height of the window in pixels
CELL_SIZE = 40         # Size of the blue square
ERASER_SIZE = 20       # Size of the pink eraser

# This function is called every time the mouse moves
def erase(event):
    x = event.x  # Get the x (left-right) position of the mouse
    y = event.y  # Get the y (up-down) position of the mouse

    # Find all shapes that are under the eraser area
    overlapping = canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)

    # For each shape under the eraser:
    for item in overlapping:
        if item != eraser:         # If it's not the eraser itself
            canvas.delete(item)    # Remove it from the canvas (erase it)

    # Move the pink eraser to follow the mouse
    canvas.coords(eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)

# Create the main window where everything will be shown
window = tk.Tk()
window.title("Eraser Example")  # Set the title of the window

# Create a canvas (a white drawing board)
canvas = tk.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
canvas.pack()  # Show the canvas in the window

# Draw one blue square at position (100, 100)
cell = canvas.create_rectangle(100, 100, 100 + CELL_SIZE, 100 + CELL_SIZE, fill='blue')

# Create a pink square that will act as an eraser (starts at position 0,0)
eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill='pink')

# When the mouse moves on the canvas, call the `erase` function
canvas.bind("<Motion>", erase)

# Start the window and keep it open
window.mainloop()
