import os


clear_console = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")
