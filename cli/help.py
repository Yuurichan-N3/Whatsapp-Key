from utils import logger


def show_help():
    lines = [
        ("info",  "Usage: python bot.py [options] [targets]"),
        ("blank", ""),
        ("warn",  "Target Keys:"),
        ("info",  "  --1234                Search For A Specific Key"),
        ("info",  "  --1234 --5678         Search Multiple Keys, Stop On First Match"),
        ("info",  "  --twin                Search All Repeated Keys 0000 To 9999"),
        ("blank", ""),
        ("warn",  "Options:"),
        ("info",  "  --ss                  Save Screenshot When Target Key Is Found"),
        ("info",  "  --help                Display This Help Message"),
        ("blank", ""),
        ("warn",  "Usage Examples:"),
        ("info",  "  python bot.py --7777"),
        ("info",  "  python bot.py --1111 --2222 --3333"),
        ("info",  "  python bot.py --ss --7777 --1234"),
        ("blank", ""),
        ("warn",  "Before Running:"),
        ("info",  "  Plug Your Phone Into PC Via USB Cable"),
        ("info",  "  Open WhatsApp And Navigate To The Username Key Page"),
    ]
    for kind, text in lines:
        if kind == "blank":
            print()
        elif kind == "warn":
            logger.warn(text)
        else:
            logger.info(text)
