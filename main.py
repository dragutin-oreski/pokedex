import cv2
import os
from pokedex.buttons import button1, open_switch_and_die, button2, button3
from pokedex.classifier import get_objects, initialize_net, get_video_capture
from pokedex.display import splash_screen, dex_image
from pokedex.resources import record_found, delete_seen
from pokedex.sound import text_to_speech


def main():
    cap = get_video_capture()
    net = initialize_net()
    splash_ran = False

    while True:

        if not splash_ran:
            splash_screen()
            splash_ran = True
        if button1.is_pressed:
            open_switch_and_die(['python', 'switch5.py'])
        if button2.is_pressed:
            open_switch_and_die(['python', 'switch4.py'])
        if button3.is_pressed:
            delete_seen()
        success, img = cap.read()
        result, object_info = get_objects(img=img, thres=0.60, nms=0.9, net=net)
        cv2.imshow("Output", result)
        cv2.waitKey(1)

        for obj in object_info:
            found_class = obj[1]  # loop through objects identified in picture and speak
            seen_file = os.path.abspath("seen/" + found_class + '.txt')
            if os.path.isfile(seen_file):
                continue
            dex_image(found_class)
            text_to_speech(found_class)
            record_found(found_class)
            splash_ran = False


if __name__ == "__main__":
    main()
