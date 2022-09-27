from gpiozero import Button
import subprocess
import sys

from pokedex.display import show_dex_image
from pokedex.resources import get_seen_names

button1 = Button(22)
button2 = Button(23)
button3 = Button(24)


def run_program(program, exit_code=0):
    subprocess.Popen(program)  # Start the dex
    sys.exit(exit_code)  # close this script


def browse_seen():
    seen_names = get_seen_names()
    size = len(seen_names)
    index = 0

    show_dex_image(seen_names[index])

    while 0 < len(seen_names):

        if button2.is_pressed:
            index = (index + 1) % size
            show_dex_image(seen_names[index])
            print(index)

        if button3.is_pressed:
            index = (index - 1) % size
            show_dex_image(seen_names[index])
            print(index)

        if button1.is_pressed:
            return
