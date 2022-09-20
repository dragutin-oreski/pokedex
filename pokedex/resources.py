import os


def get_classifier_net():
    return f"{_get_classifier_dir()}/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"


def get_model_path():
    return f"{_get_classifier_dir()}/frozen_inference_graph.pb"


def get_class_names():
    class_file = _get_class_file()
    with open(class_file, "rt") as f:
        class_names = f.read().rstrip("\n").split("\n")
    return class_names


def get_path_main_file():
    return f"{_get_root_path()}/main.py"


def get_path_browse_seen():
    return f"{_get_root_path()}/pokedex/browse_seen.py"


def get_path_switch5():
    return f"{_get_root_path()}/switch5.py"


def save_to_seen(found_class):
    """
    If it doesn't exist already, add found_class to seen folder
    """
    seen_file = get_seen_file(found_class)
    if os.path.isfile(seen_file):
        return
    f = open(seen_file, "w")
    f.close()


def is_class_seen(found_class):
    return bool(os.path.isfile(get_seen_file(found_class)))


def get_seen_file(found_class):
    return f"{_get_seen_dir()}/{found_class}.txt"


def get_image_from_dex(found_class):
    return f"{_get_dex_entries_dir()}/images/{found_class}.jpg"


def get_background_image():
    return f"{_get_res_dir()}/background_image.jpg"


def get_seen_names():
    return [os.path.splitext(filename)[0] for filename in os.listdir(_get_seen_dir())]


def delete_seen():
    for file in os.scandir(_get_seen_dir()):
        os.remove(file.path)


def get_description_from_dex(found_class):
    with open(_get_description_from_dex_file(found_class), "r") as f:
        dex_entry = f.read().rstrip()
    return dex_entry


def _get_description_from_dex_file(found_class):
    return f"{_get_dex_entries_dir()}/descriptions/{found_class}.txt"


def _get_class_file():
    return f"{_get_classifier_dir()}/coco.names"


def _get_dex_entries_dir():
    return f"{_get_classified_dir()}/dex_entries"


def _get_classified_entry_file(found_class):
    return f"{_get_classified_dir()}/dex/{found_class}.txt"


def _get_seen_dir():
    return f"{_get_classified_dir()}/seen"


def _get_classified_dir():
    return f"{_get_res_dir()}/classified"


def _get_classifier_dir():
    return f"{_get_res_dir()}/classifier"


def _get_res_dir():
    return f"{_get_root_path()}/res"


def _get_root_path():
    return os.path.abspath(os.path.join(os.path.join(__file__, os.pardir), os.pardir))
