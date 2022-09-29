import cv2
import os
from pokedex.buttons import button1, run_program, button2, button3, button4, browse_seen
from pokedex.classifier import get_objects, initialize_net, get_video_capture
from pokedex.display import show_background, show_dex_image_if_not_already_shown
from pokedex.resources import save_to_seen, delete_seen, is_class_seen, get_path_browse_seen, get_path_switch5
from pokedex.sound import text_to_speech
from time import sleep
import time


cap = get_video_capture()

def run_main_program():
    net = initialize_net()

    while True:
        if button1.is_pressed:
            wait_for_start()

        success, img = cap.read()
        result, object_info = get_objects(img=img, thres=0.80, nms=0.9, net=net)
        cv2.imshow("Output", result)
        cv2.waitKey(1)

        for obj in object_info:
            found_class = obj[1]  # loop through objects identified in picture and speak
            if is_class_seen(found_class):
                continue
            show_dex_image_if_not_already_shown(found_class)
            text_to_speech(found_class)
            save_to_seen(found_class)
            if found_class == "dog":
                found_class = "bobi"
                show_dex_image_if_not_already_shown(found_class)
                text_to_speech(found_class)

            wait_for_start()

      

def wait_for_start():
    show_background()
    while True:
    
        if button1.is_pressed:
            run_main_program()

        if button2.is_pressed or button3.is_pressed:
            browse_seen()
            show_background()
            time.sleep(0.5)

        if button4.is_pressed:
            delete_seen()


if __name__ == "__main__":
    wait_for_start()
