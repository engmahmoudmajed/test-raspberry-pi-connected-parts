from gpiozero import OutputDevice
from time import sleep

# --- CONFIGURATION ---
RELAY_PIN = 20  # The GPIO pin number (BCM numbering) connected to IN1/IN2/etc.

# 'active_high':
# Set True if the relay turns ON with a HIGH signal (3.3V).
# Set False if the relay turns ON with a LOW signal (GND). 
# Most relay boards are "Active Low", so try False if True doesn't work.
relay = OutputDevice(RELAY_PIN, active_high=False, initial_value=False)

print(f"Testing Relay on GPIO {RELAY_PIN}...")
print("Press CTRL+C to stop.")

try:
    while True:
        print("Relay -> ON")
        relay.on()
        sleep(5)  # Wait 2 seconds

        print("Relay -> OFF")
        relay.off()
        sleep(5)  # Wait 2 seconds

except KeyboardInterrupt:
    print("\nTest stopped by user.")
    relay.off()  # Ensure relay is off before exiting
    relay.close()