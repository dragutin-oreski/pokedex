from gpiozero import Button
import subprocess
import time
import sys

from pokedex.display import show_dex_image
from pokedex.resources import get_seen_names
from pokedex.sound import text_to_speech

button1 = Button(22)
button2 = Button(23)
button3 = Button(24)
button4 = Button(16)


def run_program(program, exit_code=0):
    subprocess.Popen(program)  # Start the dex
    sys.exit(exit_code)  # close this script


def browse_seen():
    seen_names = get_seen_names()
    size = len(seen_names)
    index = 0

    if size > 0:
        show_dex_image(seen_names[index])

    while size > 0:

        if button2.is_pressed:
            index = (index + 1) % size
            show_dex_image(seen_names[index])

        if button3.is_pressed:
            index = (index - 1) % size
            show_dex_image(seen_names[index])

        if button4.is_pressed:
            text_to_speech(seen_names[index])

        if button1.is_pressed:
            return
