import cv2

from pokedex.resources import get_model_path, get_classifier_net, get_class_names


def get_video_capture():
    cap = cv2.VideoCapture('libcamerasrc ! video/x-raw, width=640, height=480, framerate=30/1 ! videoconvert ! videoscale ! appsink', cv2.CAP_GSTREAMER)
    cap.set(3, 640)
    cap.set(4, 480)
    return cap


def initialize_net():
    net = cv2.dnn_DetectionModel(model=get_model_path(), config=get_classifier_net())
    net.setInputSize(320, 320)
    net.setInputScale(1.0 / 127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(True)
    return net


def get_objects(img, thres, nms, net, draw=True, objects=[]):
    class_ids, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nms)
    class_names = get_class_names()

    if len(objects) == 0:
        objects = class_names
    object_info = []
    if len(class_ids) != 0:
        for class_id, confidence, box in zip(class_ids.flatten(), confs.flatten(), bbox):
            class_name = class_names[class_id - 1]
            if class_name in objects:
                object_info.append([box, class_name])
                if draw:
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    cv2.putText(img, class_names[class_id - 1].upper(), (box[0] + 10, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    return img, object_info
