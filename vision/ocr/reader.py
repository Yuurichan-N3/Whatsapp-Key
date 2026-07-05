import warnings
import logging
import easyocr

warnings.filterwarnings("ignore")
logging.getLogger("torch").setLevel(logging.ERROR)
logging.getLogger("easyocr").setLevel(logging.ERROR)

_reader = None


def get_reader() -> easyocr.Reader:
    global _reader
    if _reader is None:
        import os
        os.environ["PYTHONWARNINGS"] = "ignore"
        _reader = easyocr.Reader(["en"], gpu=False, verbose=False)
    return _reader