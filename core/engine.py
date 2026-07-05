import threading
from utils import logger


def run(targets: list, save_ss: bool):
    from core.worker import search_loop

    target_set = set(targets)
    logger.info(f"Initiating Search For Keys {', '.join(targets)}")

    stop_event = threading.Event()
    result_holder = []

    t = threading.Thread(
        target=search_loop,
        args=(target_set, save_ss, result_holder, stop_event),
        daemon=True
    )
    t.start()

    try:
        while t.is_alive():
            t.join(timeout=0.5)
    except KeyboardInterrupt:
        stop_event.set()
        t.join(timeout=3)
        raise

    if result_holder:
        logger.info(f"Search Completed Successfully With Key {result_holder[0]}")
    else:
        logger.warn("Search Ended Without Any Matching Key")