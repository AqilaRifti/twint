from colorama import Fore, Style, init

init(autoreset=True)

def log(message):
    print(f"{message}")

def info(message):
    log(f"{Style.BRIGHT}{Fore.BLUE}{message}")

def warn(message):
    log(f"{Style.BRIGHT}{Fore.YELLOW}{message}")

def error(message):
    log(f"{Style.BRIGHT}{Fore.RED}Error: {message}")
    quit()

def succeed(message):
    log(f"{Style.BRIGHT}{Fore.GREEN}{message}")
