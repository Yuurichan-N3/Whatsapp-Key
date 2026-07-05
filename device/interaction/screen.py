import cv2
from device.adb import client
from utils.config.settings import SCREENCAP_PATH, LOCAL_SCREENCAP


def capture() -> cv2.typing.MatLike:
    client.shell("screencap", "-p", SCREENCAP_PATH)
    client.run("pull", SCREENCAP_PATH, LOCAL_SCREENCAP)
    return cv2.imread(LOCAL_SCREENCAP)


def cleanup():
    client.shell("rm", SCREENCAP_PATH)
    import os
    if os.path.exists(LOCAL_SCREENCAP):
        os.remove(LOCAL_SCREENCAP)
