import os
import time

from pokedex.services.lcd.lib.LCD_2inch4 import LCD_2inch4
import spidev as SPI
from PIL import Image


RST = 27
DC = 25
BL = 6
bus = 0
device = 0


def splash_screen():
    disp = _get_display()

    image = Image.open('/home/pi/dexGraphics/splashscreen2.jpg')
    image = image.rotate(0)
    disp.ShowImage(image)
    time.sleep(3)
    disp.module_exit()


def dex_image(foundClass):
    disp = _get_display()

    seen_file = os.path.abspath(f"seen/{foundClass}.txt")

    if os.path.isfile(seen_file):
        return

    image = Image.open(f"../res/classified/dexGraphics/dexEntryGraphics/{foundClass}.jpg")
    image = image.rotate(0)
    disp.ShowImage(image)
    time.sleep(3)
    disp.module_exit()


def _get_display():
    """
    Get display ready
    """
    disp = LCD_2inch4(spi=SPI.SpiDev(bus, device), spi_freq=10000000, rst=RST, dc=DC, bl=BL)
    disp.Init()
    disp.clear()
    return disp

