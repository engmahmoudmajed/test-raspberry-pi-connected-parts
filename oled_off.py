from luma.core.interface.serial import i2c
from luma.oled.device import sh1106

# Initialize and clear
try:
    serial = i2c(port=1, address=0x3C)
    device = sh1106(serial, width=128, height=64, rotate=0)

    # This function turns off the display mechanism and clears memory
    device.cleanup() 
except:
    pass
