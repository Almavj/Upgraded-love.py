import tkinter as tk
import random

# List of colors for the text and background (excluding yellow in the background)
text_colors = ["#FF0000", "#FFA500", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#EE82EE"]
background_colors = ["#282C35", "#8A2BE2", "#FF69B4", "#20B2AA", "#FF6347", "#4682B4"]

# Number of "I LOVE YOU" texts
num_texts = 5

# Initialize the starting positions for each label
x_positions = [-i * 150 for i in range(num_texts)]  # Staggered start positions

# Function to mix colors randomly for the text
def mix_text_color():
    return random.choice(text_colors)

# Function to change the background color randomly
def change_background_color():
    new_bg_color = random.choice(background_colors)
    root.configure(bg=new_bg_color)
    for label in labels:
        label.config(bg=new_bg_color)  # Ensure label background matches window background
    root.after(500, change_background_color)  # Change background every 500 ms

# Function to update the text color and position
def animate_text(index, label):
    global x_positions
    current_color = mix_text_color()  # Get a random color for the text
    label.config(fg=current_color)  # Update the label's color

    # Update the position of the label
    x_positions[index] += 10  # Move right by 10 pixels
    if x_positions[index] > root.winfo_width():  # Reset as soon as it goes off the screen
        x_positions[index] = -label.winfo_width()  # Start again immediately from the left edge

    label.place(x=x_positions[index], y=100 + index * 50)  # Update label's position with staggered heights
    root.after(50, animate_text, index, label)  # Call this function again after 50 ms

# Create the main window
root = tk.Tk()
root.title("I LOVE YOU Animation")
root.geometry("800x400")

# Create labels for each text and start their animations
labels = []
for i in range(num_texts):
    label = tk.Label(root, text="I LOVE YOU", font=("Helvetica", 48))
    label.pack()
    labels.append(label)
    animate_text(i, label)  # Start animation for each label

# Start the background color change and text animation
change_background_color()  # Begin blinking background
root.mainloop()
