import os
import re
import xml.etree.ElementTree as ET
from device.adb import client
from utils import logger

_UI_DEVICE_PATH = "/sdcard/_wakey_ui.xml"
_UI_LOCAL_PATH = "_wakey_ui.xml"
_XML_DIR = "xml"
_XML_SAVE_PATH = os.path.join(_XML_DIR, "UI_hierarchy.xml")


def _dump():
    client.shell("uiautomator", "dump", _UI_DEVICE_PATH)
    client.run("pull", _UI_DEVICE_PATH, _UI_LOCAL_PATH)
    if not os.path.exists(_UI_LOCAL_PATH):
        return None
    try:
        os.makedirs(_XML_DIR, exist_ok=True)
        with open(_UI_LOCAL_PATH, "r", encoding="utf-8", errors="ignore") as f:
            raw = f.read()
        with open(_XML_SAVE_PATH, "w", encoding="utf-8") as f:
            f.write(raw)
        return ET.fromstring(raw)
    except ET.ParseError:
        return None


def _parse_bounds(bounds_str):
    nums = list(map(int, re.findall(r"\d+", bounds_str)))
    if len(nums) == 4:
        x1, y1, x2, y2 = nums
        return (x1 + x2) // 2, (y1 + y2) // 2, x2 - x1, y2 - y1
    return None


def _get_descendant_texts(node):
    texts = []
    for child in node.iter("node"):
        t = child.get("text", "").strip()
        if t:
            texts.append(t)
    return texts


def find_clickable_in_band(img_h, img_w, y_min_ratio, y_max_ratio, min_w_ratio=0.0, max_area_ratio=0.5):
    root = _dump()
    if root is None:
        logger.warn("UI Dump Failed Or Returned Empty Tree")
        return None

    max_area = img_h * img_w * max_area_ratio
    candidates = []
    for node in root.iter("node"):
        if node.get("clickable") != "true":
            continue
        parsed = _parse_bounds(node.get("bounds", ""))
        if not parsed:
            continue
        cx, cy, nw, nh = parsed
        area = nw * nh
        if area > max_area:
            continue
        if y_min_ratio * img_h <= cy <= y_max_ratio * img_h and nw >= min_w_ratio * img_w:
            candidates.append((area, cx, cy, nw, nh))

    if not candidates:
        logger.warn("Generate Button Not Found In Frame")
        return None

    candidates.sort(key=lambda c: c[0])
    best = candidates[0]
    return best[1], best[2]