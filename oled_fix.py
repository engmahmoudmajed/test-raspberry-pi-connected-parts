from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
import time

# Initialize the I2C interface and the SH1106 device
# If i2cdetect showed 0x3D, change address to 0x3D below
serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

# Draw to the display
with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((10, 20), "Hello World!", fill="white")
    draw.text((10, 40), "Raspberry Pi", fill="white")

# Keep the script running to show the image for 10 seconds
time.sleep(10)