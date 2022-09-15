from gpiozero import Button
import subprocess
import sys
## for the LCD screen
button = Button(17)


def open_dex_and_die(program, exit_code=0):
    
    # Start the dex
    subprocess.Popen(program)
    # close this script
    sys.exit(exit_code)


button.when_released = open_dex_and_die(['python', 'main.py'])
