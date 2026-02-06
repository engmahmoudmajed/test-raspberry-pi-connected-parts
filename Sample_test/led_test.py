from gpiozero import LED
from time import sleep

# Setup LED on GPIO 16
led = LED(16)

print("LED Test Running on GPIO 16...")
print("Press Ctrl+C to stop.")

while True:
    led.on()   # Turn ON
    sleep(1)   # Wait 1 second
    led.off()  # Turn OFF
    sleep(1)   # Wait 1 second