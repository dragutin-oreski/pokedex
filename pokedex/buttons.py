from gpiozero import Button
import subprocess
import sys

button1 = Button(22)
button2 = Button(23)
button3 = Button(24)


def run_program(program, exit_code=0):
    subprocess.Popen(program)  # Start the dex
    sys.exit(exit_code)  # close this script
