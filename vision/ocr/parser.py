import re
import numpy as np
from vision.ocr.reader import get_reader


def read_key(img_cv) -> str:
    h, w = img_cv.shape[:2]
    crop = img_cv[int(h * 0.2):int(h * 0.5), int(w * 0.05):int(w * 0.95)]
    results = get_reader().readtext(crop, allowlist="0123456789")
    for _, text, conf in results:
        digits = re.sub(r"\D", "", text)
        if len(digits) == 4 and conf > 0.5:
            return digits
    return ""


def find_button(img_cv, label: str):
    results = get_reader().readtext(img_cv)
    target = label.lower().replace(" ", "")
    for bbox, detected, conf in results:
        if target in detected.lower().replace(" ", "") and conf > 0.4:
            pts = np.array(bbox)
            cx = int(pts[:, 0].mean())
            cy = int(pts[:, 1].mean())
            return cx, cy
    return None


def find_generate_button(img_cv):
    h, w = img_cv.shape[:2]
    from device.ui.finder import find_clickable_in_band
    return find_clickable_in_band(h, w, 0.25, 0.65, max_area_ratio=0.3)


def find_save_button(img_cv):
    h, w = img_cv.shape[:2]
    from device.ui.finder import find_clickable_in_band
    return find_clickable_in_band(h, w, 0.75, 0.98, min_w_ratio=0.5, max_area_ratio=0.3)