# Import the PiCamera class from the picamera module
from picamera import PiCamera

# Create an instance of the PiCamera class
cam = PiCamera()

# Set the resolution of the camera to 4056×3040 pixels
cam.resolution = (4056, 3040)

# Capture three images using a loop
for i in range(3):
    # Capture an image and save it
    # with a file name like
    # "image0.png", "image1.png", etc.
    cam.capture(f"image{i}.png")
    