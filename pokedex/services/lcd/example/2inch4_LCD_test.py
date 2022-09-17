#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet
import sys
import time

sys.path.append("../../../..")
from pokedex.services.lcd.lib import LCD_2inch4
from PIL import Image

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 


# display with hardware SPI:
''' Warning!!!Don't  creation of multiple displayer objects!!! '''
#disp = LCD_2inch4.LCD_2inch4(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
disp = LCD_2inch4.LCD_2inch4()
# Initialize library.
disp.Init()
# Clear display.
disp.clear()

    
image = Image.open('/home/pi/Desktop/pokedex/dex_entries/background_image.jpg')
image = image.rotate(0)
disp.ShowImage(image)
time.sleep(3)
disp.module_exit()
    

