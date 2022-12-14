import cv2
from pokedex.buttons import button1, button2, button3, button4, browse_seen
from pokedex.classifier import get_objects, initialize_net, get_video_capture
from pokedex.display import show_background, show_dex_image, show_image
from pokedex.resources import save_to_seen, delete_seen, is_class_seen
from pokedex.sound import text_to_speech
import time


cap = get_video_capture()


def run_main_program():
    net = initialize_net()
    show_dex_image("pokeball")

    while True:
        if button1.is_pressed:
            wait_for_start()

        success, img = cap.read()
        result, object_info = get_objects(img=img, thres=0.60, nms=0.9, net=net)
#         cv2.imshow("Output", result)
#         cv2.waitKey(1)
        cv2.imwrite("classification_image.jpg", result)
        show_image("classification_image.jpg")

        for obj in object_info:
            found_class = obj[1]  # loop through objects identified in picture and speak
            if is_class_seen(found_class):
                continue
            show_dex_image(found_class)
            text_to_speech(found_class)
            save_to_seen(found_class)
            if found_class == "dog":
                found_class = "bobi"
                show_dex_image(found_class)
                text_to_speech(found_class)

            wait_for_start()


def wait_for_start():
    show_background()
    while True:
    
        if button1.is_pressed:
            run_main_program()

#         if button2.is_pressed or button3.is_pressed:
        if button2.is_pressed:
            browse_seen()
            show_background()
            time.sleep(0.5)

#         if button4.is_pressed:
        if button3.is_pressed:
            delete_seen()


if __name__ == "__main__":
    wait_for_start()
