import os
import subprocess

cmd_beg = 'sudo espeak -s160 '  # puts sudo espeak in term
cmd_end = ' 2>/dev/null'  # cleans up the output from the terminal
cmd_voice = '-ven+m5 '  # Assigns which voice ill be using


def text_to_speech(found_class):
    pokedex_file = os.path.abspath(f"dex/{found_class}.txt")
    seen_file = os.path.abspath(f"seen/{found_class}.txt")
    if os.path.isfile(seen_file):
        return
    with open(pokedex_file, "r") as f:
        dex_entry = f.read().rstrip()
    subprocess.call(
        [cmd_beg + cmd_voice + dex_entry + cmd_end],
        shell=True
    )
