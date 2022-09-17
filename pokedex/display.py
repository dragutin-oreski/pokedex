import os
import time

from pokedex.resources import get_image_from_dex, get_background_image
from pokedex.services.lcd.lib.LCD_2inch4 import LCD_2inch4
import spidev as SPI
from PIL import Image


RST = 27
DC = 25
BL = 6
bus = 0
device = 0


def show_background():
    disp = _get_display()

    image = Image.open(get_background_image())
    image = image.rotate(0)
    disp.ShowImage(image)
    time.sleep(3)
    disp.module_exit()


def dex_image(found_class):
    disp = _get_display()

    seen_file = os.path.abspath(f"seen/{found_class}.txt")

    if os.path.isfile(seen_file):
        return

    image = Image.open(get_image_from_dex(found_class))
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

