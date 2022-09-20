from pokedex.buttons import button1, button2, button3, run_program
from pokedex.display import show_dex_image
from pokedex.resources import get_seen_names, get_path_main_file

seen_names = get_seen_names()
index = 0

while 0 < len(seen_names):

    show_dex_image(seen_names[index])

    if button1.is_pressed:
        show_dex_image(seen_names[index])
        print(index)        
        
    if button2.is_pressed:
        show_dex_image(seen_names[index])
        print(index)

    if button3.is_pressed:
        run_program(['python', get_path_main_file()])

run_program(['python', get_path_main_file()])
