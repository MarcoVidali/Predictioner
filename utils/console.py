def clear() -> None:
    import os

    command:str = "clear"
    if os.name in ("nt", "dos"): command = "cls"
    os.system(command)