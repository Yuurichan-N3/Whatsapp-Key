import subprocess
from utils import logger


_adb_path = "adb"


def init(path: str):
    global _adb_path
    _adb_path = path


def run(*args) -> subprocess.CompletedProcess:
    return subprocess.run([_adb_path] + list(args), capture_output=True)


def connect_usb():
    result = run("devices")
    output = result.stdout.decode().strip()
    lines = [l for l in output.splitlines() if l and "List" not in l and "device" in l]
    if not lines:
        logger.error("No Device Detected Via USB Connection")
        raise SystemExit(1)
    device_id = lines[0].split()[0]
    logger.info(f"Device Successfully Connected With ID {device_id}")


def shell(*args) -> str:
    result = run("shell", *args)
    return result.stdout.decode().strip()
