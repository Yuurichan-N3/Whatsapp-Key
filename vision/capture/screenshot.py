from device.interaction.screen import capture, cleanup
from utils.storage.saver import save_screenshot
from utils.config.settings import LOCAL_SCREENCAP
from utils import logger


def take():
    return capture()


def take_and_save(key: str):
    img = capture()
    path = save_screenshot(LOCAL_SCREENCAP, key)
    logger.info(f"Match Screenshot Captured And Saved {path}")
    return img
