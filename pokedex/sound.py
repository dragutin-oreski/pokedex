import subprocess

from pokedex.resources import get_description_from_dex

cmd_beg = 'sudo espeak -s160 '  # puts sudo espeak in term
cmd_end = ' 2>/dev/null'  # cleans up the output from the terminal
cmd_voice = '-ven+m5 '  # Assigns which voice ill be using


def text_to_speech(found_class):
    dex_entry = get_description_from_dex(found_class)
    subprocess.call(
        [cmd_beg + cmd_voice + dex_entry + cmd_end],
        shell=True
    )
