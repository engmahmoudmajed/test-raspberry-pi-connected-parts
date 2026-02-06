import RPi.GPIO as GPIO
import time

# Changed from 17 to 26
ObstaclePin = 26

def setup():
    GPIO.setmode(GPIO.BCM)
    # Set up pin 26 as an input with an internal pull-up resistor
    GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    while True:
        # Sensor sends a 0 (LOW) when it detects an obstacle
        if (0 == GPIO.input(ObstaclePin)):
            print("Detected Barrier!")
            # Adding a short delay to prevent multiple prints for one movement
            time.sleep(0.5) 
        else:
            # Optional: uncomment if you want to see when it's clear
            # print("Path Clear")
            pass
        time.sleep(0.1)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()