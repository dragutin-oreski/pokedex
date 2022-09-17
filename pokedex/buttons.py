from gpiozero import Button
import subprocess
import sys

button1 = Button(22)
button2 = Button(23)
button3 = Button(24)


## Reopens the button press script killing this process
def open_switch_and_die(program, exit_code=0):
    # Start the dex
    subprocess.Popen(program)
    # close this script
    sys.exit(exit_code)


