import os


def get_config():
    file_name = "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
    return f"{_get_res_dir()}{file_name}"


def get_model():
    file_name = "frozen_inference_graph.pb"
    return f"{_get_res_dir()}{file_name}"


def get_class_names():
    file_name = "coco.names"
    class_file = f"{_get_res_dir()}{file_name}"
    with open(class_file, "rt") as f:
        class_names = f.read().rstrip("\n").split("\n")
    return class_names


def record_found(found_class):
    seen_file = os.path.abspath(f"seen/{found_class}.txt")
    if os.path.isfile(seen_file):
        return
    f = open(seen_file, "w")
    f.close()


def _get_res_dir():
    return "../res/"
