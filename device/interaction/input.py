from device.adb import client


def tap(x: int, y: int):
    client.shell("input", "tap", str(x), str(y))
