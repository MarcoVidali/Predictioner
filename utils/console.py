def clear() -> None:
    import os

    command:str = "clear"
    if os.name in ("nt", "dos"): command = "cls"
    os.system(command)
    
def white() -> str:
    from colorama import Fore
    return Fore.WHITE
def blue() -> str:
    from colorama import Fore
    return Fore.LIGHTBLUE_EX
def red() -> str:
    from colorama import Fore
    return Fore.LIGHTRED_EX
def green() -> str:
    from colorama import Fore
    return Fore.LIGHTGREEN_EX