from gpiozero import Button
from signal import pause

# We use "Button" because the sensor acts just like a button:
# It stays HIGH (1) normally, and goes LOW (0) when it sees an obstacle.
# gpiozero handles the logic automatically: "Pressed" = "Obstacle Detected"
sensor = Button(12)

print("IR Sensor Active. Waiting for hand...")

def on_detection():
    print("Hello! I see you.")

def on_clear():
    print("Path clear.")

# Tell the sensor what functions to run
sensor.when_pressed = on_detection
sensor.when_released = on_clear

# Keep the script running
pause()