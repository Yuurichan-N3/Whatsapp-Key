from colorama import init, Fore, Style

init(autoreset=True)

BOLD = Style.BRIGHT
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
RESET = Style.RESET_ALL


def info(msg):
    print(f"{BOLD}{G}{msg}{RESET}")


def warn(msg):
    print(f"{BOLD}{Y}{msg}{RESET}")


def error(msg):
    print(f"{BOLD}{R}{msg}{RESET}")


def stopped():
    print(f"{BOLD}{R}Script Stopped By User{RESET}")
