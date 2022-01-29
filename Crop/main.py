from Screen import Screen
from datetime import datetime
import keyboard as key

print("Waiting for keyboard interruption...")
while not key.is_pressed("alt"):
    pass
print("Started")

screen = Screen()

# Screenshot
screenshot = screen.screenshot()

# Get Crop Coordinates
cords = screen.draw()
initial_start = cords[0]
initial_end = cords[1]
print(f"Initial Start: {(initial_start.x, initial_start.y)}\nInitial End: {initial_end.x, initial_end.y}")

# Correct the Coordinates on different cases
if initial_end.x < initial_start.x and initial_end.y > initial_start.y:
    start = (initial_end.x, initial_start.y)
    end = (initial_start.x, initial_end.y)
elif initial_end.y < initial_start.y and initial_end.x > initial_start.x:
    start = (initial_start.x, initial_end.y)
    end = (initial_end.x, initial_start.y)
elif initial_end.x < initial_start.x and initial_end.y < initial_start.y:
    start = (initial_end.x, initial_end.y)
    end = (initial_start.x, initial_start.y)
else:  # Coordinates are correct
    start = (initial_start.x, initial_start.y)
    end = (initial_end.x, initial_end.y)

# Crop The Image
print(f"Crop Coordinates: {start} to {end}")
cropped = screen.crop(screenshot, tuple(start), tuple(end))
date = datetime.now().strftime("%Y-%m-%d__%H-%M-%S")
cropped.save(f"images/user/{date}.png")
cropped.show()
print(f"Saved at ./images/user as {date}.png")

