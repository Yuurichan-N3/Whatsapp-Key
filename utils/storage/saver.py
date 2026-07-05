import os
import shutil
from datetime import datetime
from utils.config.settings import SCREENSHOT_DIR
from utils import logger


def save_screenshot(local_path: str, key: str):
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(SCREENSHOT_DIR, f"key_{key}_{ts}.png")
    shutil.copy(local_path, dest)
    logger.info(f"Screenshot Successfully Saved To {dest}")
    return dest
