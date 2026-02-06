from gpiozero import Button, LED
from signal import pause

# Setup
# Sensor is on GPIO 12 (Acting like a button)
sensor = Button(12)

# LED is on GPIO 16
led = LED(16)

print("--- IR SENSOR + LED TEST ---")
print("Sensor: GPIO 12")
print("LED:    GPIO 16")
print("Move your hand close to the sensor...")

# --- Logic ---
# When obstacle detected (sensor goes LOW/Pressed) -> Turn LED ON
sensor.when_pressed = led.on

# When path is clear (sensor goes HIGH/Released) -> Turn LED OFF
sensor.when_released = led.off

# Keep running
pause()