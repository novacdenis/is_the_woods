import os


clear_onsole = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")
