import os
import sys
import zipfile
import urllib.request
from utils.config.settings import ADB_DIR, ADB_URL_WIN, ADB_URL_LIN, ADB_URL_MAC
from utils import logger


def get_adb_path(base_dir: str) -> str:
    folder = os.path.join(base_dir, ADB_DIR)
    if os.name == "nt":
        return os.path.join(folder, "adb.exe")
    return os.path.join(folder, "adb")


def get_url() -> str:
    if os.name == "nt":
        return ADB_URL_WIN
    if sys.platform == "darwin":
        return ADB_URL_MAC
    return ADB_URL_LIN


def ensure_adb(base_dir: str) -> str:
    adb_path = get_adb_path(base_dir)
    if os.path.exists(adb_path):
        return adb_path

    logger.warn("ADB Binary Not Found, Initiating Download")
    url = get_url()
    zip_path = os.path.join(base_dir, "platform-tools.zip")

    with urllib.request.urlopen(url) as response:
        total_size = int(response.headers.get("Content-Length", 0))

    from tqdm import tqdm
    with tqdm(
        total=total_size,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
        desc="  Downloading",
        bar_format="  Downloading [{bar:40}] {percentage:3.0f}% {rate_fmt}",
        ncols=80,
        leave=False,
    ) as bar:
        def reporthook(block_num, block_size, total):
            bar.update(min(block_size, total_size - bar.n))

        urllib.request.urlretrieve(url, zip_path, reporthook=reporthook)

    sys.stdout.write("\r\033[K")
    sys.stdout.flush()

    logger.info("Download Complete, Extracting Platform Tools")

    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(base_dir)

    os.remove(zip_path)
    logger.info("ADB Setup Finished Successfully")
    return adb_path